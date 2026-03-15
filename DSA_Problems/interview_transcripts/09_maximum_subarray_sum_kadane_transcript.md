# Maximum Subarray (Kadane) — Human Language Transcript

In this problem, the flow starts when we receive the input for **Maximum Subarray (Kadane)**.

First, we set up the core data we need to track the process correctly. In this solution, that means two running values: best ending here and global best.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is for each number, we decide restart at current number or extend previous sum.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: best ending here is always best possible subarray ending at current index.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the global best tracked across all positions.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(n)** and **Space: O(1)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
