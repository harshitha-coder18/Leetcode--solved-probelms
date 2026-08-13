class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            found = -1

            for j in range(1, len(nums)):
                next_index = (i + j) % len(nums)

                if nums[next_index] > nums[i]:
                    found = nums[next_index]
                    break

            ans.append(found)

        return ans