class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for i in nums:
            if i not in num_dict.keys():
                num_dict[i] = 1
            else:
                num_dict[i] += 1
        num_list = sorted(num_dict.items(), key = lambda x:x[1], reverse=True)
        # this method will tansfer the dict to a tupled list
        # dict.items() will return a dict items to tuples
        print(num_list)
        result = []
        for i in range(k):
            result.append(num_list[i][0])
        return result

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        nums = []
        for i in count:
            heapq.heappush(nums, (count[i] * -1, i))
        res = []
        for i in range(k):
            res.append(heapq.heappop(nums)[1])
        return res