# Given an array of integers nums and an integer target, return indices of the t
# wo numbers such that they add up to target. 
# 
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 105 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  Only one valid answer exists. 
#  
#  Related Topics Array Hash Table 
#  👍 17531 👎 627


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for index, num in enumerate(nums):
        #     for _index, _num in enumerate(nums[index + 1:]):
        #         if target - num == _num:
        #             return index, index + _index + 1

        seen = {}
        for index, num in enumerate(nums):
            _target = target - num
            if _target in seen:
                return seen[_target], index
            seen[num] = index

        # leetcode submit region end(Prohibit modification and deletion)


s = Solution()
res = s.twoSum([2, 7, 11, 15], 9)
print(res)
