# Determine whether an integer is a palindrome. An integer is a palindrome when 
# it reads the same backward as forward. 
# 
#  Example 1: 
# 
#  
# Input: 121
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes
#  121-. Therefore it is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#  
# 
#  Follow up: 
# 
#  Coud you solve it without converting the integer to a string? 
#  Related Topics Math 
#  👍 2332 👎 1551


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x % 10 == 0 and x != 0:
            return False

        reversed_x = 0
        while x > reversed_x:
            reversed_x = reversed_x * 10 + x % 10
            x = int(x / 10)
        return reversed_x == x or int(reversed_x / 10) == x


if __name__ == '__main__':
    s = Solution()
    r = s.isPalindrome(10)
    print(r)
        
# leetcode submit region end(Prohibit modification and deletion)
