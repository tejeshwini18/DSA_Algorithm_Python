# Merge K Sorted Lists — Human Language Transcript

In this problem, the flow starts when we receive the input for **Merge K Sorted Lists**.

First, we set up the core data we need to track the process correctly. In this solution, that means a min-heap seeded with each list head.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is we repeatedly pop smallest node, attach it to output, and push its next node if present.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: heap always stores the smallest unmerged candidate from each active list.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the merged linked list built from the dummy pointer.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(N log k)** and **Space: O(k)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
