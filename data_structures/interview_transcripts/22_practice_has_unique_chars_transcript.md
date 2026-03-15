# Interview Transcript: Has Unique Characters

## Problem in plain English
**Interviewer:** Explain this question quickly.

**Candidate:** We need to solve **Has Unique Characters**. Best interview approach: Track seen characters in set; duplicate seen => false immediately.

## Clarifying questions
1. Are numbers/strings unique or can duplicates appear?
2. Do we return indices, values, count, or boolean?
3. What to return when no answer exists?

## Brute-force baseline
- Try every pair/subarray/combination directly.
- Correct but too slow for bigger inputs.

## Optimized approach I would present
- Pick the right helper structure (hash map/set, pointers, prefix sums).
- Update it once per element.
- Return answer as soon as condition is satisfied.

## Correctness intuition
The maintained state (seen values / running best / prefix counts) always contains exactly the information needed for the current position, so each step is locally correct and the final result is globally correct.

## Complexity
- **Time:** `O(n)`
- **Space:** `O(k)`

## Edge cases
- Empty input or size 1.
- All duplicates / all negatives / no valid solution.
- Large input performance.

## Closing statement
**Candidate:** I can code this in one pass with clean variable naming and then verify with 3-4 focused tests.
