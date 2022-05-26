# the most basic of two pointers method
# O(n) time
# O(1) space

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphabet = 'qwertyuiopasdfghjklzxcvbnm0123456789'
        # initialize a string of alphabet and s to lower

        i = 0
        j = len(s) - 1
        # initialize two pointers

        while i < j: # should not touch each other
            if s[i] not in alphabet:
                i += 1
            elif s[j] not in alphabet:
                j -= 1
            elif s[i] != s[j]: # after filtered by previous if statement, no junk while comparing
                return False
            else:    # should not put this outside of else, since it might pass when hit junk
                i += 1
                j -= 1
        return True