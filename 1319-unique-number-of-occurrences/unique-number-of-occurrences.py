class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq={}
        for ch in arr:
            if  ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        seen=set()
        for value in freq.values():
            if value  in seen:
                return False
            seen.add(value)
        return True

        
