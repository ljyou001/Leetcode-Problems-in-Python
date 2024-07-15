# Note: This question is not a data stream input

class Solution:
    def first_unique_number(self, nums: List[int], number: int) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if num == number:
                break
        else:
            return -1
        
        for num in nums:
            if counter[num] == 1:
                return num
            if num == number:
                break
        return -1