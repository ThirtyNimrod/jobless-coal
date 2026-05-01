# ============================================================
# Problem : 242. Valid Anagram
# Source  : LeetCode
# URL     : https://leetcode.com/problems/valid-anagram/
# Approach: Sorting
# ============================================================

def isAnagram(s: str, t: str) -> bool:
    """
    Approach: Sorting
    Time Complexity : O(n log n)  Sorting both strings
    Space Complexity: O(n)  Storing sorted strings

    Strategy:
    Sort both strings and compare them. If they are equal, the strings are anagrams.
    """
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

# Example Usage
if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))  # Expected: True
    print(isAnagram("rat", "car"))          # Expected: False
