"""
LeetCode 389: Find the Difference
Approach: Summation (Sum of ASCII values)
Time Complexity: O(n) where n = len(s) + len(t)
Space Complexity: O(1) - only using a single variable
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Calculate the difference in ASCII sums
        # sum(t) - sum(s) gives the ASCII value of the extra character
        return chr(sum(map(ord, t)) - sum(map(ord, s)))


if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    print(solution.findTheDifference("abcd", "abcde"))  # Output: "e"
    
    # Example 2
    print(solution.findTheDifference("", "y"))  # Output: "y"
    
    # Example 3
    print(solution.findTheDifference("a", "aa"))  # Output: "a"
