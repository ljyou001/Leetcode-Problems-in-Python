class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                lower_temp = stack.pop()
                res[lower_temp[1]] = i - lower_temp[1]
            stack.append([temperatures[i], i])
        
        return res


# Faster way
# If you will use index and value for a list, please use enumerate
# which will be faster
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp , index = stack.pop()
                res[index] = i - index
            stack.append((t,i))

        return res