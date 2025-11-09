# 搜索二维矩阵 II
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
       """
       在有序二维矩阵中搜索目标值
       
       Args:
              matrix: List[List[int]] - m x n 的有序矩阵
              target: int - 目标值
       
       Returns:
              bool - 是否找到目标值
       """       
       if not matrix or not matrix[0]:
              return False

       # 类比二分查找，从右上角开始，减少搜索次数
       row=0
       col=len(matrix[0])-1


       while  row<len(matrix) and col>=0:
              if matrix[row][col]==target:
                     return True
              
              # 根据当前值与目标值关系移动
              elif matrix[row][col]> target:
                     col-=1
              else:
                     row+=1
                     
       return False

if __name__ == "__main__":
       matrix1 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
       target1 = 5
       print(searchMatrix(matrix1,target1))

       matrix2 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
       target2 = 20
       print(searchMatrix(matrix2,target2))
