class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        res = [1,1]
        for i in range(rowIndex - 1):
            newline = [1]
            for j in range(len(res)-1):
                newline.append(res[j] + res[j+1])
            newline.append(1)
            res = newline
        return res