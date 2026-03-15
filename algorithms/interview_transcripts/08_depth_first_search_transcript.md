# Depth First Search (DFS) — Human Language Transcript

In this problem, the flow starts when we receive the input for **Depth First Search (DFS)**.

First, we set up the core data we need to track the process correctly. In this solution, that means a recursion stack (or explicit stack) and visited tracking.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is from each node, we go as deep as possible before backtracking.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: a node is processed once, and all reachable descendants are explored before return.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the traversal order / reachability set collected.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(V + E)** and **Space: O(V)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
