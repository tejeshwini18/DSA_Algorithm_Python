# Graph — Human Language Transcript

In this problem, the flow starts when we receive the input for **Graph**.

First, we set up the core data we need to track the process correctly. In this solution, that means an adjacency list plus traversal state.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is we iterate neighbors through BFS/DFS depending on task.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: visited set prevents duplicate processing and preserves traversal correctness.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from reachability/order/path-related result from full traversal.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(V + E)** and **Space: O(V + E)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
