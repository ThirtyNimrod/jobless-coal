---
title: "Hash Maps"
concept: hash_maps
module: 2
problems_referenced: [242.leetcode]
date_updated: 2026-05-02
---

# Hash Maps

> Part of the Python DSA Course  Module 2

## Real-World Analogy

A hash map is like a physical dictionary. You look up a word, and you instantly get its definition. You dont need to read every page to find the wordthe dictionary uses an internal system to jump directly to the right page.

## What Is It?

A **hash map** is a data structure that stores key-value pairs and provides average O(1) lookup, insertion, and deletion. It uses a hash function to compute a memory location from the key.

## When to Use This Pattern

> **Hash Map Pattern:** When a problem asks you to find a pair, group, or matchand doing it with nested loops feels slowask yourself: "Can I store what Ive already seen?" If yes, a hash map is probably the answer.

Look for these signals in a problem:
- You need to count occurrences of elements.
- You need to check for the existence of an element in constant time.
- You need to map one value to another (e.g., a number to its index).

## Your Problems That Use This

### 242. Valid Anagram (`1.questions/242.leetcode.md`)

> **The key use:** Count the frequency of each character in both strings and compare the counts.

```python
# From 2.answers/242.leetcode.hash_map.py
def isAnagram(s: str, t: str) -> bool:
    count_s, count_t = {}, {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    return count_s == count_t
```

See the full progressive explanation: [[3.understand/242.leetcode|Valid Anagram  Progressive Explanation]]

## Exercises

- **Exercise 1 — Two Sum (LeetCode 1)**: Given `nums` and `target`, return indices of two numbers that add up to `target` in O(n) time using a hash map.
    - Example: `nums = [2,7,11,15], target = 9` -> `[0,1]`

- **Exercise 2 — Group Anagrams**: Group anagrams from a list of strings. Use a hashable key (sorted string or character counts) to bucket words.
    - Example: `['eat','tea','tan','ate','nat','bat']` -> `[['eat','tea','ate'],['tan','nat'],['bat']]`

**Hints:** Use a dictionary mapping computed keys to lists or indices. Aim for O(n * k log k) with sorting-key or O(n * k) using counts (k = word length).

---