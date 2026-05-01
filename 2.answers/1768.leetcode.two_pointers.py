"""
LeetCode 1768: Merge Strings Alternately
Approach: Two Pointers with Array Building
Time Complexity: O(n + m) where n = len(word1), m = len(word2)
Space Complexity: O(n + m) for the result array
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize an empty result list to store characters
        result = []
        
        # Get the lengths of both words
        n, p = len(word1), len(word2)
        
        # Find the minimum length of the two words
        min_length = min(n, p)
        
        # Loop through the minimum length and alternate characters
        for i in range(min_length):
            result.append(word1[i])  # Add character from word1
            result.append(word2[i])  # Add character from word2
        
        # Add the remaining letters from the longer word
        if n > p:
            result.append(word1[min_length:])  # Add remaining characters from word1
        elif p > n:
            result.append(word2[min_length:])  # Add remaining characters from word2
        
        # Join the list into a string and return
        return ''.join(result)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    print(solution.mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
    
    # Example 2
    print(solution.mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
    
    # Example 3
    print(solution.mergeAlternately("abcd", "pq"))  # Output: "apbqcd"
