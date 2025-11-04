# 无重复字符的最长子串

def lengthOfLongestSubstring(s: str) -> int:
    # set记录当前子串
    str_set=set()

    # 左指针
    left=0
    # 最长子串统计
    max_length=0

    # 扩张窗口，右指针遍历整个字符串
    for right in range(len(s)):
        # 收缩判断
        # 右指针包含元素在set中，窗口需要收缩，直到重复元素去除
        while s[right] in str_set:
            str_set.remove(s[left])
            left+=1

        # 扩张窗口    
        str_set.add(s[right])

        # 更新统计指标
        max_length = max(max_length,right-left+1)
   
    return max_length

# 测试用例
if __name__ == "__main__":
    # 示例 1
    s1 = "abcabcbb"
    print(f"输入: {s1}")
    print(f"输出: {lengthOfLongestSubstring(s1)}")  # 应该输出 3
    
    # 示例 2
    s2 = "bbbbb"
    print(f"输入: {s2}")
    print(f"输出: {lengthOfLongestSubstring(s2)}")  # 应该输出 1
    
    # 示例 3
    s3 = "pwwkew"
    print(f"输入: {s3}")
    print(f"输出: {lengthOfLongestSubstring(s3)}")  # 应该输出 3
    
    # 边界情况测试
    s4 = ""
    print(f"输入: {s4}")
    print(f"输出: {lengthOfLongestSubstring(s4)}")  # 应该输出 0
    
    # 单个字符
    s5 = "a"
    print(f"输入: {s5}")
    print(f"输出: {lengthOfLongestSubstring(s5)}")  # 应该输出 1