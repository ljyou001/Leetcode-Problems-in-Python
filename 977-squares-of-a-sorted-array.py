class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = []
        negative = []
        positive = []

        for i in nums:
            if i < 0:
                negative.append(i * i)
                continue
            positive.append(i * i)

        negative = negative[::-1]
        ind_n = 0
        ind_p = 0
        while ind_n < len(negative) and ind_p < len(positive):
            if negative[ind_n] < positive[ind_p]:
                res.append(negative[ind_n])
                ind_n += 1
            else:
                res.append(positive[ind_p])
                ind_p += 1
        if ind_n < len(negative):
            res += negative[ind_n:]
        if ind_p < len(positive):
            res += positive[ind_p:]
        return res