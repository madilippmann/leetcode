import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] in string.whitespace or s[start] in string.punctuation: start += 1
            elif s[end] in string.whitespace or s[end] in string.punctuation: end -= 1
            elif s[start].lower() != s[end].lower(): return False
            else:
                start += 1
                end -= 1

        return True