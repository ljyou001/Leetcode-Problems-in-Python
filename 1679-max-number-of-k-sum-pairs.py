class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        numdict = {}
        for i in nums:
            if i in numdict.keys():
                numdict[i] += 1
            else:
                numdict[i] = 1
        print(numdict)
        res = 0
        for i in numdict.keys():
            if k-i in numdict.keys() and numdict[k-i] > 0:
                if k-i == i:
                    res += numdict[k-i] // 2
                    numdict[k-i] -= numdict[k-i] // 2 * 2
                else:
                    numb = min(numdict[i], numdict[k-i])
                    res += numb
                    numdict[i] -= numb
                    numdict[k-i] -= numb
        return res