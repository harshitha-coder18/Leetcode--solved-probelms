class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        left = 0
        window = []

        for right in range(len(s2)):

            window.append(s2[right])

            # Keep window size equal to s1
            if right - left + 1 == len(s1):

                if sorted(window) == sorted(s1):
                    return True

                window.remove(s2[left])
                left += 1

        return False