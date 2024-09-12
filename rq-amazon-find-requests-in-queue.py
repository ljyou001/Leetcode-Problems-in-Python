from collections import Counter 
import heapq

class Solution:
    def findRequestsInQueue(self, wait):
        if not wait:
            return [0]
        heap = []
        wait_set = set()
        for i in range(len(wait)):
            heapq.heappush(heap, (wait[i], i))
            wait_set.add(i)
        
        res = []
        time = 0
        i = 0
        while wait_set:
            while heap and heap[0][1] not in wait_set:
                heapq.heappop(heap)

            while heap and heap[0][0] <= time:
                _, task_id = heapq.heappop(heap)
                wait_set.remove(task_id)

            res.append(len(wait_set))

            while wait_set:
                if i in wait_set:
                    wait_set.remove(i)
                    break
                i += 1

            time += 1

        res.append(0)
        return res
