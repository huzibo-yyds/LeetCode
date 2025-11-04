# 找到字符串中所有字母异位词
# 字母异位词是通过重新排列不同单词或短语的字母而形成的单词或短语，并使用所有原字母一次。

def findAnagrams_m(s: str, p: str) -> list[int]:
    '''
        1- 每次都list排序比较，时间复杂度高
    '''
    index_list=[]
    left=0
    subs_list=[]
    p_list=list(p)

    for right in range(len(s)):

        subs_list.append(s[right])

        if sorted(subs_list) == sorted(p_list): # 复杂度过高
            index_list.append(left)

        # print(subs_list)

        if len(subs_list) == len(p_list):
            subs_list.pop(0)
            left+=1

    return index_list


def findAnagrams(s: str, p: str) -> list[int]:
    # 只包含小写字母
    if len(s) < len(p):
        return []
    
    index_list = []

    # ⭐ 使用哈希表比较
    # 使用字符频率数组替代列表排序
    p_count = [0] * 26
    window_count = [0] * 26    

    # 统计目标字符串p的字符频率
    for char in p:
        p_count[ord(char) - ord('a')] += 1
    
    # 滑动窗口遍历字符串s
    for i in range(len(s)):
        # 将右边界字符加入窗口
        window_count[ord(s[i]) - ord('a')] += 1
        
        # 当窗口大小超过p的长度时，移动左边界|窗口长度固定为p长度
        if i >= len(p):
            window_count[ord(s[i - len(p)]) - ord('a')] -= 1
        
        # 比较窗口字符频率与目标字符频率
        if window_count == p_count:
            index_list.append(i - len(p) + 1)
    
    return index_list


# 测试用例
if __name__ == "__main__":
    # 示例 1
    s1 = "cbaebabacd"
    p1 = "abc"
    print(f"输入: {s1}")
    print(f"输入: {p1}")

    # a=["a",'b','c']
    # b=['b','c','a']
    # print(sorted(a))
    # print(sorted(b))

    print(f"输出: {findAnagrams(s1,p1)}")
