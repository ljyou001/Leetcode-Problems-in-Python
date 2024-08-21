class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)
        bobSizes = set(bobSizes)

        for i in aliceSizes:
            bval = (bob_sum - alice_sum) // 2 + i
            if int(bval) in bobSizes:
                return [i, int(bval)]