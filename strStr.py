"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        elif needle in haystack:
            # 假设 haystack 长度是10，needle 长度是3
            # 那么 haystack 匹配 neddle 的子字符串，其首字母最迟出现在第7位
            # 即下面循环中 i 的最大值
            for i in range(len(haystack)-len(needle)+1): 
                 if haystack[i:i+len(needle)] == needle:
                     return i
        else:
            return -1

test = Solution().strStr('mississippi','issip')
print(test)
