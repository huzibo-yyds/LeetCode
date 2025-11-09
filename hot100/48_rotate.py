# 旋转图像 | 顺时针循环90度
# (i,j) -> (j,n-1-i)
def rotate(matrix):
    """
    将 n × n 矩阵顺时针旋转 90 度
    :param matrix: List[List[int]] - 输入的二维矩阵
    :return: None - 原地修改矩阵
    """
    n = len(matrix)
    
    # 先进行转置操作（沿主对角线翻转）
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # 再进行水平翻转（沿垂直中线翻转）
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

# 测试示例
if __name__ == "__main__":
    # 示例 1
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    print("原矩阵:")
    for row in matrix1:
        print(row)
    
    rotate(matrix1)
    print("旋转后:")
    for row in matrix1:
        print(row)
    
    # 示例 2
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print("\n原矩阵:")
    for row in matrix2:
        print(row)
    
    rotate(matrix2)
    print("旋转后:")
    for row in matrix2:
        print(row)