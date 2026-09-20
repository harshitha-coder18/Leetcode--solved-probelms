class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans=[]
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if intervals[i][1]>=intervals[j][0]:
                    intervals[i][1]=max(intervals[i][1],intervals[j][1])
            if not ans or intervals[i][0]>ans[-1][1]:
                ans.append(intervals[i])
        return ans
        