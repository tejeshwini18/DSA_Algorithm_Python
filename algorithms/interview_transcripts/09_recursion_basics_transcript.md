# Recursion Basics — Human Language Transcript

In this problem, the flow starts when we receive the input for **Recursion Basics**.

First, we set up the core data we need to track the process correctly. In this solution, that means a clear base case and a recursive reduction step.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is each call transforms the problem into a smaller equivalent subproblem.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: every recursive chain must strictly progress toward base case.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the return value propagated back through call stack.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: depends on specific recurrence** and **Space: depends on recursion depth**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
