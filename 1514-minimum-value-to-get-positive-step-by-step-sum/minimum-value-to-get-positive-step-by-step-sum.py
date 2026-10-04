class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        prefix=0
        minimum=0
        for num in nums:
            prefix+=num
            minimum=min(minimum,prefix)
        answer=1-minimum
        return answer

        