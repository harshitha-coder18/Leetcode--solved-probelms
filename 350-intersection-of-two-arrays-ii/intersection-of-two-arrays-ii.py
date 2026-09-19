class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq={}
        for i in nums1:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        ans=[]
        for i in nums2:
            if i in  freq and freq[i]>0:
                ans.append(i)
                freq[i]-=1
        return ans 