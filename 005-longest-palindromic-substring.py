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