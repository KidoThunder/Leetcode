# Implement strStr(). 
# 
#  Return the index of the first occurrence of needle in haystack, or -1 if need
# le is not part of haystack. 
# 
#  Clarification: 
# 
#  What should we return when needle is an empty string? This is a great questio
# n to ask during an interview. 
# 
#  For the purpose of this problem, we will return 0 when needle is an empty str
# ing. This is consistent to C's strstr() and Java's indexOf(). 
# 
#  
#  Example 1: 
#  Input: haystack = "hello", needle = "ll"
# Output: 2
#  Example 2: 
#  Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#  Example 3: 
#  Input: haystack = "", needle = ""
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  0 <= haystack.length, needle.length <= 5 * 104 
#  haystack and needle consist of only lower-case English characters. 
#  
#  Related Topics Two Pointers String 
#  👍 1899 👎 2090


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        n = len(needle)

        i = 0
        while i <= len(haystack) - n:
            if haystack[i: i + n] == needle:
                return i
            i += 1

        return -1

# leetcode submit region end(Prohibit modification and deletion)
