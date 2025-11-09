# 矩阵置零

def setZeroes(matrix: list[list[int]]) -> None:

    # 标记第一行和第一列状况
    first_row_has_zero = any(matrix[0][j]==0 for j in range(len(matrix[0])))
    firsr_col_has_zero = any(matrix[i][0]==0 for i in range(len(matrix)))

    # -- 使用第一行和第一列 作为标记数组
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0

    for j in range(1,len(matrix[0])):
        if matrix[0][j]==0:
            for i in range(len(matrix)):
                matrix[i][j]=0

    for i in range(1,len(matrix)):
        if matrix[i][0]==0:
            for j in range(len(matrix[0])):
                matrix[i][j]=0

    ## -- 单独处理第一行与第一列
    if first_row_has_zero:
        for j in range(len(matrix[0])):
            matrix[0][j]=0
    if firsr_col_has_zero:
        for i in range(len(matrix)):
            matrix[i][0]=0

'''其他方法
1- 使用标记数组，标记行列0的情况
    循环2次： 1）标记0情况 2）置0
    时间复杂度：O(mn)
    空间复杂度：O(m+n)
2- 上述代码，使用第1行和第一列作为标记
'''


if __name__ == "__main__":
    
    # 测试用例1
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    print("测试用例1:")
    print("输入:", matrix1)
    setZeroes(matrix1)
    print("输出:", matrix1)

    
    # 测试用例2
    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print("测试用例2:")
    print("输入:", matrix2)
    setZeroes(matrix2)
    print("输出:", matrix2)
   