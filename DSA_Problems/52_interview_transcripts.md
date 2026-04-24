## Basic Level

### 1. Reverse a String

**Problem**  
Given a string, return a new string with the characters in reverse order.

**Intuition (simple explanation)**  
To reverse a string, we just want to read it from the last character back to the first. In Python, slicing lets us jump through a string in steps. If we use a step of `-1`, Python starts at the end and moves backwards, giving us a reversed copy.

**Step-by-step logic**

1. Take the input string, say `s = "hello"`.
2. Use slicing: `s[::-1]`.
   - The first `:` means "from start to end".
   - The second `:` with `-1` means "step backwards one character at a time".
3. The result is a new string `"olleh"`.
4. Return this new reversed string.

**Time Complexity**: O(n) — we touch each character once to build the reversed string.  
**Space Complexity**: O(n) — we create a new string of the same size.

**Why we can’t do it in-place in Python**  
Python strings cannot be changed after they are created (they are immutable). So, we must create a new string instead of modifying the original.

**Edge cases**

- **Empty string**: `""` → result is also `""`.
- **Single character**: `"a"` → result is still `"a"`.

---

### 2. Check Palindrome

**Problem**  
Check if a given string reads the same forwards and backwards (a palindrome).

**Intuition**  
A palindrome is a word or phrase that looks the same when reversed, like `"madam"` or `"racecar"`. So the simplest way is: reverse the string and compare it to the original. If they are equal, it's a palindrome.

**Step-by-step logic**

1. Normalize the string (optional but common):
   - Convert to lowercase so `"Madam"` and `"madam"` are treated the same.
   - Optionally remove spaces if you want to handle phrases like `"nurses run"`.
2. Create a reversed version of the string using slicing: `s[::-1]`.
3. Compare original (normalized) string and reversed string.
4. If they match, return `True`; otherwise, return `False`.

**Time Complexity**: O(n) — we scan the whole string to reverse and compare.  
**Space Complexity**: O(n) — for the reversed copy.

**Optimization**

- Normalize by:
  - Removing spaces: `s.replace(" ", "")`.
  - Converting to lowercase: `s.lower()`.

**Edge cases**

- **Mixed case letters**: `"Madam"` should still be palindrome if we ignore case.
- **Strings with spaces**: `"nurses run"` can be considered palindrome if we ignore spaces.
- **Empty string**: Usually treated as a palindrome (nothing to contradict the rule).

---

### 3. Find Largest Element in a List

**Problem**  
Given a list of numbers, find the largest (maximum) value.

**Intuition**  
Think of scanning the list from left to right while remembering the biggest number seen so far. Each time we see a number bigger than our current “largest”, we update it.

**Step-by-step logic**

1. If the list is empty, decide how to handle it (return `None` or raise an error).
2. Set `largest` to the first element.
3. Loop through the rest of the list:
   - For each number `x`, if `x > largest`, then set `largest = x`.
4. After the loop finishes, `largest` holds the maximum number.
5. Return `largest`.

**Time Complexity**: O(n) — we look at each element once.  
**Space Complexity**: O(1) — we use just a few variables.

**Optimization**

- Use Python’s built-in `max()` function. It is written in C and is already very efficient.

**Edge cases**

- **Empty list**: No maximum; handle carefully.
- **List with negative numbers**: The logic still works; the maximum could be negative.
- **Single element list**: That single element is the largest.

---

### 4. Count Vowels in a String

**Problem**  
Count how many vowels (`a, e, i, o, u`) appear in a string.

**Intuition**  
We go through each character and see if it is a vowel. If it is, we increase a counter.

**Step-by-step logic**

1. Define a set of vowels, for example: `vowels = {"a", "e", "i", "o", "u"}`.
2. Initialize a counter to 0.
3. Convert string to lowercase so we don’t miss uppercase vowels.
4. For each character in the string:
   - If the character is in `vowels`, increase the counter.
5. Return the counter at the end.

**Time Complexity**: O(n) — each character is checked once.  
**Space Complexity**: O(1) — the vowel set has fixed size.

**Why use a set?**

- Checking `char in vowels_set` is O(1) on average.
- This is much faster than checking in a long string repeatedly.

**Edge cases**

- **Uppercase characters**: `"AEIOU"` should be handled by converting to lowercase.
- **Empty string**: Count is 0.
- **Strings without vowels**: Also result in 0.

---

### 5. Swap Two Variables

**Problem**  
Given two variables `a` and `b`, swap their values.

**Intuition**  
In many languages, you need a temporary third variable to hold one value while you swap. Python supports tuple unpacking, which lets you swap in one line without a temporary variable.

**Step-by-step logic**

1. Suppose `a = 5` and `b = 10`.
2. Do: `a, b = b, a`.
   - On the right side, Python creates a tuple `(b, a)`.
   - On the left side, it unpacks that tuple into `a` and `b`.
3. After this, `a` becomes `10` and `b` becomes `5`.

**Time Complexity**: O(1).  
**Space Complexity**: O(1) — the tuple is handled internally and very efficiently.

**Optimization**

- Tuple unpacking in Python is already the standard and cleanest way.

**Edge cases**

- **Same values**: If `a` and `b` are the same, swapping has no visible effect, but still works.
- **Large numbers**: Works the same, size of the numbers doesn’t matter.

---

### 6. Factorial of a Number

**Problem**  
Compute the factorial of `n`, written as `n!`, which is `1 * 2 * 3 * ... * n`.

**Intuition**  
Factorial is just repeated multiplication from 1 up to `n`. We keep a running result and multiply it by each number.

**Step-by-step logic**

1. If `n` is 0, return 0! = 1 by definition.
2. Initialize `result = 1`.
3. Loop from 1 to `n`:
   - For each `i`, do `result *= i`.
4. After the loop, `result` holds `n!`.
5. Return `result`.

**Time Complexity**: O(n) — we do one multiplication per number.  
**Space Complexity**: O(1) — we only store the current result and loop variable.

**Optimization**

- Use `math.factorial(n)` from Python’s standard library; it is faster and handles big numbers more efficiently.

**Edge cases**

- **n = 0**: Return 1.
- **Negative numbers**: Factorial is not defined for negative integers in the usual sense; typically raise an error.
- **Very large n**: Can cause very large results; may be slow or use a lot of memory.

---

### 7. Fibonacci Series

**Problem**  
Generate the first `n` numbers of the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...

**Intuition**  
Each number (from the third onward) is the sum of the previous two. We can just keep track of the last two numbers and keep adding.

**Step-by-step logic**

1. If `n` is 0, return an empty list.
2. If `n` is 1, return `[0]`.
3. Start with `a = 0`, `b = 1` and a list `[0, 1]`.
4. For the next `n-2` steps:
   - Compute `c = a + b`.
   - Append `c` to the list.
   - Update `a = b`, `b = c`.
5. Return the list of Fibonacci numbers.

**Time Complexity**: O(n) — we generate each term once.  
**Space Complexity**: O(n) — we store all terms in a list.

**Optimization**

- If you only need the nth Fibonacci number, you can just keep the last two numbers and not store the entire sequence (space O(1)).

**Edge cases**

- **n = 0**: No numbers to return.
- **n = 1**: Return only `[0]`.

---

### 8. Check Prime Number

**Problem**  
Determine if a number `n` is prime (has exactly two positive divisors: 1 and itself).

