# Selection Sort — Human Language Transcript

In this problem, the flow starts when we receive the input for **Selection Sort**.

First, we set up the core data we need to track the process correctly. In this solution, that means a boundary between sorted prefix and unsorted suffix.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is each step finds minimum in unsorted suffix and swaps it to boundary index.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: sorted prefix always contains globally smallest elements in correct order.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the array after boundary reaches end.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(n^2)** and **Space: O(1)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
