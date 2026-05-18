class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        # reverse words
        words = words[::-1]

        # join with single space
        return " ".join(words)