**Intuition**  
To check if `n` is prime, we see if it has any divisor other than 1 and itself. Instead of checking all numbers up to `n`, we only need to check up to √n because if `n = a * b` and both `a` and `b` were greater than √n, their product would be greater than `n`.

**Step-by-step logic**

1. If `n < 2`, it is not prime.
2. Loop `i` from 2 to `int(sqrt(n))`:
   - If `n % i == 0`, then `n` has a divisor and is not prime.
3. If no divisor is found, `n` is prime.

**Time Complexity**: O(√n).  
**Space Complexity**: O(1).

**Optimization**

- As soon as you find a divisor, you can stop and return `False` (early exit).

**Edge cases**

- **n < 2**: Not prime.
- **Very large numbers**: The algorithm still works but may be slower; more advanced methods exist for very large inputs.

---

### 9. Remove Duplicates from a List

**Problem**  
Given a list, remove duplicate elements so that each value appears only once.

**Intuition**  
A set in Python automatically stores only unique elements. Converting a list to a set removes duplicates instantly.

**Step-by-step logic**

1. Take the list, for example `[1, 2, 2, 3]`.
2. Convert it to a set: `unique_set = set(lst)` → `{1, 2, 3}`.
3. If you don’t care about order, you can convert this set back to a list.
4. If order matters, you can:
   - Create an empty list and empty set.
   - Loop through the original list and add each element to the result list only the first time you see it.

**Time Complexity**: O(n) — inserting each element into a set is O(1) average.  
**Space Complexity**: O(n) — the set needs space for distinct elements.

**Optimization**

- If order matters, use an ordered structure like a dictionary (in Python 3.7+, `dict` preserves insertion order) or use a loop with a set of “seen” elements.

**Edge cases**

- **Empty list**: Return an empty list.
- **List with all duplicates**: Result will have one element.
- **List with all unique elements**: Output should be the same as input.

---

### 10. Sort a List

**Problem**  
Given a list of elements (usually numbers), return them sorted (typically in ascending order).

**Intuition**  
Sorting arranges elements from smallest to largest (or vice versa). Python’s built-in sorting is highly optimized and uses an algorithm called Timsort, which is very fast for real-world data.

**Step-by-step logic**

1. To get a new sorted list: `sorted_list = sorted(lst)`.
2. To sort the list in-place (modify the original list): `lst.sort()`.
3. Optionally, pass arguments like `reverse=True` or a custom `key` function.

**Time Complexity**: O(n log n).  
**Space Complexity**: O(n) — for the `sorted()` function; in-place sort uses extra space efficiently under the hood.

**Optimization**

- Using the built-in sort is better than writing your own, as it’s highly optimized.

**Edge cases**

- **Already sorted list**: Still works; Timsort is efficient on partially sorted data.
- **List with duplicates**: All occurrences stay; sort is stable (relative order of equal elements is preserved).
- **Negative numbers**: Sorted correctly along with positive numbers.

---

## Intermediate Level

### 11. Count Frequency of Elements

**Problem**  
Given a list, count how many times each element appears.

**Intuition**  
We want a mapping from element → count. A dictionary is a natural fit: keys are elements, values are counts. We update the count as we scan.

**Step-by-step logic**

1. Create an empty dictionary, e.g. `freq = {}`.
2. Loop over each element `x` in the list:
   - If `x` is not in `freq`, set `freq[x] = 1`.
   - Otherwise, increment `freq[x] += 1`.
3. Return the `freq` dictionary.

**Time Complexity**: O(n).  
**Space Complexity**: O(n) — in the worst case, all elements are unique.

**Optimization**

- Use `collections.Counter` which does this counting efficiently and with clean syntax: `Counter(lst)`.

**Edge cases**

- **Empty list**: Return an empty dictionary.
- **All elements identical**: Dictionary will have one key with a high count.

---

### 12. Second Largest Element

**Problem**  
Find the second largest distinct value in a list.

**Intuition**  
We can track two values while scanning: the largest and the second largest. As we see new numbers, we update them appropriately.

**Step-by-step logic**

1. If the list has fewer than 2 distinct elements, decide how to handle (error or `None`).
2. Initialize `largest` and `second_largest` (often with `None` or very small numbers).
3. Loop through each element `x`:
   - If `largest` is `None` or `x > largest`:
     - Set `second_largest = largest`.
     - Set `largest = x`.
   - Else if `x` is less than `largest` but greater than `second_largest`:
     - Update `second_largest = x`.
4. After the loop, `second_largest` holds the answer.

**Time Complexity**: O(n).  
**Space Complexity**: O(1).

**Optimization**

- Avoid sorting (which is O(n log n)) just to find the second largest.

**Edge cases**

- **Less than two elements**: No second largest; handle carefully.
- **All elements same**: No distinct second largest; may return `None` or raise an error.

---

### 13. Merge Two Lists

**Problem**  
Combine two lists into one.

**Intuition**  
Merging here just means putting the elements of one list after the elements of another.

**Step-by-step logic**

1. Given lists `a` and `b`, you can merge them as:
   - `merged = a + b`.
2. Or use `extend` to add elements of `b` into `a`:
   - `a.extend(b)` modifies `a` directly.
3. Return the merged list.

**Time Complexity**: O(n + m), where `n` and `m` are lengths of the two lists.  
**Space Complexity**: O(n + m) for the new list.

**Optimization**

- List concatenation with `+` or `extend` is already efficient in Python.

**Edge cases**

- **One list empty**: Result is just the other list.
- **Both lists empty**: Result is empty.

---

### 14. Find Length Without `len()`

**Problem**  
Find the length of a list without using the built-in `len()` function.

**Intuition**  
We can count how many elements are in the list by walking through it and incrementing a counter.

**Step-by-step logic**

1. Initialize `count = 0`.
2. Loop over each element of the list:
   - For each element, do `count += 1`.
3. After the loop ends, `count` is the length.
4. Return `count`.

**Time Complexity**: O(n).  
**Space Complexity**: O(1).

**Edge cases**

- **Empty list**: The loop doesn’t run; `count` stays 0.

---

### 15. Sum of Digits

**Problem**  
Given an integer, compute the sum of its digits.

**Intuition**  
We can peel off the last digit using modulo 10, add it to a total, and then remove that digit by dividing by 10.

**Step-by-step logic**

1. Take the absolute value of the number if you want to ignore the sign.
2. Initialize `total = 0`.
3. While the number is greater than 0:
   - Get last digit: `digit = n % 10`.
   - Add to total: `total += digit`.
   - Remove last digit: `n = n // 10`.
4. Return `total`.

**Time Complexity**: O(d), where `d` is the number of digits.  
**Space Complexity**: O(1).

**Edge cases**

- **Negative numbers**: Handle by using `abs(n)` if sign doesn’t matter.
- **Zero**: Sum of digits is 0.

---

### 16. Check Anagram

**Problem**  
Check if two strings are anagrams (they contain the same characters with the same frequencies, in any order).

**Intuition**  
If two words use the same letters the same number of times, then after sorting their characters, they will look identical. Alternatively, their character frequency maps will match.

**Step-by-step logic (sorting approach)**

1. Normalize both strings:
   - Convert to lowercase.
   - Remove spaces if you want to ignore them.
