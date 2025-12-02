# 994 腐烂的橘子
'''
1、 0空，1新鲜，2腐烂
2、 腐烂橘子，四个方向橘子腐烂
return: 没有新鲜橘子为止所必须经过的最小分钟数 | 如果不可能，返回 -1
'''

import collections

class Solution:
    # ⭐️ 多源广度优先搜索
    def orangesRotting(self, grid: list[list[int]]) -> int:
        '''
        适合使用广度优先搜索，BFS能够模拟逐层扩展、 所有腐烂橘子同一时间发生

        算法思路：值为2的橘子在网格中扩散的过程

        1、初始化，获得腐烂源坐标
        2、处理边界情况，若没有新鲜橘子，则不需要执行
        3、开始BFS 模拟时间流逝
        4、得出结果
            若 fresh_count 为0，则返回minutes
            若 fresh_count不为0，则说明存在感染不到的
                
        '''
        if not grid:
            return 0
        
        rows,cols = len(grid),len(grid[0])
        queue = collections.deque()
        fresh_count = 0

        # 1 init
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh_count+=1
                elif grid[r][c]==2:
                    queue.append([r,c])
        
        # 2 边界判断
        if fresh_count==0:
            return 0
        
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 3 BFS
        while queue:
            
            if fresh_count==0:
                break
            level_size = len(queue)

            for _ in range(level_size):
                r,c = queue.popleft()
                for dr,dc in directions: # 逐层检查
                    next_r,next_c = r+dr,c+dc

                    if 0<= next_r <rows and 0<= next_c <cols and grid[next_r][next_c]==1:
                        grid[next_r][next_c]=2
                        fresh_count-=1
                        queue.append([next_r,next_c])

            if queue:
                minutes+=1

        # 4 结果判断
        return minutes if fresh_count==0 else -1