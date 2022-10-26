class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_count = {}
        res = set()
        req_pass = len(nums) / 3

        for i in nums:
            num_count[i] = num_count.get(i, 0) + 1
            if num_count[i] > req_pass:
                res.add(i)
                
        return list(res)