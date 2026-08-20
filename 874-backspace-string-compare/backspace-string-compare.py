class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for ch in s:
            if ch=="#":
                stack1 and stack1.pop()
            else:
                stack1.append(ch)
        for ch in t:
            if ch=="#":
                stack2 and stack2.pop()
            else:
                stack2.append(ch) 
        if stack1==stack2:
            return True
        else:
            return False
           
        
            e
        