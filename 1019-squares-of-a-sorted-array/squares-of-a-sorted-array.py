class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            square=i*i
            ans.append(square)
        ans.sort()
        return ans
        