2. Sort the characters of each string: `sorted(s1)` and `sorted(s2)`.
3. If these sorted lists are equal, they are anagrams.

**Time Complexity**: O(n log n) — sorting dominates.  
**Space Complexity**: O(n).

**Optimization (counting approach)**

- Count characters using a dictionary or `Counter` for both strings, and compare these dictionaries.
- This makes the time complexity O(n).

**Edge cases**

- **Case differences**: `"Listen"` and `"silent"` should still match if case-insensitive.
- **Spaces**: `"a gentleman"` vs `"elegant man"` may be considered anagrams if you remove spaces.

---

### 17. Missing Number in Array

**Problem**  
Given an array of numbers from 1 to `n` with exactly one number missing, find the missing number.

**Intuition**  
We know what the total sum **should** be if no number is missing: `n(n+1)/2`. If we subtract the sum of the given array from this expected sum, the difference is the missing number.

**Step-by-step logic**

1. Let `n` be the largest number in the full range.
2. Compute expected sum: `expected = n * (n + 1) // 2`.
3. Compute actual sum of array: `actual = sum(arr)`.
4. The missing number is `expected - actual`.
5. Return this value.

**Time Complexity**: O(n).  
**Space Complexity**: O(1).

**Optimization**

- Use XOR method to avoid potential overflow in languages where integer overflow is an issue (less of a problem in Python).

**Edge cases**

- **Empty array**: Technically there’s more than one missing number; needs special handling.
- **Missing first number** or **missing last number**: The formula still works.

---

### 18. Common Elements Between Lists

**Problem**  
Find elements that appear in both lists.

**Intuition**  
Sets allow fast membership checks. We convert lists to sets and then use set intersection.

**Step-by-step logic**

1. Convert both lists to sets: `set1 = set(a)`, `set2 = set(b)`.
2. Find intersection: `common = set1 & set2` or `set1.intersection(set2)`.
3. Convert back to a list if needed.
4. Return this list of common elements.

**Time Complexity**: O(n + m).  
**Space Complexity**: O(n + m) for the sets (worst case).

**Edge cases**

- **No common elements**: Intersection is an empty set.
- **Duplicates in original lists**: Sets remove duplicates, so each common element appears once.

---

### 19. First Non-Repeating Character

**Problem**  
Given a string, find the first character that appears only once.

**Intuition**  
We need to know how many times each character appears, and then we want the first one with a count of 1 in the original order.

**Step-by-step logic**

1. First pass:
   - Create a frequency dictionary for all characters in the string.
2. Second pass:
   - Loop through the string again in order.
   - For each character, check if its frequency is 1.
   - The first one that satisfies this is the answer.
3. If none found, there is no non-repeating character.

**Time Complexity**: O(n).  
**Space Complexity**: O(n) for the frequency dictionary.

**Edge cases**

- **All characters repeating**: No result; often return something like `None` or a special symbol.
- **Empty string**: No characters to examine.

---

### 20. Flatten Nested List

**Problem**  
Given a list that may contain other lists inside it (nested), return a flat list with all values.

**Intuition**  
When you see an element:
- If it’s a normal value, add it to the result.
- If it’s a list, you need to go inside that list and flatten it too. This is a natural fit for recursion.

**Step-by-step logic**

1. Create an empty result list.
2. For each element `x` in the original list:
   - If `x` is not a list, append it to the result.
   - If `x` is a list, recursively flatten `x` and extend the result with that.
3. Return the result list.

**Time Complexity**: O(n), where `n` is the total number of elements across all levels.  
**Space Complexity**: O(n) for the result, plus recursion stack depending on depth.

**Edge cases**

- **Deeply nested lists**: Recursion depth can become large.
- **Empty lists**: Should just be skipped or contribute nothing.

---

### 21. Find Duplicates in List

**Problem**  
Identify which elements appear more than once in a list.

**Intuition**  
We use a set to remember what we have seen. If we see an element that is already in the set, it’s a duplicate.

**Step-by-step logic**

1. Create an empty set `seen` and an empty set `duplicates`.
2. Loop through each element `x`:
   - If `x` not in `seen`, add it to `seen`.
   - Else, add `x` to `duplicates`.
3. At the end, `duplicates` contains all values that appeared at least twice.
4. Convert `duplicates` to a list and return if needed.

**Time Complexity**: O(n).  
**Space Complexity**: O(n) in the worst case.

**Edge cases**

- **No duplicates**: `duplicates` remains empty.
- **All elements identical**: That single value will be in `duplicates`.
- **Empty list**: No duplicates.

---

### 22. Reverse Words in a Sentence

**Problem**  
Given a sentence (string), reverse the order of the words while keeping each word itself intact.

**Intuition**  
Words are separated by spaces. If we split the sentence by spaces, we get a list of words. We can reverse this list and join it back with spaces.

**Step-by-step logic**

1. Split the sentence: `words = s.split()` (this handles multiple spaces nicely).
2. Reverse the list: `words = words[::-1]`.
3. Join them back: `reversed_sentence = " ".join(words)`.
4. Return `reversed_sentence`.

**Time Complexity**: O(n).  
**Space Complexity**: O(n) — for the list of words and the output string.

**Optimization**

- Python’s `split()` and `join()` are already optimized.

**Edge cases**

- **Multiple spaces**: `split()` collapses consecutive spaces.
- **Single word**: Reversing has no effect.
- **Empty string**: Returns empty string.

---

### 23. Check Armstrong Number

**Problem**  
An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits (e.g., 153 = 1³ + 5³ + 3³). Check if a given number is Armstrong.

**Intuition**  
We break the number into digits, count how many digits there are, raise each digit to that power, and sum them. If the sum matches the original number, it’s an Armstrong number.

**Step-by-step logic**

1. Convert the number to a string to easily access digits, or repeatedly use `% 10` and `// 10`.
2. Let `d` be the number of digits.
3. For each digit:
   - Raise it to the power `d` and add it to a running sum.
4. Compare the sum with the original number.
5. If equal, return `True`; otherwise, `False`.

**Time Complexity**: O(d) — one pass over the digits.  
**Space Complexity**: O(1).

**Edge cases**

- **Single digit numbers**: All single digits (0–9) are Armstrong numbers.
- **Large numbers**: More digits lead to more computation, but logic is the same.

---

### 24. Find GCD of Two Numbers

**Problem**  
Find the greatest common divisor (GCD) of two numbers.

**Intuition**  
The Euclidean algorithm uses the fact that `gcd(a, b) = gcd(b, a % b)`. We keep replacing the pair with `(b, a % b)` until the remainder becomes 0. The non-zero number is the GCD.

**Step-by-step logic**

1. Let the numbers be `a` and `b`.
2. While `b` is not 0:
   - Set `a, b = b, a % b`.
3. When `b` becomes 0, `a` is the GCD.
4. Return `a`.

**Time Complexity**: O(log(min(a, b))).  
**Space Complexity**: O(1).

**Optimization**

- This algorithm is already very efficient.

**Edge cases**

- **One number is zero**: `gcd(a, 0) = |a|`.
- **Both numbers equal**: GCD is that number.

---

### 25. Check Balanced Parentheses

**Problem**  
Given a string of brackets (like `()[]{}`), determine if it is properly balanced.

**Intuition**  
A stack is ideal:  
- Push opening brackets.  
- When you see a closing bracket, check that it matches the top of the stack. If not, it's unbalanced.

