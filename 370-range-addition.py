# LINT 903

# [0 0 0 0 0]

# [0 2 0 0 -2]
# [0 2 2 2 0]

# [0 2 3 0 -2]
# [0 2 5 5 3]

# [-2 2 3 2 -2]
# [-2 0 3 5 3]

class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def get_modified_array(self, length: int, updates: List[List[int]]) -> List[int]:
        # Write your code here
        prefix_sub = [0] * length
        for start, end, inc in updates:
            prefix_sub[start] += inc
            if end + 1 < length:
                prefix_sub[end + 1] -= inc
        
        res = [0] * length
        prev = 0
        for i in range(length):
            res[i] = prev + prefix_sub[i]
            prev = res[i]
        return res