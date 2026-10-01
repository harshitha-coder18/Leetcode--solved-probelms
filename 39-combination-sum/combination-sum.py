class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        stack = []

        def backtrack(start, total):
            if total == target:
                ans.append(list(stack))
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                stack.append(candidates[i])

                backtrack(i, total + candidates[i])

                stack.pop()

        backtrack(0, 0)
        return ans