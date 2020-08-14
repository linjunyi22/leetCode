# 239. 滑动窗口最大值
"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

进阶：
你能在线性时间复杂度内解决此题吗？

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        elif k == 1:
            return nums
        elif k == len(nums):
            return [max(nums)]

        max_num = max(nums[0:k])
        res = [max_num]

        # 开始滑动窗口，比较左边值与最大值的关系，然后求出新的最大值
        n = len(nums)
        for i in range(1, n - k + 1):
            left_num = nums[i - 1]
            right_num = nums[i + k - 1]

            # 左侧值比最大值小，则最大值仍在新窗口中，直接将最大值和新值 right_num 比较
            if left_num < max_num:
                max_num = max(max_num, right_num)
            # 左侧值比最大值大，则左侧值就是最大值，新窗口需要重新计算最大值
            else:
                max_num = max(nums[i:i + k])
            res.append(max_num)
        return res
