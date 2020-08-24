# 1558. 得到目标数组的最少函数调用次数
"""
给你一个与 nums 大小相同且初始值全为 0 的数组 arr ，请你调用以上函数得到整数数组 nums 。
请你返回将 arr 变成 nums 的最少函数调用次数。
答案保证在 32 位有符号整数以内。

示例 1：

输入：nums = [1,5]
输出：5
解释：给第二个数加 1 ：[0, 0] 变成 [0, 1] （1 次操作）。
将所有数字乘以 2 ：[0, 1] -> [0, 2] -> [0, 4] （2 次操作）。
给两个数字都加 1 ：[0, 4] -> [1, 4] -> [1, 5] （2 次操作）。
总操作次数为：1 + 2 + 2 = 5 。
示例 2：

输入：nums = [2,2]
输出：3
解释：给两个数字都加 1 ：[0, 0] -> [0, 1] -> [1, 1] （2 次操作）。
将所有数字乘以 2 ： [1, 1] -> [2, 2] （1 次操作）。
总操作次数为： 2 + 1 = 3 。
示例 3：

输入：nums = [4,2,5]
输出：6
解释：（初始）[0,0,0] -> [1,0,0] -> [1,0,1] -> [2,0,2] -> [2,1,2] -> [4,2,4] -> [4,2,5] （nums 数组）。
示例 4：

输入：nums = [3,2,2,4]
输出：7
示例 5：

输入：nums = [2,4,8,16]
输出：8
 

提示：

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-numbers-of-function-calls-to-make-target-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 逆向处理，遇到奇数则减一，遇到偶数则除以二
# 减一操作是可独立操作，每次操作计数加一
# 除数操作是统一操作，全部操作完再计数加一
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            for i in range(0, len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    count += 1
            # 最后一步只能从 1 减到 0，因此判断减完后是否已经全部为零
            # 判断标志，如果数字全部都是零，直接跳出循环
            flag = False
            for i in range(0, len(nums)):
                if nums[i] != 0:
                    flag = True
                nums[i] /= 2
            if not flag:
                break
            count += 1
        return count
