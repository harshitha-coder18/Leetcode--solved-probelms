class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen=set(jewels)
        count=0
        for ch in stones:
            if ch in seen:
                count+=1
        return count

        