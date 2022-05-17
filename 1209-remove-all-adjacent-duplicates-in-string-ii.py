class Solution_n_sq:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < 2:
            return s
        
        res = ''
        opt = ''
        for i in range(len(s)):
            if len(opt)==0 or (len(opt) < k and opt[-1] == s[i]):
                opt += s[i]
            else:
                if len(opt) == k:
                    opt = s[i]
                else:
                    res += opt
                    opt = s[i]
        if len(opt) < k: 
            res += opt
        # print(res)
        
        if res == s:
            return res
        else:
            return self.removeDuplicates(res,k)

### Solution_n_sq is too slow for large input, here is another better solution

# cool
class Solution_n:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res = ''
        for i in s:
            if len(stack) > 0 and stack[-1][0] == i:
                stack[-1][1] += 1
            else:
                stack.append([i,1])
            if stack[-1][1] == k:
                stack.pop()
                # Here is the point about this line
                # If the last element in the stack is the same as the current element,
                # it will always pop the stack until the last element is not the same as the current element
                # Say s = 'abcddcba', k = 2
                # it will not just pop ['d',2] but also pop ['c',2], ['b',2] and ['a',2] at the same time
        for i in stack:
            res += i[0] * i[1]
            
        return res