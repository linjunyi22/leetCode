"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指由字母组成，但不包含任何空格的字符串。
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_split = s.strip().split(' ') # 清除字符串两边的空格并切割成列表
        if len(s_split[-1]) > 0: # 如果有单词存在，最后一个单词长度必然大于零，如果没有，则表明整个字符串都是空格
            return len(s_split[-1])
        else:
            return 0