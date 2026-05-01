# Two Pointers

## Concept Explanation
The two pointers technique is a common algorithmic approach used to solve problems involving arrays or strings. It involves using two indices (or pointers) to traverse the data structure, often from different directions or at different speeds.

### When to Use:
- When you need to find pairs or subarrays that satisfy a certain condition.
- When you need to merge or compare two sequences.

### Example Problem: Merge Strings Alternately (1768)

#### Problem:
You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

#### Solution:
We use two pointers to iterate through both strings simultaneously. At each step, we append one character from each string to the result. After the shorter string is exhausted, we append the remaining characters from the longer string.

#### Code:
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        n, p = len(word1), len(word2)
        min_length = min(n, p)

        for i in range(min_length):
            result.append(word1[i])
            result.append(word2[i])

        if n > p:
            result.append(word1[min_length:])
        else:
            result.append(word2[min_length:])

        return ''.join(result)
```

### Two Pointers

> **Concept**: Use two pointers to efficiently solve problems involving rearranging or comparing elements in arrays or linked lists.

#### Problems Covered:
- [[1.questions/283.leetcode|283. Move Zeroes]]
  - **Key Use**: Use two pointers to move all non-zero elements to the front of the array while maintaining their relative order.
  - **Solution**: [[2.answers/283.leetcode.two_pointers.py|Two Pointers Solution]]
  - **Explanation**: [[3.understand/283.leetcode|Progressive Explanation]]

---

## Complexity:
- **Time Complexity**: `O(n + p)` where `n` and `p` are the lengths of the two strings.
- **Space Complexity**: `O(n + p)` for the result string.

## Exercises

- **Exercise 1 — Move Zeroes (LeetCode 283)**: Move all zeros to the end of the array in-place while preserving order.
    - Example: `nums = [0,1,0,3,12]` -> `[1,3,12,0,0]`

- **Exercise 2 — Two Sum II (Input Array Is Sorted, LeetCode 167)**: Given a sorted array, find indices of two numbers summing to target using two pointers.
    - Example: `numbers = [2,7,11,15], target = 9` -> `[1,2]` (1-based indices)

**Hints:** Practice pointer initialization and loop invariants; verify termination conditions with odd/even length inputs.