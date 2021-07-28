# Given an integer array nums, find the contiguous subarray (containing at least
#  one number) which has the largest sum and return its sum. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [5,4,-1,7,8]
# Output: 23
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  -105 <= nums[i] <= 105 
#  
# 
#  
# Follow up: If you have figured out the O(n) solution, try coding another solut
# ion using the divide and conquer approach, which is more subtle. Related Topics 
# Array Divide and Conquer Dynamic Programming 
#  👍 13232 👎 629


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = None
        current_num = 0

        for num in nums:
            if current_num + num <= num:
                current_num = num
            else:
                current_num += num

            if total_sum is None or total_sum <= current_num:
                total_sum = current_num
        return total_sum


s = Solution()
r = s.maxSubArray([1])
print(r)

# leetcode submit region end(Prohibit modification and deletion)
