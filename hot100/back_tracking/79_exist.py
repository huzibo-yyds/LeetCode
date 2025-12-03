# 单词搜索，判断单词是否存在二维网格

class Solution:
    def exist_m(self, board: list[list[str]], word: str) -> bool:
        '''
        ❌没有 防止字母重复使用的机制

        '''
        rows,cols = len(board),len(board[0])

        directions = [[0,1],[1,0],[-1,0],[0,-1]] # 右下左上

        def backtrack(index,r,c):
            if index==len(word):
                return True

            flag = False
            for dr,dc in directions:

                # 剪枝
                if 0<=r+dr<rows and 0<=c+dc<cols and board[r+dr][c+dc]==word[index]:
                    # 1、2 做选择、进入下一层决策
                    flag=backtrack(index+1,r+dr,c+dc)
            
            
            return flag

        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0]:
                    if backtrack(1,r,c):
                        return True

        return False
    

    def exist(self, board: list[list[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])

        directions = [[0,1],[1,0],[-1,0],[0,-1]] # 右下左上


        # 判断从 (r, c) 开始，能否匹配 word[index:]
        def backtrack(index,r,c):
            if not (0 <= r < rows and 0 <= c < cols and board[r][c] == word[index]):
                return False
            
            if index==len(word)-1:
                return True

            # 标记当前节点为已访问，防止重复使用
            original_char = board[r][c]
            board[r][c] = '#'
            
            for dr,dc in directions:
                # 回溯 1 2
                if backtrack(index+1,r+dr,c+dc):
                    board[r][c]=original_char
                    return True
            
            # 回溯 3
            board[r][c]=original_char
            return False

        for r in range(rows):
            for c in range(cols):
                if backtrack(0,r,c):
                    return True

        return False
