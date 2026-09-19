class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        n=len(nums)
        freq={}
        ans=[]
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        count=0
        for key,value in freq.items():
            if value!=1:
                ans.append(key)
        return ans


        