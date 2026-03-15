# Rotate List/Array — Human Language Transcript

In this problem, the flow starts when we receive the input for **Rotate List/Array**.

First, we set up the core data we need to track the process correctly. In this solution, that means effective rotation size `k % n` and boundary split.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is we reconnect/slice so last `k` segment moves to front.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: relative order inside both moved and remaining segments is preserved.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the rotated sequence/list head.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(n)** and **Space: O(1) or O(n) depending on representation**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
