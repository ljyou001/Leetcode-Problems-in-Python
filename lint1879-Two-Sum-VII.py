

class SolutionHashtable:
    def two_sum_v_i_i(self, nums: List[int], target: int) -> List[List[int]]:
        # write your code here
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        
        res = []
        for i in range(len(nums)):
            if target - nums[i] in nums_dict and target - nums[i] != nums[i]:
                res.append([i, nums_dict[target - nums[i]]])
                del nums_dict[nums[i]]
                del nums_dict[target - nums[i]]
        return res

class SolutionTwoPointers:
    def two_sum_v_i_i(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        首先把这个数组看成一段带折叠楼梯：例如 [1,-2,3,-4,5] 变成：

                      5 <- i
                 3
            1           <- 中折位置
              -2      
                   -4   <- j

        需要有两个指针：i 指向最高的数，j 指向最低的数。
        搜索target时，i 向下一个次高的数移动，j 向下一个次低的数移动。
        i，j交叉，搜索终止。
        '''             
        ret = []
        if len(nums) < 2:
            return ret
        
        # 判断i, j初始位置
        i, j = self.find_init_top_bottom(nums)

        # 相向双指针找target
        while (i != j ):
            curr = nums[i] + nums[j]
            if curr > target:
                i = self.move_down(i, nums)
            elif curr < target:
                j = self.move_up(j, nums)
            else:
                ret.append([min(i, j), max(i ,j)])
                
                # 这里只移动i指针，而不动j。同时移动两者可能让其交错，从而失去退出循环的机会
                i = self.move_down(i, nums)
        
        return ret
    
    def find_init_top_bottom(self, nums):
        i = j = len(nums) - 1
        if nums[-1] > 0:
            while nums[j] > 0:
                j -= 1
        else:
            while nums[i] < 0:
                i -= 1
  
        return i, j
    
    def move_down(self, i, nums):
        # 如果i还在中折上边儿
        if nums[i] > nums[0]:
            i -= 1
            while (i > 0 and nums[i] < nums[0]):
                i -= 1    
        
        # i就在中折，或者其下边儿了
        else:
            i += 1
            while(nums[i] > nums[0]):
                i += 1
        return i
    
    def move_up(self, j, nums):
        # 如果j还在中折下边儿
        if nums[j] < nums[0]:
            j -= 1
            while(j > 0 and nums[j] > nums[0]):
                 j -= 1
        
        # j就在中折，或者其上边儿了
        else:
            j += 1
            while (nums[j] < nums[0]):
                j += 1
        return j