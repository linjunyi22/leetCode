"""
Given two strings representing two complex numbers.
You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

给定两个表示复数的字符串。
返回表示它们乘积的字符串。注意，根据定义 i2 = -1 。

示例 1:
输入: "1+1i", "1+1i"
输出: "0+2i"
解释: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。

示例 2:
输入: "1+-1i", "1+-1i"
输出: "0+-2i"
解释: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 

注意:
1.输入字符串不包含额外的空格。
2.输入字符串将以 a+bi 的形式给出，其中整数 a 和 b 的范围均在 [-100, 100] 之间。输出也应当符合这种形式。

"""


class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        list_a = a.split('+')
        list_b = b.split('+')

        int_0 = int(list_a[0]) * int(list_b[0])
        int_1 = int(list_a[0]) * int(list_b[1][:-1])
        int_2 = int(list_a[1][:-1]) * int(list_b[0])
        int_3 = int(list_a[1][:-1]) * int(list_b[1][:-1]) * -1

        return '+'.join([str(int_0 + int_3),str(int_1 + int_2) + 'i'])

test = Solution().complexNumberMultiply('1+1i','1+-1i')
print(test)
