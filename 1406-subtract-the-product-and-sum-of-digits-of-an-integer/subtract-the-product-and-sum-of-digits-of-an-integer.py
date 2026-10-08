class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        addition=0
        multiplication=1
        while n>0:
            digit=n%10
            addition+=digit
            multiplication*=digit
            n=n//10
        return multiplication-addition
        