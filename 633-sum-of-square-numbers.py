class SolutionTwoPointer:
    def judgeSquareSum(self, c: int) -> bool:
        search = [i ** 2 for i in range(int(math.sqrt(c)) + 1)]

        left = 0
        right = len(search) - 1
        while left <= right:
            if search[left] + search[right] > c:
                right -= 1
            elif search[left] + search[right] < c:
                left += 1
            else:
                return True
        return False

class SolutionTwoPointerConstantMemory:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5) + 1
        while left <= right:
            value = left * left + right * right
            if value > c:
                right -= 1
            elif value < c:
                left += 1
            else: # ==
                 return True
        return False

class SolutionSet:
    def judgeSquareSum(self, c: int) -> bool:
        search = set()
        for i in range(int(math.sqrt(c)) + 1):
            search.add(i ** 2)
        
        for i in range(int(math.sqrt(c)) + 1):
            if c - (i ** 2) in search:
                return True
        return False