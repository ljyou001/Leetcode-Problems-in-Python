class Solution:
    """
    Best method but not the best utilized
    """
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter1 = self.counting_two_lists(nums1, nums2)
        counter2 = self.counting_two_lists(nums3, nums4)
        res = 0
        for index, val in counter1.items():
            if -index in counter2:
                res += len(val) * len(counter2[-index])
        return res
        
    def counting_two_lists(self, nums1, nums2):
        counter = {}
        for i in nums1:
            for j in nums2:
                two_sum = i + j
                if two_sum not in counter:
                    counter[two_sum] = []
                counter[two_sum].append((i, j))
        return counter

class Solution:
    """
    Utilized write operations
    """
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter1 = self.counting_two_lists(nums1, nums2)
        counter2 = self.counting_two_lists(nums3, nums4)
        res = 0
        for index, val in counter1.items():
            if -index in counter2:
                res += val * counter2[-index]
        return res
        
    def counting_two_lists(self, nums1, nums2):
        counter = {}
        for i in nums1:
            for j in nums2:
                counter[i + j]= counter.get(i + j, 0) + 1
        return counter

class Solution:
    """
    This one is wrong for the question,
    But it is correct if unique combinations required
    """
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter1 = self.counting_two_lists(nums1, nums2)
        counter2 = self.counting_two_lists(nums3, nums4)
        res = 0
        for index, val in counter1.items():
            if -index in counter2:
                res += len(val) * len(counter2[-index])
        return res
        
    def counting_two_lists(self, nums1, nums2):
        counter = {}
        for i in nums1:
            for j in nums2:
                two_sum = i + j
                if two_sum not in counter:
                    counter[two_sum] = set()
                counter[two_sum].add((i, j))
        return counter