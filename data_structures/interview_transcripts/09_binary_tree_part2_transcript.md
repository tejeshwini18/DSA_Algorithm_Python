# Interview Transcript: Binary Tree Part 2

## Problem framing
**Interviewer:** What is this structure/problem about?

**Candidate:** This topic is **Binary Tree Part 2**. Practical interview idea: Combine traversal + state propagation for advanced binary-tree queries.

## Clarifications before coding
- Expected operations and their target complexities.
- Behavior for empty structure / missing keys.
- Whether ordering, stability, or uniqueness matters.

## Baseline vs better approach
**Candidate:** I quickly mention naive simulation, then switch to the data-structure-aware method that avoids repeated full scans.

## Strong interview explanation
- Define the invariant (ordering/frequency/parent-child relation/etc.).
- Show how each operation preserves the invariant.
- Mention one tricky edge case and how code handles it.

## Complexity
- **Time:** Depends on query; common traversals remain `O(n)`.
- **Space:** `O(h)` recursion/aux state.

## Common follow-ups
- Can you support this in streaming mode?
- What breaks in worst-case input?
- How would you test inserts, deletes, and boundary cases?

## Final pitch
**Candidate:** I would implement the operations with invariant-first reasoning, then prove correctness operation-by-operation.
