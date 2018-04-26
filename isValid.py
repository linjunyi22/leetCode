"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
"""

"""
原来这道题目用栈可以解决，一开始我还想找规律，发现每个配对的下标都是2的倍数+1，自己想的方向偏了...

先把字符串的一些干扰的空格去掉，保证只剩下各种括号或者空字符串。
然后遍历每个括号，遇到左括号就压到栈里面，如果遇到右括号，就把括号跟栈顶元素比较，
如果配对上了，那就可以消除栈顶元素，否则，直接返回 False。最后判断下栈是否空，空则有效，不空则无效。
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip().replace(' ','') # 去除干扰
        if s == '': # 空字符串，有效
        	return True
        
        stack_box = [] # 栈容器
        data_box = {'(':')','[':']','{':'}'} # 括号字典

        for i in list(s):
        	if i in data_box:
        		stack_box.append(i) # 碰到左括号，压栈
        	else:
        		if len(stack_box) == 0:
        			return False
        		else:
        			if data_box.get(stack_box[-1]) != i: #匹配栈顶左括号跟目前右括号是否匹配
        				return False
        			else:
        				del stack_box[-1] # 匹配上就删除栈顶元素

        if len(stack_box) != 0: #判断下栈是否空
        	return False
        return True

test = Solution().isValid('){([)]()')
print(test)






