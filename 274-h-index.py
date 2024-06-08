class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(len(citations) - 1, -1, -1):
            paper_nums = len(citations) - i
            if citations[i] == paper_nums:
                return paper_nums
            if citations[i] <= paper_nums:
                return paper_nums - 1
        return len(citations)