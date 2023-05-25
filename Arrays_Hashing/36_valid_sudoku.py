#36. Valid Sudoku - Medium - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visitedrow = []
        visitedcol = []
        visitedsec = []
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                elem = board[i][j]
                if elem != ".":
                    visitedrow += [(j, elem)]
                    visitedcol += [(i, elem)]
                    visitedsec += [(i//3, j//3, elem)]
        return len(visitedrow) == len(set(visitedrow)) and len(visitedcol) == len(set(visitedcol)) and len(visitedsec) == len(set(visitedsec))