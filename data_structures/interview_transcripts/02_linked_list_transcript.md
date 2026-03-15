# Linked List — Human Language Transcript

In this problem, the flow starts when we receive the input for **Linked List**.

First, we set up the core data we need to track the process correctly. In this solution, that means node pointers (`head`, optional `tail`, and next/prev links).

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is insert/delete is done by rewiring local pointers instead of shifting elements.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: list connectivity is preserved after every pointer update.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from the updated list structure and traversal output.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: O(1) local insert/delete with pointer known, O(n) search** and **Space: O(1) extra**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
