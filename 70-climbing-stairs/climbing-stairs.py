class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2

        if n == 1:
            return a

        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c

        return b