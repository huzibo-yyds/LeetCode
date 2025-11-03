# 字母异位词分组
# 哈希表 ｜ #
# 时间复杂度：O(N * K * log K)，其中 N 是字符串数量，K 是字符串的最大长度
# 空间复杂度：O(N * K)

def groupAnagrams(strs:list[str])->list[list[str]]:
    # 键、值（为列表）
    anagram_groups={}

    for s in strs:
        # 将排序后的字符串作为键
        key=''.join(sorted(s))

        # 若不存在键，则创建对应列表
        if key not in anagram_groups:
            anagram_groups[key]=[]

        # 将当前字符串添加到对应分组
        anagram_groups[key].append(s)
    
    return(list(anagram_groups.values()))

# 测试用例
if __name__ == "__main__":
    # 示例 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs1))  # [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    # 示例 2
    strs2 = [""]
    print(groupAnagrams(strs2))  # [[""]]
    
    # 示例 3
    strs3 = ["a"]
    print(groupAnagrams(strs3))  # [["a"]]