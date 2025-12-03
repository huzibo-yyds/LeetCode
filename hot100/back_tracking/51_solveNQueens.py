# N皇后
# 皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        '''
        适合用回溯
        定下前一个元素后，再考虑后续元素
        每个元素遍历每行所有的位置
        '''
        result=[]
        board = [['.' for _ in range(n)] for _ in range(n)]

        # 用于快速判断的集合 （若每次遍历矩阵效率低
        columns = set()
        diagonals1 = set() # 主对角线 r - c
        diagonals2 = set() # 副对角线 r + c


        def backtrack(row:int):
            # 终止条件
            if row == n:
                temp_solution = ["".join(row_list) for row_list in  board]
                result.append(temp_solution)
                return
            
            # 遍历当前所有列，放置 Q
            for col in range(n):
                # 剪枝
                if col in columns or (row-col) in diagonals1 or  (row+col) in diagonals2:
                    continue

                # 1
                board[row][col]='Q'
                columns.add(col)
                diagonals1.add(row-col)
                diagonals2.add(row+col)

                # 2
                backtrack(row+1)

                # 3
                board[row][col]='.'
                columns.remove(col)
                diagonals1.remove(row-col)
                diagonals2.remove(row+col)


        backtrack(0)
        return result