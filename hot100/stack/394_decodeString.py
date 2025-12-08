# 字符串解码
'''
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的
    - 原始数据不包含数字
    - 数字只表示重复次数
'''

class Solution:
    def decodeString(self, s: str) -> str:
        '''
        将[看作进入一个更深层次的开始
        把]看作当前层次的结束，并返回上一层
        当进入新层次时，保存上一层状态
        返回上一层的时候，将保存的状态恢复，并加上新层次的东西
        '''
        stack= []
        res= '' # 记录当前层解码的字符串
        multi=0

        for char in s:
            if '0'<= char <='9':
                multi = multi*10 + int(char) # 1️⃣ 处理数字
            elif char=='[':
                # 当前倍数，上一层字符串结果，入栈
                stack.append((multi,res))
                multi=0
                res=''
            elif char==']': #解码并更新res
                last_multi,last_res = stack.pop()
                res=last_res+last_multi*res # 执行解码，更新res
            else:
                res+=char # 记录当前层字符
        
        
        return res