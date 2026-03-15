# LRU Cache — Human Language Transcript

In this problem, the flow starts when we receive the input for **LRU Cache**.

First, we set up the core data we need to track the process correctly. In this solution, that means a capacity and an `OrderedDict` where key order represents recency.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is on `get`, we move the key to the end; on `put`, we insert/update and evict from the front if capacity is exceeded.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: the dictionary always contains the most recent items in correct LRU order.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the value from `get` or the current cache content after eviction checks.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(1) per get/put (amortized)** and **Space: O(capacity)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
