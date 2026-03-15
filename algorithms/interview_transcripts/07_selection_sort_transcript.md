# Interview Transcript: Selection Sort

## Problem in simple words
**Interviewer:** Explain what this question is testing.

**Candidate:** This problem is about **Selection Sort**. Core idea: Repeatedly select the minimum from unsorted portion and place it at the next fixed index.

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

For this topic, the invariant is tied directly to `Selection Sort` and that is why correctness is easy to justify.

## Walkthrough (how I narrate)
- Start with a tiny input.
- Show initial state variables.
- Describe one full iteration/recursive level.
- Repeat until termination and confirm final answer.

## Complexity to state confidently
- **Time:** `O(n^2)` always.
- **Space:** `O(1)` in-place.

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
