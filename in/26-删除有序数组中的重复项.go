package in

// removeDuplicates 删除有序数组中的重复项
// 题目要求：
// 1. 给定一个有序数组，要求原地删除重复出现的元素
// 2. 返回删除后数组的新长度
// 3. 不要使用额外的数组空间，必须在原地修改输入数组
//
// 解题思路：
// 1. 使用哈希表记录已出现的数字，避免重复
//   - 选择 map[int]struct{} 而不是 map[int]bool 可以节省内存
//   - struct{} 不占用任何空间
//
// 2. 使用双指针技术：
//   - result 指针：指向要填入的位置，同时表示新数组的长度
//   - i 指针：用于遍历原数组，查找不重复的元素
//
// 3. 具体步骤：
//   - 遍历数组，对于每个元素 nums[i]：
//   - 检查是否在哈希表中存在
//   - 如果不存在，说明是新元素：
//     a. 将其放入 result 位置
//     b. result 指针向前移动
//     c. 将该元素加入哈希表
//   - 如果存在，则跳过该元素
//
// 4. 最终 result 的值就是新数组的长度
//
// 优化空间：
// 由于输入数组已经排序，实际上可以不使用哈希表
// 可以直接比较相邻元素是否相同，可以将空间复杂度优化到 O(1)
//
// 时间复杂度：O(n)，其中 n 是数组长度
// 空间复杂度：O(n)，使用了哈希表存储不重复的元素
func removeDuplicates(nums []int) int {
	hashTable := make(map[int]struct{})
	result := 0
	for i := 0; i < len(nums); i++ {
		_, ok := hashTable[nums[i]]
		if !ok {
			nums[result] = nums[i]
			result++
			hashTable[nums[i]] = struct{}{}
		}
	}
	return result
}

// removeDuplicatesOptimized 删除有序数组中的重复项的优化解法
// 题目要求：
// 1. 给定一个有序数组，要求原地删除重复出现的元素
// 2. 返回删除后数组的新长度
// 3. 不要使用额外的数组空间，必须在原地修改输入数组
//
// 优化解题思路：
// 1. 由于输入数组已经排序，相同的元素一定是相邻的
// 2. 使用快慢双指针：
//   - slow 指针：指向当前无重复数组的最后一个位置
//   - fast 指针：用于遍历数组寻找不重复的元素
//
// 3. 具体步骤：
//   - 特殊情况处理：如果数组长度为 0，直接返回 0
//   - 初始化 slow = 0，表示第一个元素一定是不重复的
//   - fast 从索引 1 开始遍历数组：
//     a. 比较 nums[fast] 和 nums[slow] 是否相同
//     b. 如果不同，说明遇到新元素：
//   - slow 指针前进一位
//   - 将 fast 指向的新元素复制到 slow 位置
//     c. 如果相同，则 fast 继续前进
//
// 4. 最终 slow + 1 就是新数组的长度
//
// 优化说明：
// 1. 不需要使用额外的哈希表，空间复杂度降到 O(1)
// 2. 由于数组有序，通过比较相邻元素即可判断重复
// 3. 只需要一次遍历，时间复杂度保持 O(n)
//
// 时间复杂度：O(n)，其中 n 是数组长度
// 空间复杂度：O(1)，只使用了常数额外空间
func removeDuplicatesOptimized(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	slow := 0
	for fast := 1; fast < len(nums); fast++ {
		if nums[fast] != nums[slow] {
			slow++
			nums[slow] = nums[fast]
		}
	}
	return slow + 1
}
