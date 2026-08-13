class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right=-1
        for i in range(len(arr)-1,-1,-1):
            current=arr[i]
            arr[i]=max_right
            if current>max_right:
                max_right=current
             
        return arr
        