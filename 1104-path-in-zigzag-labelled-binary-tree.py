class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = int(math.log2(label)) + 1
        path = []
        while label > 0:
            path.append(label)
            max_value = (2 ** level) - 1
            min_value = 2 ** (level - 1)
            label = (max_value + min_value - label)//2
            level -= 1

        return path[::-1]