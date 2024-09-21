class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, a: List[int]):
        positives, negatives = 0, 0
        more_positive = -1
        for i in a:
            if i > 0:
                positives += 1
            else:
                negatives += 1
        if positives > negatives: 
            more_positive = 1
        self.partition(a, more_positive)
        print(a)
        self.interleaving(a, positives == negatives)

    def interleaving(self, a, is_same_length):
        left = 0
        right = len(a) - 2
        if is_same_length:
            left += 1
        while right > left:
            a[left], a[right] = a[right], a[left]
            left += 2
            right -= 2

    def partition(self, a, more_positive):
        # more right than left
        left = 0
        right = len(a) - 1
        while left <= right:
            while left <= right and a[left] * more_positive < 0:
                left += 1
            while left <= right and a[right] * more_positive > 0:
                right -= 1
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
