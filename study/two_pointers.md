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

---

## Complexity:
- **Time Complexity**: `O(n + p)` where `n` and `p` are the lengths of the two strings.
- **Space Complexity**: `O(n + p)` for the result string.