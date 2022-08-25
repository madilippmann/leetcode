class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        words = s.split()
        # print(words)
        # print(words[-1])
        return len(words[-1])