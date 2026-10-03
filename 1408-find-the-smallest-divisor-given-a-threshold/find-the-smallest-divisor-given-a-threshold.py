class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # lets try binary solution

        left = 1
        right = max(nums)

        while left <= right:
            mid = (left+right)//2

            if self.suffice(nums, mid, threshold):
                # can look in right side
                left = mid + 1

            else:
                # should look in left side
                right = mid - 1
        
        return left
    
    def suffice(self, nums, i, threshold):
        s = sum(ceil(j/i) for j in nums)
        return s > threshold