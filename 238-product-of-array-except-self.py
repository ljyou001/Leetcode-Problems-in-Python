#!!! prefix method
# O(n) time, O(n) space

class Solution_prefix_postfix_table:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # let's take [1,2,3,4] as an example

        prefix = [1] * len(nums)
        for i in range(len(nums)):
            if i < 1:
                prefix[i] = nums[i]
                continue
            prefix[i] = prefix[i - 1] * nums[i]
        # build a prefix list of [1, 2, 6, 24] 
        # the product of each number itself and the product of all numbers before it

        postfix = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = nums[i]
                continue
            postfix[i] = postfix[i + 1] * nums[i]
        # build a postfix list of [24, 12, 4, 1]
        # the product of each number itself and the product of all numbers after it
        
        res = []
        for i in range(len(nums)):
            # always mind the boundry
            if i == 0:
                res.append(postfix[i+1])
                continue
            if i == len(nums) - 1:
                res.append(prefix[i-1])
                continue
            res.append(prefix[i-1] * postfix[i+1])
        # result[i] is multipled by prefix[i-1] and postfix[i+1]
        
        return res


# Unilized version
# operation in the res list
# Time: O(n)
# Space: O(1)

class Solution_util: