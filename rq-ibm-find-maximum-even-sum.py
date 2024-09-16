class Solution:
    def findMaximumEvenSum(self, vals) -> int:
        min_positive_odd = float('inf')
        max_negative_odd = float('-inf')
        positive_sum = 0
        for num in vals:
            if num > 0:
                positive_sum += num
                if num % 2 == 1:
                    min_positive_odd = min(min_positive_odd, num)
            else:
                if num % 2 == 1:
                    max_negative_odd = max(max_negative_odd, num)
        
        if positive_sum % 2 == 0:
            return positive_sum
        
        return max(positive_sum + max_negative_odd, positive_sum - min_positive_odd)