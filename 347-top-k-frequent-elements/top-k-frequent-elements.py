class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        ans=[]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for i in range(k):
            maximum=max(freq.values())
            for num in freq:
                if freq[num]==maximum:
                    ans.append(num)
                    del freq[num]
                    break
        return ans
        