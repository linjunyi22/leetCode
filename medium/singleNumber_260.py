"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 没能想到 O(1)的空间复杂度解法
        # 官方题解使用位运算达到 O(1)的空间复杂度
        # 详情可查阅此链接 https://leetcode-cn.com/problems/single-number-iii/solution/zhi-chu-xian-yi-ci-de-shu-zi-iii-by-leetcode/
        m = {}
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        res = []
        for i in m:
            if m[i] == 1:
                res.append(i)
                if len(res) == 2:
                    return res
        return res
