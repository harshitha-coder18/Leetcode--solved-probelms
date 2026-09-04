class Solution:
    def isHappy(self, n: int) -> bool: 
        while(n>=10):
            sum=0   
            while(n!=0):
                digit=n%10
                square=digit*digit
                sum+=square
                n=n//10
            n=sum
        if n==1 or n==7:
            return True
        else:
            return False
    