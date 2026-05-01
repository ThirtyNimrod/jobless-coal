"""
LeetCode 389: Find the Difference
Approach: XOR (Bit Manipulation)
Time Complexity: O(n) where n = len(s) + len(t)
Space Complexity: O(1) - only using a single variable
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # XOR all characters from s and t
        # XOR of identical characters = 0
        # XOR of all pairs cancels out, leaving only the extra character
        result = 0
        for char in s + t:
            result ^= ord(char)  # XOR the ASCII value
        return chr(result)  # Convert back to character


if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    print(solution.findTheDifference("abcd", "abcde"))  # Output: "e"
    
    # Example 2
    print(solution.findTheDifference("", "y"))  # Output: "y"
    
    # Example 3
    print(solution.findTheDifference("a", "aa"))  # Output: "a"
