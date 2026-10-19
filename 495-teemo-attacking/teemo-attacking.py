class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        total = 0
        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i + 1] - timeSeries[i]
            total += min(gap, duration)
        if timeSeries:
            total += duration
        return total