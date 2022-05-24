#!!! heap

import heapq

class Solution_heap:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        heaplist = [] 
        # to declare a heap, just use a list is OK or heapify function to a list
        for num, char in [(a * -1, 'a'), (b * -1, 'b'), (c * -1, 'c')]:
            if num < 0: 
                # this is to ensure the >=0 number will not get into the heap, 
                # you cannot filter out after added by heapify
                # if not clean up the 0, the else below will add some 0 chars to the result
                heapq.heappush(heaplist, (num, char))
                # note how to push one by one to the heap
        
        while heaplist:
            num_1, char_1 = heapq.heappop(heaplist)
            # this is how to pop a element from heap: heapq.heappop(<heap name>)
            
            if len(res) > 1 and res[-1] == char_1 and res[-2] == char_1:
                if not heaplist: 
                    # ALWAYS check the boundary. Since no 0 char in the heap, we just need to check heaplist itself
                    break
                num_2, char_2 = heapq.heappop(heaplist)
                res += char_2
                num_2 += 1
                if num_2 < 0:
                    # if the number is ==0, then no need to add back to the heap
                    heapq.heappush(heaplist, (num_2, char_2))
            else:
                res += char_1
                num_1 += 1
            if num_1 < 0: 
                # if the number is ==0, then no need to add back to the heap
                heapq.heappush(heaplist, (num_1, char_1))

        return res