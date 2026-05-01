# ============================================================
# Problem : 459. Repeated Substring Pattern
# Source  : LeetCode
# URL     : https://leetcode.com/problems/repeated-substring-pattern/
# Approach: String Manipulation
# ============================================================

def repeatedSubstringPattern(s: str) -> bool:
    """
    Approach: String Manipulation
    Time Complexity : O(n)  Checking substring in concatenated string
    Space Complexity: O(n)  Concatenated string

    Strategy:
    Concatenate the string with itself and remove the first and last characters.
    Check if the original string exists in the modified concatenated string.
    """
    doubled_s = (s + s)[1:-1]
    return s in doubled_s

# Example Usage
if __name__ == "__main__":
    print(repeatedSubstringPattern("abab"))  # Expected: True
    print(repeatedSubstringPattern("aba"))   # Expected: False
    print(repeatedSubstringPattern("abcabcabcabc"))  # Expected: True
