# String Matching

## Concept Explanation
String matching is the process of finding one string (the pattern) within another string (the text). It is a fundamental problem in computer science with applications in text processing, search engines, and bioinformatics.

### When to Use:
- When you need to find the first occurrence of a substring in a string.
- When you need to count the occurrences of a substring in a string.

### Example Problem: Find the Index of the First Occurrence in a String (28)

#### Problem:
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

#### Solution:
A brute-force approach involves iterating through `haystack` and checking for the first occurrence of `needle` by comparing substrings.

#### Code:
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        len_h = len(haystack)
        len_n = len(needle)

        for i in range(len_h - len_n + 1):
            if haystack[i:i+len_n] == needle:
                return i

        return -1
```

---

## Complexity:
- **Time Complexity**: `O(n * m)` where `n` is the length of `haystack` and `m` is the length of `needle`.
- **Space Complexity**: `O(1)` as no additional space is used apart from a few variables.

---

## Optimal Approach: Knuth-Morris-Pratt (KMP) Algorithm

The KMP algorithm preprocesses the `needle` to create a Longest Prefix Suffix (LPS) array, which helps skip unnecessary comparisons during the search.

#### Code:
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        def build_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = build_lps(needle)
        i = j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

            if j == len(needle):
                return i - j

            if i < len(haystack) and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1
```

---

## Complexity of KMP:
- **Time Complexity**: `O(n + m)` where `n` is the length of `haystack` and `m` is the length of `needle`.
- **Space Complexity**: `O(m)` for the LPS array.