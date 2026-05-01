"""
LeetCode 389: Find the Difference
Approach: Sorting + Two Pointers
Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) for sorted strings
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Sort both strings to align characters in order
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        
        # Compare characters one by one
        i, j = 0, 0
        while i < len(t):
            if j < len(s) and s[j] == t[i]:
                j += 1
            else:
                return t[i]  # Return the extra character in t
            i += 1
        
        # If no mismatch is found, the last character in t is the extra one
        return t[-1]


if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    print(solution.findTheDifference("abcd", "abcde"))  # Output: "e"
    
    # Example 2
    print(solution.findTheDifference("", "y"))  # Output: "y"
    
    # Example 3
    print(solution.findTheDifference("a", "aa"))  # Output: "a"
