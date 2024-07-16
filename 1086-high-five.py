# LINT 613
# This solution is from lintcode 613
# Originally, in leet 1086
# There is no Record class
# You can directly `for id, val in results` is OK to go

'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
from heapq import heappush, heappop

class Solution:
    def highFive(self, results):
        students = {}
        for record in results:
            if record.id not in students:
                students[record.id] = [record.score]
                continue
            if len(students[record.id]) < 5:
                heappush(students[record.id], record.score)
            elif students[record.id][0] < record.score:
                heappush(students[record.id], record.score)
                heappop(students[record.id])
        for key, scores in students.items():
            students[key] = sum(scores) / 5
        return students