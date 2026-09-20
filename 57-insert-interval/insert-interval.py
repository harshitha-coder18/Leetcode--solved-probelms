class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []

        start = newInterval[0]
        end = newInterval[1]

        for interval in intervals:
            if interval[1] < start:
                ans.append(interval)
            elif interval[0] > end:
                ans.append([start, end])
                start = interval[0]
                end = interval[1]
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        ans.append([start, end])
        return ans