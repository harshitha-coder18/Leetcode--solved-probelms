class Solution:
    def nextPermutation(self, nums):
        
        # Step 1: Find the pivot
        i = len(nums) - 2
        
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: Find the number just greater than pivot
        if i >= 0:
            j = len(nums) - 1
            
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: Swap pivot and that number
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the part after pivot
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1