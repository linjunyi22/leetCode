"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.

统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:
输入: "Hello, my name is John"
输出: 5

"""


class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len([i for i in s.split(' ') if i != ''])

test = Solution().countSegments('Hello world')
print(test)
