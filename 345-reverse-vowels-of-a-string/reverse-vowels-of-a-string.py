class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        right=len(s)-1
        vowels="AEIOUaeiou"
        ans=list(s)
        while left <= right:
            if ans[left] in vowels and ans[right] in vowels:
                ans[left],ans[right]=ans[right],ans[left]
                left+=1
                right-=1
            elif ans[left] in vowels and ans[right]not in vowels:
                right-=1
            else:
                left+=1
        return "".join(ans)
            


        