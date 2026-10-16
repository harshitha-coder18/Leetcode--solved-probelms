class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        num = n
        while num:
            res += num & 1
            num = num >> 1
        
        return res