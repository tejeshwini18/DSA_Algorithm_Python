# Bubble Sort — Human Language Transcript

In this problem, the flow starts when we receive the input for **Bubble Sort**.

First, we set up the core data we need to track the process correctly. In this solution, that means nested passes over adjacent pairs and a swap flag.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is in each pass, adjacent out-of-order elements are swapped so largest unsorted value moves right.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: after pass `p`, last `p` elements are in final sorted position.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the fully sorted array after no swaps / all passes.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(n^2) worst, O(n) best with early exit** and **Space: O(1)**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
