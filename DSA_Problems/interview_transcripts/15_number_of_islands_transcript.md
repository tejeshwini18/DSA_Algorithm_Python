# Interview Transcript: Number of Islands

## 1) Problem in plain English
**Interviewer:** Explain the problem quickly.

**Candidate:** We need to solve **Number of Islands**. The clean approach is: Scan grid; when land found, increment count and DFS/BFS flood-fill to mark whole island as visited.

## 2) Clarifying questions I would ask first
**Candidate:** Before I code, I would confirm:
- Exact input format and constraints.
- Expected behavior for empty input or impossible cases.
- Whether we optimize for latency per operation or total batch runtime.

## 3) Brute-force I would mention (briefly)
**Candidate:** A straightforward baseline is to simulate all options or repeatedly scan/recompute.
That makes correctness easy to reason about, but it is usually too slow for interview constraints.
I mention it quickly, then move to the optimal design.

## 4) Optimal approach (what I would say while whiteboarding)
**Candidate:**
- I choose data structures that preserve the key invariant after every step.
- Each update/query touches only what is necessary.
- This avoids repeated full rescans and gives predictable complexity.
- I also keep edge-case handling explicit (empty input, ties, impossible result).

## 5) Why this works (short correctness argument)
**Candidate:** The algorithm is correct because every operation maintains the same invariant the answer depends on.
If the invariant holds before a step and my update preserves it, it holds for all steps.
So the final output is valid.

## 6) Complexity (say this confidently)
- **Time:** `O(rows * cols)`.
- **Space:** `O(rows * cols)` worst-case recursion/queue.

## 7) Edge cases I would call out
- Empty/minimal input.
- Duplicate values / tie-breaking.
- No valid answer path (return sentinel value).
- Very large input where brute force would timeout.

## 8) Follow-up extensions interviewers ask
- Can we reduce memory further?
- Can we return reconstruction/path, not just boolean/count?
- Can this work in streaming/online settings?
- How would we unit-test quickly?

## 9) 30-second closing summary
**Candidate:** I start from a simple baseline, then optimize with the right data structure and invariant.
This gives clean correctness reasoning, handles edge cases, and meets interview-level performance targets.
