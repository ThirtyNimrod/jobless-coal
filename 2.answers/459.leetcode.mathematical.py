# ============================================================
# Problem : 459. Repeated Substring Pattern
# Source  : LeetCode
# URL     : https://leetcode.com/problems/repeated-substring-pattern/
# Approach: Mathematical
# ============================================================

def repeatedSubstringPattern(s: str) -> bool:
    """
    Approach: Mathematical
    Time Complexity : O(n)  Iterating through possible substring lengths
    Space Complexity: O(1)  No extra space used

    Strategy:
    Iterate through all possible substring lengths. If the length of the string
    is divisible by the substring length, check if repeating the substring forms
    the original string.
    """
    n = len(s)
    for l in range(1, n // 2 + 1):
        if n % l == 0:  # Check if length is divisible
            if s[:l] * (n // l) == s:
                return True
    return False

# Example Usage
if __name__ == "__main__":
    print(repeatedSubstringPattern("abab"))  # Expected: True
    print(repeatedSubstringPattern("aba"))   # Expected: False
    print(repeatedSubstringPattern("abcabcabcabc"))  # Expected: True
