class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                num = board[i][j]

                if num == ".":
                    continue

                if num in rows[i]:
                    return False
                else:
                    rows[i].add(num)

                if num in columns[j]:
                    return False
                else:
                    columns[j].add(num)

                box = (i // 3) * 3 + (j // 3)

                if num in boxes[box]:
                    return False
                else:
                    boxes[box].add(num)

        return True