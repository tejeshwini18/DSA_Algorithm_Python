# Queue — Human Language Transcript

In this problem, the flow starts when we receive the input for **Queue**.

First, we set up the core data we need to track the process correctly. In this solution, that means FIFO operations (`enqueue`, `dequeue`) using front/rear tracking.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is new items join rear, removals happen from front.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: oldest unprocessed element is always served next.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the dequeued sequence or final queue state.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(1) with deque implementation** and **Space: O(n)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
