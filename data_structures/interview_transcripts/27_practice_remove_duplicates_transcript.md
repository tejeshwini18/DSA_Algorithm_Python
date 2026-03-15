# Remove Duplicates — Human Language Transcript

In this problem, the flow starts when we receive the input for **Remove Duplicates**.

First, we set up the core data we need to track the process correctly. In this solution, that means either seen-set or two-pointer on sorted array.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is we keep one representative per value and skip repeats.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: output prefix/set contains unique values only.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from deduplicated length/collection.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(n)** and **Space: O(1) sorted-two-pointer or O(n) set**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
