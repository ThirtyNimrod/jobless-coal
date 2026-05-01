"""
LeetCode 28: Find the Index of the First Occurrence in a String
Approach: Knuth-Morris-Pratt (KMP) Algorithm
Time Complexity: O(n + m) where n = len(haystack), m = len(needle)
Space Complexity: O(m) for the LPS array
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # Build the LPS (Longest Prefix Suffix) array
        def build_lps(pattern):
            lps = [0] * len(pattern)
            length = 0  # Length of the previous longest prefix suffix
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
        i = j = 0  # i for haystack, j for needle
        
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
            if j == len(needle):  # Found the needle
                return i - j
            
            if i < len(haystack) and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1


if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    print(solution.strStr("sadbutsad", "sad"))  # Output: 0
    
    # Example 2
    print(solution.strStr("leetcode", "leeto"))  # Output: -1
    
    # Edge cases
    print(solution.strStr("a", "a"))  # Output: 0
    print(solution.strStr("aaaa", "aa"))  # Output: 0
