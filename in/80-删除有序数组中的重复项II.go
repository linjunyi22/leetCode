// 80. 删除有序数组中的重复项 II
// 难度：中等

// 给你一个有序数组 nums ，请你原地删除重复出现的元素，使得出现次数超过两次的元素只出现两次，
// 返回删除后数组的新长度。
//
// 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

// 解题思路：
// 1. 由于数组已经排序，所以相同的元素一定是相邻的
// 2. 使用快慢指针法：
//    - slow 指针表示处理完成的数组的最后一个位置
//    - fast 指针用于遍历数组
// 3. 关键点是判断当前数字是否应该保留：
//    - 如果当前数字和它前两个位置的数字不同，说明当前数字最多只出现过一次，可以保留
//    - 通过比较 nums[slow-2] 和 nums[fast] 来判断是否需要保留当前数字
// 4. 时间复杂度 O(n)，空间复杂度 O(1)

func removeDuplicates(nums []int) int {
	if len(nums) <= 2 {
		return len(nums)
	}

	slow, fast := 2, 2
	for fast < len(nums) {
		if nums[slow-2] != nums[fast] {
			nums[slow] = nums[fast]
			slow++
		}
		fast++
	}
	return slow
}

// 示例：
// 输入：nums = [1,1,1,2,2,3]
// 输出：5, nums = [1,1,2,2,3]
// 解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。
// 不需要考虑数组中超出新长度后面的元素。

// 进阶版本：允许最多保留k个相同元素
// 思路：
// 1. 基本思路与保留2个元素相同，只是将比较点从 slow-2 改为 slow-k
// 2. 初始化时，slow 和 fast 都从索引 k 开始
// 3. 其他逻辑保持不变
func removeDuplicatesK(nums []int, k int) int {
	if len(nums) <= k {
		return len(nums)
	}

	slow, fast := k, k
	for fast < len(nums) {
		if nums[slow-k] != nums[fast] {
			nums[slow] = nums[fast]
			slow++
		}
		fast++
	}
	return slow
}

// 示例：
// 输入：nums = [1,1,1,1,2,2,2,3], k = 3
// 输出：7, nums = [1,1,1,2,2,2,3]
// 解释：允许最多保留3个相同元素，所以1和2都保留3个，3保留1个，总长度为7
