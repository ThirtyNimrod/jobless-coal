"""
LeetCode 28: Find the Index of the First Occurrence in a String
Approach: Brute Force (Substring Comparison)
Time Complexity: O((n - m + 1) * m) = O(n * m) in worst case
Space Complexity: O(1)
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is empty, return 0
        if not needle:
            return 0
        
        # Get the lengths of haystack and needle
        len_h = len(haystack)
        len_n = len(needle)
        
        # Loop through the haystack
        # Only iterate up to where needle can fit
        for i in range(len_h - len_n + 1):
            # Check if the substring of haystack matches needle
            if haystack[i:i+len_n] == needle:
                return i  # Return the starting index of the match
        
        # If no match is found, return -1
        return -1


if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    print(solution.strStr("sadbutsad", "sad"))  # Output: 0
    
    # Example 2
    print(solution.strStr("leetcode", "leeto"))  # Output: -1
    
    # Edge case
    print(solution.strStr("a", "a"))  # Output: 0
    print(solution.strStr("aaaa", "aa"))  # Output: 0
