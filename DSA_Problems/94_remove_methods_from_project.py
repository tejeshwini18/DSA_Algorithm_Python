"""Remove specified class methods from a Python project."""

import argparse
import ast
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple


class MethodRemover:
    def __init__(self, project_root: str, method_names: Sequence[str], extensions: Sequence[str] = (".py",)):
        self.project_root = Path(project_root)
        self.method_names = set(name.strip() for name in method_names if name.strip())
        self.extensions = tuple(extensions)

    def find_source_files(self) -> List[Path]:
        if not self.project_root.exists():
            raise FileNotFoundError(f"Project root not found: {self.project_root}")

        return [
            path
            for path in self.project_root.rglob("*")
            if path.is_file() and path.suffix in self.extensions
        ]

    def remove_methods_from_file(self, path: Path) -> bool:
        source = path.read_text(encoding="utf-8")
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return False

        ranges = self._collect_method_ranges(tree)
        if not ranges:
            return False

        lines = source.splitlines(keepends=True)
        merged_ranges = self._merge_ranges(ranges)
        remaining = [
            line
            for index, line in enumerate(lines, start=1)
            if not any(start <= index <= end for start, end in merged_ranges)
        ]

        cleaned = self._collapse_blank_lines(remaining)
        path.write_text("".join(cleaned), encoding="utf-8")
        return True

    def _collect_method_ranges(self, tree: ast.AST) -> List[Tuple[int, int]]:
        collector = _MethodRangeCollector(self.method_names)
        collector.visit(tree)
        return collector.ranges

    @staticmethod
    def _merge_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if not ranges:
            return []

        sorted_ranges = sorted(ranges)
        merged = [sorted_ranges[0]]
        for start, end in sorted_ranges[1:]:
            last_start, last_end = merged[-1]
            if start <= last_end + 1:
                merged[-1] = (last_start, max(last_end, end))
            else:
                merged.append((start, end))
        return merged

    @staticmethod
    def _collapse_blank_lines(lines: List[str]) -> List[str]:
        cleaned: List[str] = []
        previous_blank = False
        for line in lines:
            if line.strip() == "":
                if not previous_blank:
                    cleaned.append(line)
                previous_blank = True
            else:
                cleaned.append(line)
                previous_blank = False
        return cleaned


class _MethodRangeCollector(ast.NodeVisitor):
    def __init__(self, method_names: Iterable[str]):
        self.method_names = set(method_names)
        self.ranges: List[Tuple[int, int]] = []
        self._class_stack: List[ast.ClassDef] = []

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self._class_stack.append(node)
        self.generic_visit(node)
        self._class_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._collect_range(node)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._collect_range(node)
        self.generic_visit(node)

    def _collect_range(self, node: ast.AST) -> None:
        if not self._class_stack or getattr(node, "name", None) not in self.method_names:
            return

        start_lineno = self._starting_line(node)
        end_lineno = getattr(node, "end_lineno", node.lineno)
        self.ranges.append((start_lineno, end_lineno))

    @staticmethod
    def _starting_line(node: ast.AST) -> int:
        if decorators := getattr(node, "decorator_list", None):
            return min(decorator.lineno for decorator in decorators)
        return getattr(node, "lineno", 0)


def remove_suspicious_methods(n: int, k: int, invocations: List[List[int]]) -> List[int]:
    """Return remaining methods after removing suspicious methods starting from k."""
    graph = {i: [] for i in range(1, n + 1)}
    for caller, callee in invocations:
        graph[caller].append(callee)

    suspicious = set()
    stack = [k]
    while stack:
        node = stack.pop()
        if node in suspicious:
            continue
        suspicious.add(node)
        for child in graph.get(node, []):
            if child not in suspicious:
                stack.append(child)

    for caller, callee in invocations:
        if caller not in suspicious and callee in suspicious:
            return list(range(1, n + 1))

    return [method for method in range(1, n + 1) if method not in suspicious]


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Remove specified class methods from a Python project.")
    parser.add_argument("root", nargs="?", default=".", help="Project root directory to scan for Python files. Defaults to current directory.")
    parser.add_argument(
        "methods",
        nargs="*",
        help="Method names to remove from class definitions. Provide one or more names.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply changes to files. Without this flag, runs in dry-run mode and reports files that would change.",
    )
    return parser.parse_args()


def run_demo() -> None:
    examples = [
        {
            "name": "removal possible",
            "n": 5,
            "k": 2,
            "invocations": [[2, 3], [3, 4], [1, 5]],
            "expected": [1, 5],
            "reason": "No outside invocation into suspicious methods 2->3->4.",
        },
        {
            "name": "removal blocked",
            "n": 5,
            "k": 2,
            "invocations": [[2, 3], [1, 3], [4, 5]],
            "expected": [1, 2, 3, 4, 5],
            "reason": "Method 3 is suspicious but is also invoked from outside by method 1.",
        },
    ]

    print("Demo mode: verifying suspicious-method removal logic")
    print("---------------------------------------------------")
    for example in examples:
        result = remove_suspicious_methods(example["n"], example["k"], example["invocations"])
        passed = result == example["expected"]
        print(f"Example: {example['name']}")
        print(f"  n={example['n']}, k={example['k']}, invocations={example['invocations']}")
        print(f"  expected: {example['expected']}")
        print(f"  actual:   {result}")
        print(f"  reason:   {example['reason']}")
        print(f"  status:   {'PASS' if passed else 'FAIL'}")
        print()
    print("Run `python 94_remove_methods_from_project.py . method_name ...` to remove class methods from your project files.")


def main() -> None:
    args = parse_arguments()
    if not args.methods:
        run_demo()
        return

    remover = MethodRemover(args.root, args.methods)
    files = remover.find_source_files()

    if not files:
        print(f"No Python files found under {args.root}")
        return

    modified_files = []
    for path in files:
        changed = remover.remove_methods_from_file(path)
        if changed:
            modified_files.append(path)
            action = "Updated" if args.apply else "Would update"
            print(f"{action}: {path}")

    if modified_files:
        summary = "Modified" if args.apply else "Would modify"
        print(f"{summary} {len(modified_files)} file(s).")
    else:
        print("No matching class methods found.")


if __name__ == "__main__":
    main()
