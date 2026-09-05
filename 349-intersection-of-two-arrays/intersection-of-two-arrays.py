class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        seen=set(nums1)
        seen2=set(nums2)
        ans=[]
        for num in seen:
            if num in seen2:
                ans.append(num)
        return ans
