class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq={}
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        first=list(freq.values())[0]
        for value in freq.values():
            if value!=first:
                return False
        
        return True
        