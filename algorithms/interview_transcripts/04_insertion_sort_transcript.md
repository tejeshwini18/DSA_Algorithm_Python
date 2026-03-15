# Insertion Sort — Human Language Transcript

In this problem, the flow starts when we receive the input for **Insertion Sort**.

First, we set up the core data we need to track the process correctly. In this solution, that means a growing sorted prefix at the start of the array.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is for each new element, shift larger prefix elements right and insert into gap.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: prefix `[0..i]` is sorted after processing index `i`.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the final array once all elements are inserted.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(n^2) worst, O(n) best on nearly sorted input** and **Space: O(1)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
