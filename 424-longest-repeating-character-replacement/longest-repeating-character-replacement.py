class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        maximum = 0
        max_freq = 0
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            maximum = max(maximum, right - left + 1)
        return maximum