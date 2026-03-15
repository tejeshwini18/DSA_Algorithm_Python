# Find Max and Min — Human Language Transcript

In this problem, the flow starts when we receive the input for **Find Max and Min**.

First, we set up the core data we need to track the process correctly. In this solution, that means two running values: current max and current min.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is each new number compares once against current max/min and updates as needed.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: running pair always reflects processed prefix extremes.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from final max and min values.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(n)** and **Space: O(1)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
