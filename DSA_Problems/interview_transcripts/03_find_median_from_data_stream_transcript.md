# Find Median from Data Stream — Human Language Transcript

In this problem, the flow starts when we receive the input for **Find Median from Data Stream**.

First, we set up the core data we need to track the process correctly. In this solution, that means two heaps: max-heap for lower half and min-heap for upper half.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is we push into lower half, rebalance across heaps, and keep sizes balanced.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: all values in lower heap are <= all values in upper heap.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from heap tops (one top for odd count, average of two tops for even count).

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(log n) insert, O(1) median query** and **Space: O(n)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
