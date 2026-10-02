class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)
        ans = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                total = mul + ans[i + j + 1]

                ans[i + j + 1] = total % 10
                ans[i + j] += total // 10

        return ''.join(map(str, ans)).lstrip('0')
        