**Step-by-step logic**

1. Create an empty stack.
2. Create a mapping of closing to opening brackets, e.g. `pairs = {')': '(', ']': '[', '}': '{'}`.
3. For each character in the string:
   - If it is an opening bracket, push it onto the stack.
   - If it is a closing bracket:
     - If stack is empty, it’s unbalanced.
     - Pop from stack and check if it matches the corresponding opening bracket.
4. At the end, if stack is empty, it is balanced; otherwise not.

**Time Complexity**: O(n).  
**Space Complexity**: O(n) in the worst case.

**Optimization**

- You can fail early as soon as a mismatch is found.

**Edge cases**

- **Empty string**: Typically considered balanced.
- **Only opening brackets**: Stack not empty at end → unbalanced.
- **Incorrect nesting**: e.g. `([)]` is invalid.

---

### 26. Implement Stack

**Problem**  
Implement a basic stack data structure with push and pop.

**Intuition**  
A stack is "Last In, First Out". A Python list already works like a stack when using `append()` and `pop()` at the end.

**Step-by-step logic**

1. Represent the stack as a list: `stack = []`.
2. **Push** operation:
   - `stack.append(x)` to put an item on top.
3. **Pop** operation:
   - `stack.pop()` to remove and return the top item.
4. Optionally, provide methods like `peek()` to look at the top element without removing it.

**Time Complexity**

- **Push**: O(1).
- **Pop**: O(1).

**Space Complexity**: O(n) — stores `n` elements.

**Edge cases**

- **Popping from empty stack**: Should handle gracefully (return `None` or raise an error).

---

### 27. Implement Queue

**Problem**  
Implement a basic queue data structure with enqueue and dequeue operations.

**Intuition**  
A queue is "First In, First Out". If we use a list and remove from the front, it becomes slow. Instead, `collections.deque` is designed for fast appends and pops from both ends.

**Step-by-step logic**

1. Use `collections.deque` to represent the queue: `from collections import deque; q = deque()`.
2. **Enqueue**:
   - `q.append(x)` to add to the rear.
3. **Dequeue**:
   - `q.popleft()` to remove from the front.
4. Optionally, check size or peek at the front element.

**Time Complexity** (with `deque`)

- **Enqueue**: O(1).
- **Dequeue**: O(1).

**Space Complexity**: O(n).

**Optimization**

- Avoid using a plain list for dequeue from front (`pop(0)`), which is O(n).

**Edge cases**

- **Dequeue from empty queue**: Should be handled gracefully (return `None` or raise an error).

---

### 28. Intersection of Two Arrays

**Problem**  
Find the common unique elements between two arrays.

**Intuition**  
This is similar to “common elements between lists”. Sets give us a simple, fast way to find intersection.

**Step-by-step logic**

1. Convert arrays to sets: `set1 = set(a)`, `set2 = set(b)`.
2. Intersection: `result = set1 & set2`.
3. Convert to list if needed and return.

**Time Complexity**: O(n + m).  
**Space Complexity**: O(n + m).

**Optimization**

- Sets provide O(1) average membership checks, so intersection is efficient.

**Edge cases**

- **No intersection**: Result is empty.
- **Arrays with duplicates**: Each element appears at most once in the intersection.

---

### 29. Group Anagrams

**Problem**  
Given a list of words, group together words that are anagrams of each other.

**Intuition**  
Words that are anagrams will have the same characters in the same counts. A simple way is to sort each word’s letters; the sorted form becomes the key for grouping.

**Step-by-step logic**

1. Create an empty dictionary `groups = {}`.
2. For each word in the list:
   - Sort its characters: `key = ''.join(sorted(word))`.
   - Use this `key` as a dictionary key, and append the original word to `groups[key]`.
3. At the end, the values of `groups` are lists of anagrams.
4. Return these groups.

**Time Complexity**: O(n * k log k), where `n` is number of words and `k` is maximum word length.  
**Space Complexity**: O(n).

**Optimization**

- Instead of sorting, you can use a character frequency tuple as the key, which gives O(n * k) time.

**Edge cases**

- **Empty string**: Can appear as its own group.
- **Words of different lengths**: Can’t be anagrams if lengths differ.

---

### 30. Rotate List by K Positions

**Problem**  
Rotate a list to the right by `k` positions.

**Intuition**  
Rotating right by `k` positions means taking the last `k` elements and moving them to the front.

**Step-by-step logic**

1. Let `n` be the length of the list.
2. Handle `k` bigger than `n` by doing `k = k % n`.
3. Split the list:
   - Last `k` elements: `lst[-k:]`.
   - First `n - k` elements: `lst[:-k]`.
4. New list is `lst[-k:] + lst[:-k]`.
5. Return this new list.

**Time Complexity**: O(n) — slicing and concatenation touch all elements.  
**Space Complexity**: O(n) — for the new rotated list.

**Optimization**

- Using modulo `k % n` avoids unnecessary full rotations.

**Edge cases**

- **k = 0**: List remains unchanged.
- **k > length**: Handled by modulo.
- **Empty list**: Return empty list.

---

### 31. Find Pair with Given Sum

**Problem**  
Given an array and a target sum, find if there exists a pair of numbers that adds up to the target.

**Intuition**  
For each number `x`, we need another number `target - x`. We can store seen numbers in a set and check if the needed complement is already present.

**Step-by-step logic**

1. Create an empty set `seen`.
2. For each number `x` in the array:
   - Compute `needed = target - x`.
   - If `needed` is in `seen`, we found a pair.
   - Otherwise, add `x` to `seen`.
3. If you finish the loop without finding a pair, no such pair exists.

**Time Complexity**: O(n).  
**Space Complexity**: O(n) for the set.

**Optimization**

- This avoids a nested loop (which would be O(n²)).

**Edge cases**

- **No pair exists**: Return something like `False` or `None`.
- **Multiple valid pairs**: Often returning any one pair is enough.

---

### 32. Count Words in a File

**Problem**  
Count how many words are in a text file.

**Intuition**  
We read the file as text, split the content into words by whitespace, and then count how many items we got.

**Step-by-step logic**

1. Open the file in read mode.
2. Read the entire content (for small files): `text = f.read()`.
3. Split into words: `words = text.split()`.
4. The word count is `len(words)`.
5. Return this count.

**Time Complexity**: O(n), where `n` is number of characters.  
**Space Complexity**: O(n) — storing all text and words.

**Optimization**

- For large files, read line by line:
  - For each line, do `line.split()` and increment a counter instead of storing everything at once.

**Edge cases**

- **Empty file**: Word count is 0.
- **Special characters**: `split()` by default splits on any whitespace; punctuation is attached to words unless you remove it separately.

---

### 33. Binary Search

**Problem**  
Find a target value in a sorted array using binary search.

**Intuition**  
Rather than checking every element, we repeatedly cut the search range in half. We compare the target with the middle element to decide which half to keep.

**Step-by-step logic**

1. Set `left = 0`, `right = n - 1`.
2. While `left <= right`:
   - Compute `mid = (left + right) // 2`.
   - If `arr[mid] == target`, return `mid`.
   - If `arr[mid] < target`, move the left boundary: `left = mid + 1`.
   - Else, move the right boundary: `right = mid - 1`.
3. If the loop ends without finding the target, it is not in the array.

