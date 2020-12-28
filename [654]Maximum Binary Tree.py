# Given an integer array with no duplicates. A maximum tree building on this arr
# ay is defined as follow: 
# 
#  
#  The root is the maximum number in the array. 
#  The left subtree is the maximum tree constructed from left part subarray divi
# ded by the maximum number. 
#  The right subtree is the maximum tree constructed from right part subarray di
# vided by the maximum number. 
#  
# 
#  Construct the maximum tree by the given array and output the root node of thi
# s tree. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,2,1,6,0,5]
# Output: [6,3,5,null,2,0,null,null,1]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,1]
# Output: [3,null,2,null,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 1000 
#  0 <= nums[i] <= 1000 
#  All integers in nums are unique. 
#  
#  Related Topics Tree 
#  👍 2209 👎 262


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        max_num = self.find_max_num_in_array(nums)
        if max_num is None:
            return None
        left = self.constructMaximumBinaryTree(nums[0: nums.index(max_num)])
        right = self.constructMaximumBinaryTree(nums[nums.index(max_num) + 1::])
        root = TreeNode(val=max_num, left=left, right=right)
        return root

    @staticmethod
    def find_max_num_in_array(nums):
        if not nums:
            return None
        return max(nums)

        
# leetcode submit region end(Prohibit modification and deletion)
