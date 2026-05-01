# ============================================================
# Problem : 242. Valid Anagram
# Source  : LeetCode
# URL     : https://leetcode.com/problems/valid-anagram/
# Approach: Hash Map
# ============================================================

def isAnagram(s: str, t: str) -> bool:
    """
    Approach: Hash Map
    Time Complexity : O(n)  Counting character frequencies
    Space Complexity: O(1)  Fixed size for lowercase English letters

    Strategy:
    Count the frequency of each character in both strings using a dictionary.
    Compare the two dictionaries. If they are equal, the strings are anagrams.
    """
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    return count_s == count_t

# Example Usage
if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))  # Expected: True
    print(isAnagram("rat", "car"))          # Expected: False
