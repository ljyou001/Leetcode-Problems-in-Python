class Solution_slow:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(string):
            return string == string[::-1]
        
        i = 0
        res = []
        while i < len(words):
            j = 0
            while j < len(words):
                if i != j and isPalindrome(words[i]+words[j]):
                    res.append([i,j])
                j += 1
            i += 1
        return res