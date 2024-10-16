class Set:
    def solution(self, queries):
        built = set()
        res = []
        max_value = 0
        for i in queries:
            built.add(i)
            max_value = max(
                max_value,
                self.count_neighbor(i, built),
            )
            res.append(max_value)
        return res

    def count_neighbor(self, id, built):
        count = 0
        left = id
        right = id + 1
        while left in built:
            count += 1
            left -= 1
        while right in built:
            count += 1
            right += 1
        return count


class UnionFind:
    def solution(self, queries):
        built = {}
        res = []
        max_value = 0
        
        for i in queries:
            if i in built:
                res.append(max_value)
                continue

            left_size = built.get(i - 1, 0)
            right_size = built.get(i + 1, 0)
            total_size = left_size + right_size + 1
            
            built[i] = total_size
            built[i - left_size] = total_size  # left boundary
            built[i + right_size] = total_size  # right boundary
            
            max_value = max(max_value, total_size)
            res.append(max_value)

        return res