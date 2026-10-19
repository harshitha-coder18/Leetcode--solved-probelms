class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans=[]
        for num in range(len(nums)):
            if nums[num]==target:
                ans.append(num)
        return ans

        