**Time Complexity**: O(log n).  
**Space Complexity**: O(1) for iterative version.

**Edge cases**

- **Target not present**: Return some indication like `-1`.
- **Empty array**: Immediately return not found.

---

## Advanced Level

### 34. Maximum Subarray Sum (Kadane’s Algorithm)

**Problem**  
Given an array (possibly with negative numbers), find the contiguous subarray with the maximum possible sum.

**Intuition**  
As we go through the array, we keep track of a current running sum. If this running sum becomes worse than just starting fresh at the current element, we reset it. This avoids checking all subarrays.

**Step-by-step logic**

1. Initialize two variables:
   - `current_sum = arr[0]`
   - `max_sum = arr[0]`
2. Loop from the second element onward:
   - For each element `x`, update:
     - `current_sum = max(x, current_sum + x)`
   - Then update `max_sum = max(max_sum, current_sum)`.
3. At the end, `max_sum` is the maximum subarray sum.
4. Return `max_sum`.

**Time Complexity**: O(n).  
**Space Complexity**: O(1).

**Optimization**

- Kadane’s algorithm is already optimal for this problem.

**Edge cases**

- **All negative numbers**: The answer is the least negative (largest) number.
- **Single element**: That element is the maximum sum.

---

### 35. Longest Substring Without Repeating Characters

**Problem**  
Given a string, find the length of the longest substring that has all unique (non-repeated) characters.

**Intuition**  
We use a sliding window: expand the window by moving the right pointer; if we see a repeated character, move the left pointer until the window has only unique characters again.

**Step-by-step logic**

1. Keep a set to store characters in the current window.
2. Use two pointers: `left = 0`, `right = 0`.
3. While `right < len(s)`:
   - If `s[right]` is not in the set:
     - Add it to the set.
     - Update maximum length.
     - Move `right` forward.
   - Else:
     - Remove `s[left]` from the set and move `left` forward.
4. At the end, the recorded maximum length is the answer.

**Time Complexity**: O(n) — each character is added and removed at most once.  
**Space Complexity**: O(n) — at worst, all characters in the window are unique.

**Optimization**

- Using a dictionary with character positions can let you jump `left` more quickly.

**Edge cases**

- **All characters same**: Longest length is 1.
- **Empty string**: Length is 0.

---

### 36. LRU Cache

**Problem**  
Design a cache that removes the **Least Recently Used** item when it reaches capacity.

**Intuition**  
We need two things:
- Fast lookup by key.
- Ability to know which key was used least recently.  
A combination of a hash map and a doubly linked list (or structures like `OrderedDict`) gives both.

**Step-by-step logic (conceptual)**

1. Maintain:
   - A dictionary mapping keys to nodes.
   - A doubly linked list that keeps nodes in order of usage (most recent at one end).
2. **Get(key)**:
   - If key not present, return a miss indicator (e.g. `-1`).
   - Move the node corresponding to key to the “most recently used” position.
   - Return its value.
3. **Put(key, value)**:
   - If key exists, update its value and move node to the MRU position.
   - If key does not exist:
     - If at full capacity, remove the least recently used node from both the list and dictionary.
     - Insert the new key as the most recently used.
4. This keeps get/put operations O(1).

**Time Complexity**

- **Get**: O(1).
- **Put**: O(1).

**Space Complexity**: O(capacity).

**Edge cases**

- **Cache full**: Need to evict correct item.
- **Accessing missing key**: Return some defined value, typically `-1` or `None`.

---

### 37. Detect Cycle in Linked List

**Problem**  
Check if a singly linked list has a cycle (the next pointers eventually loop back instead of ending in `None`).

**Intuition**  
Use Floyd’s Tortoise and Hare algorithm:
- One pointer moves one step at a time (slow).
- Another moves two steps at a time (fast).
- If there is a cycle, they will eventually meet inside the cycle.

**Step-by-step logic**

1. Initialize `slow` and `fast` pointers to the head.
2. While `fast` and `fast.next` are not `None`:
   - Move `slow` by one step.
   - Move `fast` by two steps.
   - If `slow == fast`, a cycle exists; return `True`.
3. If the loop ends (fast reaches `None`), there is no cycle; return `False`.

**Time Complexity**: O(n).  
**Space Complexity**: O(1).

**Edge cases**

- **Single node**: If it points to itself, that’s a cycle.
- **No cycle**: Pointers eventually hit `None`.

---

### 38. Merge Overlapping Intervals

**Problem**  
Given a list of intervals (like `[start, end]`), merge all overlapping intervals.

**Intuition**  
If we sort intervals by their start time, overlapping intervals will appear next to each other. We can then merge them by comparing the current interval with the last merged one.

**Step-by-step logic**

1. Sort the intervals based on start value.
2. Initialize a list `merged` with the first interval.
3. For each interval `curr` in the sorted list:
   - Let `last` be the last interval in `merged`.
   - If `curr.start` is less than or equal to `last.end`, they overlap:
     - Merge by setting `last.end = max(last.end, curr.end)`.
   - Otherwise, they don’t overlap:
     - Append `curr` to `merged`.
4. Return `merged`.

**Time Complexity**: O(n log n) — due to sorting.  
**Space Complexity**: O(n) — for the `merged` list.

**Edge cases**

- **No overlaps**: All intervals stay as they are.
- **Fully overlapping intervals**: Many intervals can merge into one bigger interval.

---

### 39. Top K Frequent Elements

**Problem**  
Given a list of elements, return the `k` elements that occur most frequently.

**Intuition**  
First, count how many times each element appears (using a dictionary). Then, pick the `k` elements with highest counts. A heap is useful for efficiently getting the top `k`.

**Step-by-step logic**

1. Count frequencies with a dictionary or `Counter`.
2. Use a min-heap (size `k`):
   - Push elements into the heap based on frequency.
   - If heap size exceeds `k`, pop the smallest frequency element.
3. At the end, the heap contains the `k` most frequent elements.
4. Extract and return them.

**Time Complexity**: O(n log k).  
**Space Complexity**: O(n) for the frequency map and O(k) for the heap.

**Optimization**

- Heap is better than sorting all elements when `k` is much smaller than the number of unique elements.

**Edge cases**

- **k larger than unique elements**: Then just return all unique elements.

---

### 40. Word Frequency in Large File

**Problem**  
Count how often each word appears in a very large file.

**Intuition**  
We cannot always load the whole file into memory at once. Instead, we process it line by line and update a running count.

**Step-by-step logic**

1. Initialize a dictionary or `Counter` for word frequencies.
2. Open the file and read it line by line.
3. For each line:
   - Split into words: `words = line.split()`.
   - For each word, update its count in the dictionary.
4. After processing all lines, return the frequency dictionary.

**Time Complexity**: O(n), where `n` is total number of characters/words processed.  
**Space Complexity**: O(unique words) — one entry per distinct word.

**Edge cases**

- **Very large files**: This approach is safe, as you never keep the full file in memory.
- **Case sensitivity**: Decide whether `"Word"` and `"word"` count as the same; you may convert to lowercase.

---

### 41. Multithreading vs Multiprocessing

**Concept**  
Describe the difference between multithreading and multiprocessing.

**Intuition**  

- **Multithreading**: Many threads run inside the same process and share memory. Good for tasks that wait a lot (I/O-bound), like network calls or file access.  
- **Multiprocessing**: Many independent processes run, each with its own memory space. Good for tasks that use a lot of CPU (CPU-bound), as they can truly run in parallel on multiple cores.

