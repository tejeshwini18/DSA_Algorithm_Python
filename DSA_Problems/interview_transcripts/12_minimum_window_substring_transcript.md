# Minimum Window Substring — Human Language Transcript

In this problem, the flow starts when we receive the input for **Minimum Window Substring**.

First, we set up the core data we need to track the process correctly. In this solution, that means a need-frequency map, current window counts, and satisfied counter.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is expand right to satisfy all needs, then shrink left while still valid.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: window is valid exactly when all required character counts are met.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the smallest valid window boundaries recorded.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(|s| + |t|)** and **Space: O(alphabet)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
