class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for i in nums:
            if i not in res:
                res.add(i)
            else:
                return True
        return False