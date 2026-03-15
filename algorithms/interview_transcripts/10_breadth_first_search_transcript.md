# Breadth First Search (BFS) — Human Language Transcript

In this problem, the flow starts when we receive the input for **Breadth First Search (BFS)**.

First, we set up the core data we need to track the process correctly. In this solution, that means a queue and visited set initialized with start node.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is we pop front node, expand neighbors, and enqueue unseen neighbors.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: nodes are visited in non-decreasing distance from source.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the traversal order, shortest level distances, or target reach step.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(V + E)** and **Space: O(V)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
