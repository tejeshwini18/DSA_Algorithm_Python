# Remove Element — Human Language Transcript

In this problem, the flow starts when we receive the input for **Remove Element**.

First, we set up the core data we need to track the process correctly. In this solution, that means a read pointer and write pointer.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is we copy only allowed elements to write position and skip target value.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: prefix `[0..write-1]` always contains kept elements compactly.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from new logical length (and compacted prefix array).

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(n)** and **Space: O(1)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
