class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            if i not in ans:
                ans.append(i)
        nums[:]=ans
