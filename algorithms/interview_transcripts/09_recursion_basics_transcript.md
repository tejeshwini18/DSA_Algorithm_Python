# Interview Transcript: Recursion Basics

## Problem in simple words
**Interviewer:** Explain what this question is testing.

**Candidate:** This problem is about **Recursion Basics**. Core idea: Define a base case and a smaller subproblem so each call progresses toward termination.

## Clarifying points I would ask
1. Are there input size limits that force better than `O(n^2)`?
2. Is input always valid (sorted array, connected graph, etc.)?
3. Do we need in-place output, stable order, or just correctness?

## Brute-force baseline
**Candidate:** I first mention the naive way (linear scan / repeated swapping / full traversal), then explain why it is too slow for bigger input.

## Optimal interview approach (spoken)
**Candidate:**
- I keep one invariant throughout execution.
- Each iteration updates only the minimal state needed.
- I stop as soon as answer is guaranteed.

For this topic, the invariant is tied directly to `Recursion Basics` and that is why correctness is easy to justify.

## Walkthrough (how I narrate)
- Start with a tiny input.
- Show initial state variables.
- Describe one full iteration/recursive level.
- Repeat until termination and confirm final answer.

## Complexity to state confidently
- **Time:** Depends on recurrence relation of the specific function.
- **Space:** Depends on recursion depth.

## Common edge cases
- Empty or one-element input.
- Duplicate values or ties.
- Already sorted / reverse sorted patterns.
- Impossible target case (where applicable).

## Follow-up prompts
- Can we make it iterative/recursive alternative?
- Can we reduce auxiliary memory?
- How would we test worst-case behavior quickly?

## Closing line
**Candidate:** I would code this with clear variable names, prove the invariant in 2-3 lines, and validate with edge-case tests.
