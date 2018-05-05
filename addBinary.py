"""
"""
class Solution(object):		
	def addBinary(self, a, b):
		import math
		
		i = 0
		sum_a = 0 # 保存二进制a转换为十进制后的值
		sum_b = 0
		a = int(a) # 因为输入的是二进制字符串
		b = int(b)
		while a:
		    dec = a % 2 # 取出最后一个数字
		    sum_a += dec * pow(2, i) # 将每一位二进制数与其位权相乘，然后相加就得到了十进制数
		    a = a // 10  # 是两数相除，留下整数部分，除去最后一位
		    i += 1

		i = 0
		while b:
		    dec = b % 2
		    sum_b += dec * pow(2, i)
		    b = b // 10
		    i += 1

		sum = sum_a + sum_b 
		temp = []
		result = ''

		while sum:
		    dec = sum % 2
		    sum = sum // 2
		    temp.append(dec)
		while temp:
		    result += str(temp.pop())

		result = int(result)
		return result

test = Solution().addBinary(1001,100)
print(test)
