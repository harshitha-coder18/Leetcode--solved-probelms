class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        total = 0
        count = 0

        for num in nums:
            total += num

            if total - k in freq:
                count += freq[total - k]

            if total in freq:
                freq[total] += 1
            else:
                freq[total] = 1

        return count