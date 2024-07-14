class SolutionSort:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        count = 1
        max_count = 1
        for i in range( len(nums) -1 ):
            if nums[i] != nums[i+1]:
                if nums[i] == nums[i+1] - 1:
                    count = count + 1
                    max_count = max(max_count, count)
                else: 
                    count = 1
        return max_count
# sort method takes O(nlogn) time, O(1) space if input not counted in space

class SolutionLinear:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = set(nums)
        i = 0
        starts = []
        for i in nums:
            if i-1 not in nums:
                starts.append(i)
        res = starts
        for i in range(len(starts)):
            start = starts[i]
            res[i] = 1
            while start + 1 in nums:
                res[i] += 1
                start += 1
        return max(res)

class SolutionSet:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for i in nums:
            number_plus = i + 1
            number_minus = i - 1
            # initialize two vars covers possible +1 and -1 in the set
            count = 1
            while number_plus in num_set:
                # search for +1, +1, +1...
                count += 1
                num_set.remove(number_plus)
                number_plus += 1
            while number_minus in num_set:
                # search for -1, -1, -1...
                count += 1
                num_set.remove(number_minus)
                number_minus -= 1
            # as long as they are continous, they should be counted into one same group
            res = max(res, count)
        return res
        
# Set method take O(n) time, O(n) space

class SolutionSetII:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        while nums:
            numb = nums.pop()
            numb_up = numb + 1
            numb_down = numb - 1
            cur_res = 1
            while numb_up in nums:
                nums.remove(numb_up)
                cur_res += 1
                numb_up += 1
            while numb_down in nums:
                nums.remove(numb_down)
                cur_res += 1
                numb_down -= 1
            res = max(res, cur_res)
        return res

class SolutionSetIII:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 in num_set:
                continue
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)

        return longest_streak