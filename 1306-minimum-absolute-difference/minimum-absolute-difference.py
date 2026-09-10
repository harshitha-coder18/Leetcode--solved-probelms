class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum=float('inf')
        for i in range(len(arr)-1):
            differences=arr[i+1]-arr[i]
            minimum=min(minimum,differences)
        ans=[]
        for i in range(len(arr)-1):
            differences=arr[i+1]-arr[i]
            if differences==minimum:
                ans.append([arr[i],arr[i+1]])
        return ans

