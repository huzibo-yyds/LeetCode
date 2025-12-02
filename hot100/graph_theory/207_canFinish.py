# 课程表
# 某些课程存在先修关系  prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi
#  [0, 1] ，学习课程0，需要先完成课程1
# 📍 判断是否可能修完，返回True 和 False

'''
- 顶点，课程
- 边，课程之间的先修关系

构造出来的图:
- 若存在环，则无法完成
- 若不存在环，有向无环图，则可以完成
'''

import collections

class Solution:
    # 1️⃣ BFS，模拟课程学习路径
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if numCourses<=1:
            return True
        
        adj=[[] for _ in range(numCourses)]
        in_degree=[0]*numCourses


        for course,prereq in prerequisites:
            adj[prereq].append(course)  # 邻接表，表示以当前节点为前缀的节点有哪些   # 图的表示方法，邻接表、邻接矩阵
            in_degree[course]+=1  # 入度，表示当前课程需要几个前缀
        

        queue = collections.deque() # 存储已就绪课程
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)

        # BFS过程，拿出课程，表示已完成
        course_taken = 0
        while queue:
            prereq_course = queue.popleft()
            course_taken+=1 # 完成课程+1
            
            # 已完成课程后，更细该课程后续课程
            for next_course in adj[prereq_course]:
                in_degree[next_course]-=1
                if in_degree[next_course]==0:
                    queue.append(next_course)

        return course_taken == numCourses

    # 2️⃣ 直接判断构造的图是否存在环
    def canFinish_dfs(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        '''
        深度优先搜索 (DFS) 判断有向图是否有环
        
        节点状态:
        0: 未访问 (unvisited)
        1: 访问中 (visiting) - 在当前递归栈中
        2: 已访问 (visited) - 已被证明无环
        '''

        # 邻接表表示图 prereq -> course
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        # 0: unvisited, 1: visiting, 2: visited
        visited = [0] * numCourses

        def has_cycle(course:int)-> bool:
            if visited[course] == 1:
                return True
            if visited[course]==2:
                return False
            
            visited[course] = 1

            for next_course in adj[course]:
                if has_cycle(next_course):
                    return True
                
            visited[course]=2
            return False

        for i in range(numCourses):
            if visited[i]==0:
                if has_cycle(i):
                    return False
        
        return True