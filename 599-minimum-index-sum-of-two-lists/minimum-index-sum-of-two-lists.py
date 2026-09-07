class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        freq = {}
        ans = []
        minimum = float('inf')

        for i in range(len(list1)):
            freq[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in freq:
                total = i + freq[list2[i]]

                if total < minimum:
                    minimum = total
                    ans = [list2[i]]

                elif total == minimum:
                    ans.append(list2[i])

        return ans