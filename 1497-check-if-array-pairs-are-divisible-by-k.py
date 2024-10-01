class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if not arr:
            return False

        reminders = {}
        for i in arr:
            mod = (i % k + k) % k
            reminders[mod] = reminders.get(mod, 0) + 1
        
        for i in arr:
            mod = (i % k + k) % k
            if mod == 0:
                if reminders[mod] % 2 != 0:
                    return False 
                continue
            if reminders[mod] != reminders.get(k - mod, 0):
                return False
            
        return True