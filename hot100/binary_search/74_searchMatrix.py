# 搜索二维矩阵 m x n 整数矩阵

# 每行递增，下一行第一个数字大于上一行最后一个数字
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        '''
        将数组坐标，转换为单个整数
        '''
        rows,cols = len(matrix),len(matrix[0])
        left,right=0,(rows*cols - 1)

        # 根据序号返回在数组中的值
        def value(num:int)->int:
            r=num//cols 
            c=num%cols

            return matrix[r][c]

        while left<=right:
            mid= left+(right-left)//2
            if value(mid)==target:
                return True
            elif value(mid)<target:
                left=mid+1
            else:
                right=mid-1

        return False