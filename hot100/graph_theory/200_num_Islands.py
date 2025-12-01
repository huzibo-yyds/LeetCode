# 岛屿
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成
import collections

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        num_islands = 0

        def dfs(r,c):
            '''深度优先搜索
            核心思想：优先探索一个分支到底，再回溯探索其他分支
            '''
            # 1、边界检查 + 终止条件
            # 如果越界，或者是水，或者是已经访问过的陆地，就返回
            if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == '1'):
                return

            # 2. 标记当前陆地为已访问（淹没）
            grid[r][c] = '0'

            # 3. 向四个方向递归探索
            dfs(r + 1, c)  # 下
            dfs(r - 1, c)  # 上
            dfs(r, c + 1)  # 右
            dfs(r, c - 1)  # 左

        for i in range(rows):
            for j in range(cols):
                if(grid[i][j]=='1'):
                    num_islands+=1
                    dfs(i,j)


        return num_islands
    

    ### 2️⃣、广度优先搜索实现 BFS
    def numIslands_bfs(self,grid:list[list[str]])-> int:
        ''' 广度优先搜索，与DFS基本一致，区别在于处理岛屿淹没

        1、 遍历整个岛屿，寻找‘1’
        2、 找到‘1’时，岛屿数量+1
        3、 使用BFS来处理岛屿淹没
            使用队列管理岛屿节点
            四个方向遍历岛屿，直到所有该岛屿节点被访问
        4、队列为空，则开始下个岛屿的寻找，返回1
        
        '''

        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        num_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    num_islands+=1
                    queue=collections.deque([r,c])
                    grid[r][c]= '0'

                    while queue:
                        curr_r,curr_c = queue.popleft()

                        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            next_r,next_c = curr_r+dr,curr_c+dc

                            if 0<= next_r <rows and 0<= next_c <cols and grid[next_r][next_c]=='1':
                                queue.append([next_r,next_c])
                                grid[next_r][next_c]='0'

        return num_islands
