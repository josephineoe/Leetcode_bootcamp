class Solution:
    def reverseWords(self, s: str) -> str:
        # Split string by spaces (automatically removes extra spaces)
        words = s.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join them with a single space
        return ' '.join(reversed_words)
