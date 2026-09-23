class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
        ans = ""
        for ch in sorted(freq, key=freq.get, reverse=True):
            ans += ch * freq[ch]
        return ans