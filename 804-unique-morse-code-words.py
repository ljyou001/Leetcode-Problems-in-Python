class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = []
        list_a = "abcdefghijklmnopqrstuvwxyz"
        list_m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        match = {}
        
        for i in range(len(list_a)):
            match[ list_a[i] ] = list_m[i]
        
        for i in words:
            middle = ''
            for j in i:
                middle += match[j]
            res.append(middle)
        
        return len( set( res ) )