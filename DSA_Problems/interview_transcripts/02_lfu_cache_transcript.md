# LFU Cache — Human Language Transcript

In this problem, the flow starts when we receive the input for **LFU Cache**.

First, we set up the core data we need to track the process correctly. In this solution, that means a key->node map, frequency->doubly linked list buckets, and `min_freq`.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is every access increases a node frequency and moves it to the next bucket; eviction happens from the lowest-frequency bucket.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: items are grouped by exact frequency, and tie-breaking follows recency inside each frequency bucket.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the updated node value for queries, and the proper victim node during eviction.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(1) amortized per operation** and **Space: O(capacity)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
