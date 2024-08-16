"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def merge_two_interval(self, list1: List[Interval], list2: List[Interval]) -> List[Interval]:
        res = []
        i = 0
        j = 0
        while i < len(list1) or j < len(list2):
            if i == len(list1):
                this_inte = list2[j]
                j += 1
            elif j == len(list2):
                this_inte = list1[i]
                i += 1
            elif list1[i].start <= list2[j].start:
                this_inte = list1[i]
                i += 1
            elif list1[i].start > list2[j].start:
                this_inte = list2[j]
                j += 1
            
            if not res or res[-1].end < this_inte.start:
                res.append(this_inte)
            else:
                res[-1] = Interval(res[-1].start, max(
                    res[-1].end,
                    this_inte.end,
                ))
        return res
