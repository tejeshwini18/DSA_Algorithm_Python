# Quick Sort — Human Language Transcript

In this problem, the flow starts when we receive the input for **Quick Sort**.

First, we set up the core data we need to track the process correctly. In this solution, that means a partition strategy around a pivot and recursive subranges.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is partition places pivot in final index, then recurse left and right sections.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: after partition, left side <= pivot <= right side.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the concatenation implied by recursively sorted partitions.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: Average O(n log n), worst O(n^2)** and **Space: O(log n) average recursion**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
