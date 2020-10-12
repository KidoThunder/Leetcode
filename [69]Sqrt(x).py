# Implement int sqrt(int x). 
# 
#  Compute and return the square root of x, where x is guaranteed to be a non-ne
# gative integer. 
# 
#  Since the return type is an integer, the decimal digits are truncated and onl
# y the integer part of the result is returned. 
# 
#  Example 1: 
# 
#  
# Input: 4
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.
#  
#  Related Topics Math Binary Search 
#  👍 1325 👎 1900


# leetcode submit region begin(Prohibit modification and deletion)\
from math import floor, ceil


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left = 1
        right = x

        while left < right:
            mid = left + floor((right - left) / 2)

            if mid * mid == x:
                return int(mid)
            elif mid * mid > x:
                right = mid
            else:
                left = mid + 1
        return int(left - 1)

# leetcode submit region end(Prohibit modification and deletion)


a = 4
s = Solution()
res = s.mySqrt(a)
print(res)