**Key points**

- **Shared memory**:
  - Threads share memory; easier to share data but can cause race conditions if not careful.
  - Processes don’t share memory by default; they are safer but need special ways to communicate (like queues or pipes).
- **Use cases**:
  - Multithreading for I/O-bound tasks.
  - Multiprocessing for CPU-heavy tasks.

**Edge cases**

- **Shared memory issues**: With threads, bugs can appear if two threads change the same data at the same time without locks.
- **Race conditions**: You must handle synchronization carefully in multithreading.

---

### 42. Decorator Implementation

**Problem**  
Explain and implement a decorator, which wraps a function to add extra behavior.

**Intuition**  
A decorator is a function that takes another function as input, creates a new function that does something extra before or after calling the original, and returns this new function.

**Step-by-step logic (conceptually)**

1. Define a function `decorator` that takes a function `f` as an argument.
2. Inside `decorator`, define an inner function `wrapper` that:
   - Does something before calling `f`.
   - Calls `f(*args, **kwargs)`.
   - Does something after if needed.
   - Returns the result.
3. Return `wrapper` from `decorator`.
4. Use `@decorator` above the function you want to wrap.

**Time Complexity**: Depends entirely on the wrapped function.  
**Space Complexity**: O(1) extra.

**Edge cases**

- **Functions with arguments**: The `wrapper` should accept `*args, **kwargs` to pass any type of arguments.
- **Multiple decorators**: They are applied from bottom to top.

---

### 43. Context Manager

**Problem**  
Explain a context manager (like `with open(...) as f:`) and how it manages resources.

**Intuition**  
A context manager automatically takes care of setup and cleanup. For example, it opens a file and ensures it gets closed, even if an error happens.

**Step-by-step logic (conceptually)**

1. A context manager has two main parts:
   - `__enter__`: Code that runs when entering the `with` block (e.g., open file).
   - `__exit__`: Code that runs when leaving the block (e.g., close file, handle exceptions).
2. When you write:
   - `with something as resource:`
     - Python calls `something.__enter__()` to get `resource`.
     - Runs the block of code inside.
     - Then calls `something.__exit__()` when done or if an error occurs.

**Time Complexity**: O(1) overhead beyond the actual work.  
**Space Complexity**: O(1).

**Edge cases**

- **Exceptions inside block**: `__exit__` receives information about the exception and can decide whether to suppress it or let it propagate.

---

### 44. Generator vs Iterator

**Concept**  
Compare generator and iterator in Python.

**Intuition**  

- **Iterator**: Any object that defines `__iter__()` and `__next__()` methods. You call `next()` to get values one at a time.
- **Generator**: A simpler way to create iterators using a function with `yield`. It automatically provides `__iter__` and `__next__` for you.

**Key points**

- Generators produce values lazily, one at a time, and don’t store the whole sequence in memory.
- This saves memory for large sequences.

**Time Complexity**: O(n) to iterate over all values.  
**Space Complexity**: O(1) for generators — only current state is stored.

**Optimization**

- Use generators when dealing with large or infinite sequences to avoid high memory usage.

---

### 45. Custom Exception

**Problem**  
Explain how to create a custom exception type.

**Intuition**  
Sometimes built-in exceptions (like `ValueError`) don’t describe the exact problem in your application. You can define your own exception class that inherits from `Exception`.

**Step-by-step logic**

1. Define a new class:
   - `class MyCustomError(Exception):`
   - `    pass`  (or add your own `__init__`).
2. Raise it where appropriate:
   - `raise MyCustomError("Something went wrong")`.

**Time Complexity**: O(1) to raise/handle.  
**Space Complexity**: O(1) for each instance (small overhead).

---

### 46. Read Large CSV Efficiently

**Problem**  
Read and process a very large CSV file without exhausting memory.

**Intuition**  
Instead of loading the entire file into memory (e.g., all rows at once), we process it in smaller parts like line by line or in chunks.

**Step-by-step logic**

1. Open the file.
2. Use a CSV reader or iterate line by line.
3. For each line or chunk:
   - Parse it.
   - Process it (e.g., sum values, filter rows).
4. Do not store all rows unless really needed.

**Time Complexity**: O(n) — each row is processed once.  
**Space Complexity**: O(chunk size) — small and controlled.

---

### 47. Optimize Nested Loops

**Problem**  
Reduce the time complexity of code that uses nested loops (often O(n²)).

**Intuition**  
Nested loops often appear when we repeatedly search for something in a list. We can frequently replace the inner loop with a faster lookup structure like a set or dictionary.

**Step-by-step logic (conceptual)**

1. Identify what the inner loop is doing repeatedly (e.g., searching for an element).
2. Preprocess the data into a hash-based structure (set or dict).
3. Replace the inner loop with a direct lookup (O(1) average).
4. As a result, the outer loop remains, but the inner heavy work turns into a constant-time operation.

**Time Complexity**: Often improved from O(n²) to O(n).  
**Space Complexity**: Increases to O(n) for the extra data structure.

---

### 48. Singleton Pattern

**Problem**  
Ensure only one instance of a class is created in the entire application.

**Intuition**  
A singleton pattern controls object creation so that you always get the same instance. This is useful for things like configuration managers or logging systems.

**Step-by-step logic (conceptual in Python)**

1. You can:
   - Use a module as a singleton (since modules are imported once).
   - Or, inside a class, override `__new__` to return the existing instance if one exists, instead of creating a new one.
2. Store the single instance as a class-level attribute.

**Time Complexity**: O(1) to get the instance.  
**Space Complexity**: O(1) for the single instance.

**Edge cases**

- **Multiple threads**: Needs care to prevent two threads from creating separate instances at the same time.

---

### 49. Rate Limiter

**Problem**  
Limit how many requests a user can make in a certain time window.

**Intuition**  
One common method is the **token bucket** algorithm:
- Tokens are added to a bucket at a fixed rate.
- Each request uses one token.
- If the bucket is empty (no tokens), the request is not allowed or must wait.

**Step-by-step logic**

1. Maintain:
   - Current number of tokens.
   - Last time tokens were updated.
2. When a request comes in:
   - Add tokens to the bucket based on how much time has passed (up to a maximum capacity).
   - If there is at least one token:
     - Use one token and allow the request.
   - Otherwise:
     - Reject or delay the request.
3. This ensures the request rate stays within the allowed limit.

**Time Complexity**: O(1) per request.  
**Space Complexity**: O(1).

**Edge cases**

- **Burst traffic**: If bucket has saved tokens, short bursts may be allowed up to the bucket capacity.
- **Empty bucket**: New requests must wait or be rejected.

---

### 50. URL Shortener

**Problem**  
Design a service that takes a long URL and returns a short one that redirects to the original.

**Intuition**  
We assign each long URL a short, unique key (like `abc123`) and store a mapping from that key to the long URL in a database. The short URL basically encodes this key.

**Step-by-step logic**

1. **Shorten**:
   - When a long URL comes in, generate a unique ID (e.g., incrementing number or random).
   - Convert that ID to a short string using something like base62 (digits + letters).
   - Store the pair: `short_key -> long_url` in a database or dictionary.
   - Return `domain/short_key` as the short URL.
