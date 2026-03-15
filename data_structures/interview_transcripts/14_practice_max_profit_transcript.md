# Best Time to Buy and Sell Stock — Human Language Transcript

In this problem, the flow starts when we receive the input for **Best Time to Buy and Sell Stock**.

First, we set up the core data we need to track the process correctly. In this solution, that means running minimum buy price and running best profit.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is each price updates min price first, then potential profit against current price.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: best profit is maximum achievable with one buy before sell.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the maximum profit after one pass.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(n)** and **Space: O(1)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
