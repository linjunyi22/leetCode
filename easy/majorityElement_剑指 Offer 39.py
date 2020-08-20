# 剑指 Offer 39. 数组中出现次数超过一半的数字
"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

限制：

1 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 字典存储数字的计数，每次循环作判断即可，时间复杂度 O(n)，空间复杂度 O(n/2)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        n = len(nums) // 2
        for i in nums:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
            if m[i] > n:
                return i


# 摩尔投票法，首次看到，比较巧妙的解法
# 记录当前值和一个计数值，如果遇到相同的值，则将计数加一，否则减一，如果计数值为零，则重新计数
# 因为遇到不同值时计数会减一，则相当于数之间的抵消，所以当计数为零时需要重新计数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 1
        for i in nums[1:]:
            if count == 0:
                res = res[i]
                count = 1
            elif res == nums[i]:
                res += 1
            else:
                res -= 1
        return res
