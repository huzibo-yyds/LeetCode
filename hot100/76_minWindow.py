#  最小覆盖子串
# 返回s中包含t的最小子串，如果不满足返回空串

def minWindow(s: str, t: str) -> str:
    if not t or not s or len(s)<len(t):
        return ""

    # 使用hash表记录字符频率
    need={} # 1️⃣ 哈希表1，用来统计t中信息
    for char in t:
        need[char]=need.get(char,0) + 1
        # .get() # Return the value for key if key is in the dictionary, else default.

    # 滑动窗口相关变量
    left,right=0,0
    window = {} # 2️⃣ 哈希表2，统计当前窗口信息

    # 最小覆盖字串的起始位置与长度
    start = 0
    min_len=float('inf')

    # 记录窗口中已经满足need条件的字符种类数
    valid=0 

    while right < len(s):
        c=s[right]
        right+=1

        # 窗口内字符统计
        if c in need:
            window[c]=window.get(c,0)+1
            if window[c] == need[c]:
                valid+=1

        # 满足覆盖时，窗口收缩
        while valid==len(need):
            if right-left<min_len:
                start = left
                min_len = right - left
            
            d=s[left]
            left+=1

            if d in  need:
                if window[d]==need[d]:
                    valid-=1
                window[d]-=1
    
    return "" if min_len==float('inf') else s[start:start+min_len]








if __name__ == "__main__":
    s1="ADOBECODEBANC"
    t1 = "ABC"
    print(minWindow(s1,t1)) # BANC

    s2="ab"
    t2 = "a"
    print(minWindow(s2,t2)) # a