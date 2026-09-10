class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        freq = {}

        # Count
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1

        ans = []

        # Take numbers in arr2 order
        for num in arr2:
            if num in freq:
                count = freq[num]

                for i in range(count):
                    ans.append(num)

                del freq[num]

        # Take remaining numbers
        remaining = []

        for num in freq:
            for i in range(freq[num]):
                remaining.append(num)

        remaining.sort()

        ans.extend(remaining)

        return ans