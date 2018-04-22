"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

验证给定的字符串是否为数字。

例如:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        try:
            if isinstance(float(s),float) or isinstance(int(s),int):
                return True
        except Exception as e:
            return False

test = Solution().isNumber('234 .  543')
print(test)
