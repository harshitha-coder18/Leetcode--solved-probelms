class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left=0
        window_sum=0
        answer=0
        vowels="aeiou"
        for right in range(len(s)):
            if s[right] in vowels:
                window_sum+=1
            if right-left+1==k:
                answer=max(answer,window_sum)

                if s[left] in vowels:
                    window_sum-=1
                left+=1
        return answer


        