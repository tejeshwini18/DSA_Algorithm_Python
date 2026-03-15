# First Non-Repeating Character — Human Language Transcript

In this problem, the flow starts when we receive the input for **First Non-Repeating Character**.

First, we set up the core data we need to track the process correctly. In this solution, that means a frequency count map and second pass through original order.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is first pass counts occurrences; second pass finds first character with count 1.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: frequency map is complete and accurate before selection pass.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the earliest character with frequency one.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(n)** and **Space: O(k)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
