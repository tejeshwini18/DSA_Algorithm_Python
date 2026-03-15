# Stack — Human Language Transcript

In this problem, the flow starts when we receive the input for **Stack**.

First, we set up the core data we need to track the process correctly. In this solution, that means LIFO operations (`push`, `pop`, `peek`) on top pointer.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is new items go to top, and removals happen from top only.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: most recently inserted element is always removed first.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the popped/peeked value and final stack state.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(1) per operation** and **Space: O(n)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
