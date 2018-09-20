"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:
输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 

注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        new_s = []
        for i in s:
        	new_s.append(i[::-1])
        result = ' '.join(new_s)
       	return result

test = Solution().reverseWords("Let's take LeetCode contest")
print(test)
