class Solution:
    def judgeCircle(self, moves: str) -> bool:

        left=0
        right=-0
        up=0
        down=0
        for ch in moves:
            if ch=="L":
                left+=1
            elif ch=="R":
                right+=1
            elif ch=="U":
                up+=1
            elif ch=="D":
                down+=1
        if left==right and up==down:
            return True
        else:
            return False


