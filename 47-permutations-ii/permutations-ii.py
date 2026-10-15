class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        curr = []
        n = len(nums)
        freq = [False] * n

        def backtrack():
            if len(curr) == n:
                res.append(curr[:])
                return

            for i in range(n):
                if freq[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not freq[i - 1]:
                    continue

                freq[i] = True
                curr.append(nums[i])

                backtrack()

                curr.pop()
                freq[i] = False

        backtrack()
        return res