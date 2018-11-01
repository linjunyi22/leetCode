"""
Implement atoi which converts a string to an integer.

实现 atoi，将字符串转为整数。
该函数首先根据需要丢弃任意多的空格字符，直到找到第一个非空格字符为止。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。
当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。
若函数不能执行有效的转换，返回 0。

说明：
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。如果数值超过可表示的范围，则返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        res = re.findall(r"^[\+\-]?\d+",str.strip())

        if res !=[]:
            if int(res[0]) > (2**31-1):
                return (2**31-1)
            if int(res[0]) < (-2**31):
                return (-2**31)
            return int(res[0])
        else:
            return 0

test = Solution().myAtoi("-abc")
print(test)
