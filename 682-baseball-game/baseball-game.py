class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        a=2
        for ch in operations:
            if ch.lstrip("- ").isdigit():
                stack.append(int(ch))
            elif ch=="C":
                stack.pop()
            elif ch=="D":
                b=a*int(stack[-1])
                stack.append(b)
            elif ch=="+":
                c=int(stack[-1])+int(stack[-2])
                stack.append(c)
       
        return sum(stack)

          


        