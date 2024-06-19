from typing import (
    List,
)

class Solution:
    """
    @param arr: a list
    @param helper: You can using compare function by helper.compare(int, int, int, int)
    @return: max element index
    """
    def get_max_element_index(self, arr: List[int], helper: Helper) -> int:
        left = 0
        right = len(arr) - 1
        while left + 1 < right:
            if (right - left + 1) % 2 == 1:
                leftover = right
                right -= 1
            else:
                leftover = None
            
            mid = (left + right) // 2
            comp_res = helper.compare(left, mid, mid + 1, right)
            print(comp_res)
            if comp_res == 1: 
                right = mid
            elif comp_res == -1:
                left = mid + 1
                # 注意正确使用 = 和 ==
            else: # ==0
                return leftover

        return left if helper.compare(left, left, right, right) == 1 else right