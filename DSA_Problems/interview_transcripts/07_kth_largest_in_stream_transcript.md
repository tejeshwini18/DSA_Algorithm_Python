# Kth Largest in a Stream — Human Language Transcript

In this problem, the flow starts when we receive the input for **Kth Largest in a Stream**.

First, we set up the core data we need to track the process correctly. In this solution, that means a min-heap that stores only k largest seen values.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is every new value is pushed; if heap size > k, smallest is removed.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: heap always contains exactly the k largest elements seen so far.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the heap root, which is the kth largest.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(log k) per add** and **Space: O(k)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
