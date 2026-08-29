class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum_sum=float(-inf)
        left=0
        window_sum=0
        for right in range(len(nums)):
            window_sum+=nums[right]
            if right-left+1==k:
                maximum_sum=max(maximum_sum,window_sum)

                window_sum-=nums[left]
                left+=1
        average=maximum_sum/k
        return average
        