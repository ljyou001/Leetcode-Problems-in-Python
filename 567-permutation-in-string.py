class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_list = [0] * 26
        for i in s1:
            s1_list[ord(i) - ord('a')] += 1
        
        s2_list = [0] * 26
        for i in range(0, len(s1)):
            s2_list[ord(s2[i]) - ord('a')] += 1
        
        if s1_list == s2_list:
            return True

        l = 0
        r = len(s1) - 1
        while r < len(s2) - 1:
            s2_list[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            s2_list[ord(s2[r]) - ord('a')] += 1
            if s1_list == s2_list:
                return True
        return False