class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        def dfs(num):
            if len(num) == len(nums[0]):
                if num not in nums:
                    res.append(num)
                return
            if len(res) == 1:
                return
            num += "1"
            dfs(num)
            num = num[:-1]
            num += "0"
            dfs(num)
            num = num[:-1]
        dfs("")
        return res[0]
    
        # res = []
        # def dfs(num):
        #     print(num)
        #     if len(num) == len(nums[0]):
        #         if num not in nums:
        #             res.append(num)
        #         return
        #     if len(res) == 1:
        #         return
        #     dfs(num + "1")
        #     num = num[:-1]
        #     dfs(num + "0")
        #     num = num[:-1]
        # dfs("")
        # return res[0]