"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

示例 1：
输入: "Hello"
输出: "hello"

示例 2：
输入: "here"
输出: "here"

示例 3：
输入: "LOVELY"
输出: "lovely"
"""


# 内部库函数
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


# 利用 ascii 码实现
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        LOWER = [chr(i) for i in range(ord('a'),ord('z')+1)]
        UPPER = [chr(i) for i in range(ord('A'),ord('Z')+1)]
        str_d = {x:y for x,y in zip(UPPER,LOWER)}

        str_l = list(str)
        for i in range(len(str_l)):
        	if 65 <= ord(str_l[i]) <= 90:
        		str_l[i] = str_d[str_l[i]]

        return ''.join(str_l)


test = Solution().toLowerCase('HEllo')
print(test)
