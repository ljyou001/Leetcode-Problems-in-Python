class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    # lint 447
    def searchBigSortedArray(self, reader, target):
        right = 0
        while reader.get(right) < target:
            right = right * 2 + 1
        if reader.get(right) == target:
            return right
        
        left = right // 2
        while left + 1 < right:
            mid = (left + right) // 2
            if reader.get(mid) < target:
                left = mid
            else:
                right = mid
        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right
        return -1