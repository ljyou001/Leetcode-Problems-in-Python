class TimeMapTemplate:

    def __init__(self):
        self.kv = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kv:
            self.kv[key].append((timestamp, value))
        else:
            self.kv[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ''
        
        val_list = self.kv[key]
        left = 0
        right = len(val_list) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if val_list[mid][0] > timestamp:
                right = mid
            else:
                left = mid
        
        if val_list[left][0] > timestamp:
            return ''
        if val_list[right][0] <= timestamp:
            return val_list[right][1]
        return val_list[left][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.store.get(key):
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.store.get(key) or self.store[key][0][0] > timestamp:
            return ""
        res = ""
        val_list = self.store[key]
        l, r = 0, len(val_list) - 1
        while l <= r:
            p = (l + r) // 2
            if val_list[p][0] <= timestamp:
                l = p + 1
                res = val_list[p][1]
            else:
                r = p - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)