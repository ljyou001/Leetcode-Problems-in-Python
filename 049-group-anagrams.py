class SolutionSort:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        res = {}
        for i in strs:
            ind = str(sorted(i))
            if ind not in res.keys():
                res[ind] = [i]
            else:
                res[ind].append(i)
                
        return res.values()

class SolutionCounter:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for item in strs:
            item_count = tuple(self.count_string(item))
            if res.get(item_count):
                res[item_count].append(item)
            else:
                res[item_count] = [item]
        return res.values()
        
    def count_string(self, string):
        LENGTH_ALPHABET = 26
        count = [0 for _ in range(LENGTH_ALPHABET)]
        for char in string:
            count[ord(char) - ord('a')] += 1
        return count