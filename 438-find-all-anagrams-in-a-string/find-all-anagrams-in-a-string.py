class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        left = 0
        result = []

        p_count = {}
        window_count = {}

        # Count characters in p
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        for right in range(len(s)):

            # Add s[right] to window
            ch = s[right]
            window_count[ch] = window_count.get(ch, 0) + 1

            # Keep window size equal to len(p)
            if right - left + 1 == len(p):

                # Check if frequencies are same
                if window_count == p_count:
                    result.append(left)

                # Remove s[left]
                left_ch = s[left]
                window_count[left_ch] -= 1

                if window_count[left_ch] == 0:
                    del window_count[left_ch]

                left += 1

        return result