class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            
            # else, s[left] != s[right]
            # You must change s[left] or s[right] to make it palindrome
            if s[left] < s[right]:
                s[right] = s[left]
            else:
                s[left] = s[right]
            left += 1
            right -= 1
        return ''.join(s)