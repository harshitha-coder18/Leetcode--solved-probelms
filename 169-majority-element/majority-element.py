class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        maximum_key=max(freq,key=freq.get)
        return maximum_key


        