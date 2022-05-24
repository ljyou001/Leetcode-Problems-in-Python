# monotonic increasing stack method
# time O(n) space O(n)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        
        # core part: coding a monotonic increasing stack
        for i in range(len(num)):
            while k > 0 and i > 0 and len(res) > 0 and int(num[i]) < int(res[-1]):
                # use a while here, as you need to check all the previous nums in the stack to ensure it is monotonic
                # int(num[i]) < int(res[-1]), use res[-1] rather than i - 1
                res.pop()
                k -= 1
            res.append(num[i])
        
        # when k is still not used up, we still need to pop the largest digits
        for i in range(k):
            if res:
                res.pop()
        
        # examine the final corner case, which is the res is empty
        if len(res) == 0:
            res = '0'
        
        return str(int(''.join(res)))