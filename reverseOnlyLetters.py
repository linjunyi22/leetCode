"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：
输入："ab-cd"
输出："dc-ba"

示例 2：
输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

示例 3：
输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"

提示：
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S 中不包含 \ or "
"""


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        tmp = []
        for i in S[::-1]:
            if i.isalpha():
                tmp.append(i)

        listS = list(S)
        for j in range(len(listS)):
            if listS[j].isalpha():
                listS[j] = tmp.pop(0)
        return ''.join(listS)

test = Solution().reverseOnlyLetters("a-bC-dEf-ghIj")
print(test)
