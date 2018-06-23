"""
Write a function that takes a string as input and returns the string reversed.

请编写一个函数，其功能是将输入的字符串反转过来。

示例：
输入：s = "hello"
返回："olleh"

"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = reversed(list(s))
        s = ''.join(s)
        return s

test = Solution().reverseString('abcdefg')
print(test)
