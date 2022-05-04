class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        if len(string) <= 1:
            return True
        i = 0
        j = len(string)-1
        while i < j:
            if string[i] != string[j]:
                return False
            i = i + 1
            j = j - 1
        return True