2. **Retrieve**:
   - When a user visits `domain/short_key`, look up `short_key` in storage.
   - Redirect to the original long URL.

**Time Complexity**

- **Shorten**: O(1) average — single insert.
- **Retrieve**: O(1) average — single lookup.

**Space Complexity**: O(n), where `n` is number of stored URLs.

**Edge cases**

- **Hash collision or key collision**: Must handle cases where the generated key already exists.
- **Invalid short code**: Return an error or 404-like response.

BASIC LEVEL
1. Reverse a String

Logic (How to explain)
“To reverse a string, the simplest Pythonic approach is slicing. It reads the string from the end to the beginning and returns a reversed copy.”

Time Complexity: O(n)
Space Complexity: O(n)

Optimization
In-place reversal isn't possible because strings are immutable in Python.

Edge Cases

Empty string

Single character string

2. Check Palindrome

Logic
“A palindrome reads the same forward and backward. So I simply compare the string with its reversed version. If they match, it's a palindrome.”

Time Complexity: O(n)
Space Complexity: O(n)

Optimization
Normalize input by removing spaces and converting to lowercase.

Edge Cases

Mixed case letters

Strings with spaces

Empty string

3. Find Largest Element in List

Logic
“I iterate through the list and keep track of the largest value seen so far. If I encounter a larger number, I update the value.”

Time Complexity: O(n)
Space Complexity: O(1)

Optimization
Use Python's built-in max() which is optimized in C.

Edge Cases

Empty list

List with negative numbers

Single element list

4. Count Vowels in String

Logic
“I traverse the string character by character and check if each character belongs to the vowel set. If yes, I increase the count.”

Time Complexity: O(n)
Space Complexity: O(1)

Optimization
Use a set for faster lookup instead of a string.

Edge Cases

Uppercase characters

Empty string

Strings without vowels

5. Swap Two Variables

Logic
“In Python we can swap two variables using tuple unpacking. Python assigns values simultaneously without needing a temporary variable.”

Time Complexity: O(1)
Space Complexity: O(1)

Optimization
Python’s tuple unpacking is already the most optimal.

Edge Cases

Same values

Large numbers

6. Factorial of a Number

Logic
“Factorial means multiplying all integers from 1 to n. I iterate from 1 to n and multiply each value with a running result.”

Time Complexity: O(n)
Space Complexity: O(1)

Optimization
Use built-in math.factorial() for faster computation.

Edge Cases

n = 0

Negative numbers

Large values causing overflow

7. Fibonacci Series

Logic
“The Fibonacci series starts with 0 and 1. Each next number is the sum of the previous two numbers. I generate numbers iteratively.”

Time Complexity: O(n)
Space Complexity: O(n)

Optimization
Use dynamic programming or store only last two numbers to reduce space to O(1).

Edge Cases

n = 0

n = 1

8. Check Prime Number

Logic
“A prime number has only two divisors. Instead of checking up to n, we check divisibility only up to the square root of n, which reduces unnecessary checks.”

Time Complexity: O(√n)
Space Complexity: O(1)

Optimization
Stop early once a divisor is found.

Edge Cases

n < 2

Large numbers

9. Remove Duplicates from List

Logic
“The simplest approach is converting the list into a set because sets automatically store unique values.”

Time Complexity: O(n)
Space Complexity: O(n)

Optimization
If order matters, use dictionary keys or ordered structures.

Edge Cases

Empty list

List with all duplicates

10. Sort a List

Logic
“Python uses Timsort which is an optimized hybrid sorting algorithm. Using sorted() returns a new sorted list.”

Time Complexity: O(n log n)
Space Complexity: O(n)

Optimization
Sorting is already optimized internally.

Edge Cases

Already sorted list

List with duplicates

Negative numbers

INTERMEDIATE LEVEL
11. Count Frequency of Elements

Logic
“I traverse the list and maintain a dictionary where the key is the element and the value is its count.”

Time Complexity: O(n)
Space Complexity: O(n)

Optimization
Use collections.Counter.

Edge Cases

Empty list

All elements identical

12. Second Largest Element

Logic
“I maintain two variables: largest and second largest. While iterating through the list I update them accordingly.”

Time Complexity: O(n)
Space Complexity: O(1)

Optimization
Avoid sorting because sorting would take O(n log n).

Edge Cases

Less than two elements

All elements same

13. Merge Two Lists

Logic
“Combining two lists simply means concatenating them.”

Time Complexity: O(n + m)
Space Complexity: O(n + m)

Optimization
Use list concatenation which is already efficient.

Edge Cases

One list empty

Both lists empty

14. Find Length Without len()

Logic
“I iterate through the list and increment a counter for each element.”

Time Complexity: O(n)
Space Complexity: O(1)

Edge Cases

Empty list

15. Sum of Digits

Logic
“I repeatedly extract the last digit using modulo operation and add it to the total.”

Time Complexity: O(d)
(d = number of digits)

Space Complexity: O(1)

Edge Cases

Negative numbers

Zero

16. Check Anagram

Logic
“Two strings are anagrams if they contain the same characters with the same frequency.”

Time Complexity: O(n log n) (sorting approach)

Space Complexity: O(n)

Optimization
Use character frequency counting for O(n).

Edge Cases

Case differences

Spaces

17. Missing Number in Array

Logic
“If numbers are from 1 to n, we calculate expected sum using formula n(n+1)/2 and subtract the actual sum.”

Time Complexity: O(n)
Space Complexity: O(1)

Optimization
Use XOR to avoid overflow.

Edge Cases

Empty array

Missing first number

Missing last number

18. Common Elements Between Lists

Logic
“Convert both lists to sets and find intersection.”

Time Complexity: O(n + m)

Space Complexity: O(n)

Edge Cases

No common elements

Duplicate elements

19. First Non-Repeating Character

Logic
“First count frequency of each character, then iterate again to find the first character with count equal to one.”

Time Complexity: O(n)
Space Complexity: O(n)

Edge Cases

All characters repeating

Empty string

20. Flatten Nested List

Logic
“I recursively traverse the list. If an element is another list, I flatten it recursively.”

Time Complexity: O(n)
Space Complexity: O(n)

Edge Cases

Deeply nested lists

Empty lists


21. Find Duplicates in List

Logic
“I iterate through the list while maintaining a set of elements already seen. If an element already exists in the set, it is a duplicate.”

Time Complexity: O(n)
Space Complexity: O(n)

Optimization
Using a hash set allows constant time lookup.

Edge Cases

No duplicates

All elements identical

Empty list

22. Reverse Words in a Sentence

Logic
“I split the sentence into words using spaces, reverse the order of the words, and then join them back together.”

Time Complexity: O(n)
Space Complexity: O(n)

Optimization
String split and join operations are already optimized.

Edge Cases

Multiple spaces

Single word

Empty string

23. Check Armstrong Number

Logic
“An Armstrong number is a number equal to the sum of its digits raised to the power of the number of digits. So I extract each digit, raise it to the power of the digit count, and sum them. If the sum equals the original number, it is an Armstrong number.”

Time Complexity: O(d) where d is number of digits
Space Complexity: O(1)

Edge Cases

Single digit numbers

Large numbers

24. Find GCD of Two Numbers

Logic
“I use the Euclidean algorithm. The idea is that the GCD of two numbers remains the same if we replace the larger number with the remainder when divided by the smaller number.”

