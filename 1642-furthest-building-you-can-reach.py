class SolutionMemoSearch:
    """
    Will Over Memory
    """
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        memo = {}
        return self.dfs(heights, bricks, ladders, 0, memo)

    def dfs(self, heights, bricks, ladders, index, memo):
        if index == len(heights) - 1:
            return index
        
        if (index, bricks, ladders) in memo:
            return memo[(index, bricks, ladders)]

        res = index
        if heights[index] >= heights[index + 1]:
            res = max(
                res, 
                self.dfs(heights, bricks, ladders, index + 1, memo)
            )
        else:
            height_diff = heights[index + 1] - heights[index]
            if height_diff <= bricks:
                res = max(
                    res, 
                    self.dfs(heights, bricks - height_diff, ladders, index + 1, memo)
                )
            if ladders > 0:
                res = max(res, self.dfs(heights, bricks, ladders - 1, index + 1, memo))
        memo[(index, bricks, ladders)] = res
        return res