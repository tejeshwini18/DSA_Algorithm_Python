# Binary Search — Human Language Transcript

In this problem, the flow starts when we receive the input for **Binary Search**.

First, we set up the core data we need to track the process correctly. In this solution, that means two pointers (`low`, `high`) over a sorted array.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is we compare middle value with target and discard half of the search range each step.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: if target exists, it always remains inside current `[low, high]` range.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the index when middle equals target, or failure when range collapses.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(log n)** and **Space: O(1)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
