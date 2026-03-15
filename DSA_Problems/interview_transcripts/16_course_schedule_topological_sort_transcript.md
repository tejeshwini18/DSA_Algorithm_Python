# Course Schedule (Topological Sort) — Human Language Transcript

In this problem, the flow starts when we receive the input for **Course Schedule (Topological Sort)**.

First, we set up the core data we need to track the process correctly. In this solution, that means indegree array, adjacency list, and queue of zero-indegree courses.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is we process zero-indegree courses and reduce indegrees of dependents.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: a course enters queue only when all prerequisites are satisfied.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from processed course count (or produced order length).

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(V + E)** and **Space: O(V + E)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
