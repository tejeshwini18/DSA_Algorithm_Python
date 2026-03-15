# Recursive BST (rBST) — Human Language Transcript

In this problem, the flow starts when we receive the input for **Recursive BST (rBST)**.

First, we set up the core data we need to track the process correctly. In this solution, that means BST ordering invariant with recursive insert/search/delete.

Next, we process the input step by step, and after each step we update our state so the algorithm stays correct. The key transition here is we branch left or right based on key comparisons and recurse.

As the loop or recursion continues, the algorithm keeps preserving one important invariant: for every node, left subtree keys < node < right subtree keys.

When the traversal/processing ends, we read the final value from the maintained state and return the required answer. In this implementation, the result comes from search result or updated BST after recursive operation.

This gives us an efficient solution because we avoid recomputing work from scratch on every step. The complexity is **Time: Average O(log n), worst O(n)** and **Space: O(h) recursion**.

So in interview language, the full story is: initialize the right structure, update it consistently for each element/operation, preserve the invariant, and extract the answer from the final maintained state.
