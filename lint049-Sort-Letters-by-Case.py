from typing import (
    List,
)

class SolutionPartition:
    """
    @param chars: The letter array you should sort by Case
    @return: nothing
    """
    def sort_letters(self, chars: List[str]):
        if not chars:
            return ''
        left = 0
        right = len(chars) - 1
        while left <= right:
            while left <= right and chars[left].islower():
                left += 1
            while left <= right and chars[right].isupper():
                right -= 1
            if left <= right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return chars