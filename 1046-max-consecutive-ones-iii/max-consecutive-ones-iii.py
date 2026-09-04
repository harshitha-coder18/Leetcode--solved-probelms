class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0
        zeros = 0
        answer = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeros += 1

            while zeros > k:

                if nums[left] == 0:
                    zeros -= 1

                left += 1

            answer = max(answer, right - left + 1)

        return answer