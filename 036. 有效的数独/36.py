class Solution:

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            nums = board[i]
            tmp = []
            [tmp.append(j) for j in nums if j.isdigit()]
            if len(tmp) > len(set(tmp)):
                return False

        for i in range(9):
            v = []
            for j in range(9):
                v.append(board[j][i])
            tmp = []
            [tmp.append(k) for k in v if k.isdigit()]
            if len(tmp) > len(set(tmp)):
                return False

        for k in range(3):
            for v in range(3):
                tmp = []
                for i in range(3):
                    for j in range(3):
                        tmp.append(board[k * 3 + i][v * 3 + j])
                v = []
                [v.append(o) for o in tmp if o.isdigit()]
                if len(v) > len(set(v)):
                    return False
        return True

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
sol = Solution()
sol.isValidSudoku(board)
