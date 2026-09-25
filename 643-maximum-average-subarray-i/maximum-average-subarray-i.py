class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        left=0
        right=k
        window_sum=0
        for i in range(k):
            window_sum+=nums[i]
        maximum_window=window_sum
        while right < len(nums):
            window_sum=window_sum-nums[left]+nums[right]
            maximum_window=max(maximum_window,window_sum)
            left+=1
            right+=1
        return maximum_window/k
    