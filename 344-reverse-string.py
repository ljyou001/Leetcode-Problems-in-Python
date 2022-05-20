class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            x = s[(i+1) * -1]
            s[(i+1) * -1] = s[i]
            s[i] = x