class Solution_slow:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(string):
            return string == string[::-1]
        
        i = 0
        res = ''
        while i < len(s):
            j = i
            while j < len(s) + 1:
                if isPalindrome(s[i:j]) and len(s[i:j]) > len(res):
                    res = s[i:j]
                j += 1
            i += 1
        return res

class Solution_exp:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            # the following part is for the odd length
            j = i
            k = i
            while j >= 0 and k < len(s) and s[j]==s[k]:
                if s[j] == s[k] and len(s[j:k+1]) > len(res):
                    print(1, s[j:k+1])
                    res = s[j:k+1] 
                j -= 1
                k += 1
            # this part is for even length
            j = i
            k = i + 1
            while j >= 0 and k < len(s) and s[j]==s[k]: # you need to add this "s[j]==s[k]" to ensure all the loop are correct, otherwise, e.g. "aacabdkacaa"
                if s[j] == s[k] and len(s[j:k+1]) > len(res):
                    print(2, s[j:k+1])
                    res = s[j:k+1] 
                j -= 1
                k += 1
        return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            palin1 = self.find_palindrome(s, i, i)
            if len(palin1) > len(res):
                res = palin1
            palin2 = self.find_palindrome(s, i, i + 1)
            if len(palin2) > len(res):
                res = palin2
        return res
        
    def find_palindrome(self, s, left, right):
        res = ''
        while right < len(s) and left > -1 and s[left] == s[right]:
            res = s[left:right + 1]
            right += 1
            left -= 1
        return res