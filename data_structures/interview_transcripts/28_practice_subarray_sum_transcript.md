# Subarray Sum — Human Language Transcript

In this problem, the flow starts when we receive the input for **Subarray Sum**.

First, we set up the core data we need to track the process correctly. In this solution, that means running prefix sum and map of prefix frequencies/indices.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is for each index, we check whether `prefix - target` was seen before.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: prefix map represents all sums from earlier positions.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from count/existence of target-sum subarrays.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(n)** and **Space: O(n)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