Time Complexity: O(log(min(a,b)))
Space Complexity: O(1)

Optimization
Euclidean algorithm is already optimal.

Edge Cases

One number is zero

Both numbers equal

25. Check Balanced Parentheses

Logic
“I use a stack. Whenever I see an opening bracket, I push it onto the stack. When I see a closing bracket, I check if the top of the stack contains the matching opening bracket.”

Time Complexity: O(n)
Space Complexity: O(n)

Optimization
Stop early if mismatch occurs.

Edge Cases

Empty string

Only opening brackets

Incorrect nesting

26. Implement Stack

Logic
“A stack follows LIFO — Last In First Out. We can implement it using a list where push adds elements to the end and pop removes the last element.”

Time Complexity
Push → O(1)
Pop → O(1)

Space Complexity: O(n)

Edge Cases

Popping from empty stack

27. Implement Queue

Logic
“A queue follows FIFO — First In First Out. Elements are added at the rear and removed from the front.”

Time Complexity
Enqueue → O(1)
Dequeue → O(1) (using deque)

Space Complexity: O(n)

Optimization
Using deque is better than lists because removing from front of list is O(n).

Edge Cases

Dequeue from empty queue

28. Intersection of Two Arrays

Logic
“I convert both arrays into sets and find their intersection.”

Time Complexity: O(n + m)
Space Complexity: O(n)

Optimization
Hash sets allow fast lookup.

Edge Cases

No intersection

Arrays with duplicates

29. Group Anagrams

Logic
“I sort the characters of each word. Words that have the same sorted characters belong to the same anagram group.”

Time Complexity: O(n * k log k)
(n words, k word length)

Space Complexity: O(n)

Optimization
Use character frequency instead of sorting.

Edge Cases

Empty string

Words of different lengths

30. Rotate List by K Positions

Logic
“To rotate the list, I move the last k elements to the front.”

Time Complexity: O(n)
Space Complexity: O(n)

Optimization
Use modulo to handle k greater than list size.

Edge Cases

k = 0

k > length

Empty list

31. Find Pair with Given Sum

Logic
“I iterate through the array and store elements in a hash set. For each number, I check if its complement (target minus number) already exists.”

Time Complexity: O(n)
Space Complexity: O(n)

Optimization
Hash set approach avoids nested loops.

Edge Cases

No pair exists

Multiple valid pairs

32. Count Words in File

Logic
“I read the file contents and split the text into words based on spaces, then count them.”

Time Complexity: O(n) where n is number of characters
Space Complexity: O(n)

Optimization
Read file line by line for large files.

Edge Cases

Empty file

Special characters

33. Binary Search

Logic
“Binary search works on sorted arrays. I repeatedly divide the search space in half and compare the target with the middle element.”

Time Complexity: O(log n)
Space Complexity: O(1)

Edge Cases

Target not present

Empty array

ADVANCED (Sample Style)
34. Maximum Subarray Sum (Kadane's Algorithm)

Logic
“I iterate through the array and maintain a running sum. If the running sum becomes smaller than the current element, I restart the sum from that element.”

Time Complexity: O(n)

Space Complexity: O(1)

Optimization
Kadane’s algorithm avoids checking all subarrays.

Edge Cases

All negative numbers

Single element


35. Longest Substring Without Repeating Characters

Logic
“I use a sliding window technique. I expand the window until a duplicate character appears, then move the left pointer to remove duplicates.”

Time Complexity: O(n)
Space Complexity: O(n)

Optimization
Using a hash set allows fast duplicate checks.

Edge Cases

All characters same

Empty string


36. LRU Cache

Logic
“LRU Cache removes the least recently used item when capacity is exceeded. We maintain order using a structure like OrderedDict.”

Time Complexity
Get → O(1)
Put → O(1)

Space Complexity: O(capacity)

Edge Cases

Cache full

Accessing missing key


37. Detect Cycle in Linked List

Logic
“I use Floyd’s cycle detection algorithm, also called the tortoise and hare approach. One pointer moves one step while another moves two steps. If they meet, a cycle exists.”

Time Complexity: O(n)
Space Complexity: O(1)

Edge Cases

Single node

No cycle

38. Merge Overlapping Intervals

Logic
“I first sort the intervals by start time. Then I compare each interval with the last merged interval. If they overlap, I merge them.”

Time Complexity: O(n log n) (sorting)
Space Complexity: O(n)

Edge Cases

No overlaps

Fully overlapping intervals

39. Top K Frequent Elements

Logic
“I first count the frequency of each element, then retrieve the k elements with highest frequency using a heap or sorting.”

Time Complexity: O(n log k)
Space Complexity: O(n)

Optimization
Heap reduces sorting overhead.

Edge Cases

k larger than unique elements

40. Word Frequency in Large File

Logic
“I process the file line by line and update word frequencies using a counter. This avoids loading the entire file into memory.”

Time Complexity: O(n)
Space Complexity: O(unique words)

Edge Cases

Very large files

Case sensitivity

41. Multithreading vs Multiprocessing

Logic
“Multithreading allows multiple threads to run concurrently within a process, while multiprocessing runs separate processes using multiple CPU cores.”

Time Complexity
Depends on task.

Optimization
Use multiprocessing for CPU-bound tasks.

Edge Cases

Shared memory issues

Race conditions

42. Decorator Implementation

Logic
“A decorator is a function that wraps another function to add extra behavior before or after execution.”

Time Complexity: Depends on wrapped function
Space Complexity: O(1)

Edge Cases

Functions with arguments

Multiple decorators

43. Context Manager

Logic
“A context manager automatically manages resources. When entering the block it acquires resources, and when exiting it releases them.”

Time Complexity: O(1)
Space Complexity: O(1)

Edge Cases

Exceptions inside block

44. Generator vs Iterator

Logic
“A generator produces values lazily using yield, whereas an iterator implements __iter__ and __next__ methods.”

Time Complexity: O(n)
Space Complexity: O(1) for generators

Optimization
Generators save memory.

45. Custom Exception

Logic
“We define a custom exception class derived from the base Exception class to handle specific application errors.”

Time Complexity: O(1)
Space Complexity: O(1)

46. Read Large CSV Efficiently

Logic
“Instead of loading the entire CSV into memory, we read it in chunks or line by line.”

Time Complexity: O(n)
Space Complexity: O(chunk size)

47. Optimize Nested Loops

Logic
“Nested loops often cause O(n²) complexity. We can optimize by using hash maps or sets to reduce lookup time.”

Time Complexity: O(n)
Space Complexity: O(n)

48. Singleton Pattern

Logic
“A singleton pattern ensures that only one instance of a class exists throughout the application.”

Time Complexity: O(1)
Space Complexity: O(1)

Edge Cases

Multiple thread access


49. Rate Limiter

Logic
“A rate limiter restricts how many requests a user can make within a time window. Token bucket algorithm adds tokens at a fixed rate and consumes one token per request.”

Time Complexity: O(1)

Space Complexity: O(1)

Edge Cases

Burst traffic

Empty bucket

50. URL Shortener

Logic
“A URL shortener maps a long URL to a short unique key. The short key can be generated using hashing or base62 encoding.”

Time Complexity
Shorten → O(1)
Retrieve → O(1)

Space Complexity: O(n)

Edge Cases

Hash collision

Invalid short code