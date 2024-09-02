class SolutionBruteForce:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        val2index = {}
        for i in range(len(nums2)):
            val2index[nums2[i]] = i

        res = []
        for num in nums1:
            index = val2index[num]
            res.append(self.get_next_greater(index, nums2))
        return res

    def get_next_greater(self, start, nums):
        for i in range(start + 1, len(nums)):
            if nums[start] < nums[i]:
                return nums[i]
        return -1

class SolutionMonotonicStack:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        val2index = {}
        stack = []
        next_grt_val = [-1] * len(nums2)
        for i in range(len(nums2)):
            val2index[nums2[i]] = i
            while stack and nums2[i] > stack[-1][1]:
                index, val = stack.pop()
                next_grt_val[index] = nums2[i]
            stack.append((i, nums2[i]))
        
        res = []
        for i in nums1:
            res.append(
                next_grt_val[val2index[i]]
            )
        return res