# Given a 32-bit signed integer, reverse digits of an integer. 
# 
#  Example 1: 
# 
#  
# Input: 123
# Output: 321
#  
# 
#  Example 2: 
# 
#  
# Input: -123
# Output: -321
#  
# 
#  Example 3: 
# 
#  
# Input: 120
# Output: 21
#  
# 
#  Note: 
# Assume we are dealing with an environment which could only store integers with
# in the 32-bit signed integer range: [−231, 231 − 1]. For the purpose of this pro
# blem, assume that your function returns 0 when the reversed integer overflows. 
#  Related Topics Math 
#  👍 3420 👎 5383


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = False
        if x < 0:
            x *= -1
            sign = True

        reversed_int = 0
        while x > 0:
            reversed_int = reversed_int * 10 + x % 10
            x = int(x / 10)

        if not reversed_int <= 2 ** 31 - 1:
            return 0
        if sign:
            reversed_int *= -1
        return reversed_int


if __name__ == '__main__':
    o = Solution()
    x = o.reverse(1200)
    print(x)


# leetcode submit region end(Prohibit modification and deletion)
