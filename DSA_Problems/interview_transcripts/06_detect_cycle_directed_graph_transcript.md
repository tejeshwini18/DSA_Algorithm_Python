# Detect Cycle in Directed Graph — Human Language Transcript

In this problem, the flow starts when we receive the input for **Detect Cycle in Directed Graph**.

First, we set up the core data we need to track the process correctly. In this solution, that means an adjacency list and DFS color states (unvisited, visiting, done).

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is during DFS, if we meet a currently visiting node, we found a back-edge cycle.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: the recursion stack color exactly marks active path nodes.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from whether a back-edge is found (or equivalently topo count < n in Kahn).

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(V + E)** and **Space: O(V + E)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
