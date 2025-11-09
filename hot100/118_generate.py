# 杨辉三角


def generate(numRows: int) -> list[list[int]]:

    if numRows==0:
        return []
    
    # 方法1，逐行迭代构建
    # result=[[1]]
    # for i in range(1,numRows):
    #     # 每行第一个元素为 1
    #     row=[1]
    #     # 计算中间元素，上一行对应两个元素和
    #     for j in range(1,i):
    #         row.append(result[i-1][j-1]+result[i-1][j])
    #     # 每行最后一个元素为 1
    #     row.append(1)
    #     result.append(row)
    
    ## 优化2：利用对称性优化
    result = [[1]]
    for i in range(1, numRows):
        # 创建一个长度为 i+1 的数组，首尾为1
        row = [1] * (i + 1)
        # 利用对称性，只需要计算前一半
        for j in range(1, (i + 1) // 2 + 1): #举例，第三行，i=2，stop 需要为 2 ｜ 第 4 行，i=3，stop 需要为 2
            row[j] = result[i-1][j-1] + result[i-1][j]
            row[i-j] = row[j]  # 对称位置的值相同
        result.append(row)

    return result