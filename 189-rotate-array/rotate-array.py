class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        ans=[]
        ans1=[]
        ans2=[]
        k=k%len(nums)
       
        for i in range(len(nums)-k,len(nums)):
            ans1.append(nums[i])
        for i in range(0,len(nums)-k):
            ans2.append(nums[i])
        ans=ans1+ans2
        nums[:]=ans


