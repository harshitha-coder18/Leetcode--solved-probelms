class Solution:
    def buildArray(self, nums):
        n=len(nums)
        op=[]
        for i in range(n):
            ans = nums[nums[i]] 
            op.append(ans)
        return op