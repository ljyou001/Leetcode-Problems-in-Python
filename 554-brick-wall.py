class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = {}
        max_hole = 0
        for line in wall:
            brick = 0
            sum_all = sum(line)
            for i in line:
                brick += i
                if brick < sum_all:
                    count[brick] = count.get(brick, 0) + 1
                    max_hole = max(max_hole, count[brick])
        return len(wall) - max_hole