# Roman numerals are represented by seven different symbols: I, V, X, L, C, D an
# d M. 
# 
#  
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000 
# 
#  For example, two is written as II in Roman numeral, just two one's added toge
# ther. Twelve is written as, XII, which is simply X + II. The number twenty seven
#  is written as XXVII, which is XX + V + II. 
# 
#  Roman numerals are usually written largest to smallest from left to right. Ho
# wever, the numeral for four is not IIII. Instead, the number four is written as 
# IV. Because the one is before the five we subtract it making four. The same prin
# ciple applies to the number nine, which is written as IX. There are six instance
# s where subtraction is used: 
# 
#  
#  I can be placed before V (5) and X (10) to make 4 and 9. 
#  X can be placed before L (50) and C (100) to make 40 and 90. 
#  C can be placed before D (500) and M (1000) to make 400 and 900. 
#  
# 
#  Given a roman numeral, convert it to an integer. Input is guaranteed to be wi
# thin the range from 1 to 3999. 
# 
#  Example 1: 
# 
#  
# Input: "III"
# Output: 3 
# 
#  Example 2: 
# 
#  
# Input: "IV"
# Output: 4 
# 
#  Example 3: 
# 
#  
# Input: "IX"
# Output: 9 
# 
#  Example 4: 
# 
#  
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#  
# 
#  Example 5: 
# 
#  
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4. 
#  Related Topics Math String 
#  👍 2250 👎 3517


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    ROMA_LIST = [
        "M", "D", "C", "L", "X", "V", "I"
    ]
    ROMA_HASH = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        for i, r in enumerate(s):
            if i + 1 < len(s):
                now_p = self.ROMA_LIST.index(r)
                next_p = self.ROMA_LIST.index(s[i + 1])
                if r == s[i + 1]:
                    number += self.ROMA_HASH[r]
                elif now_p < next_p:
                    number += self.ROMA_HASH[r]
                elif now_p > next_p:
                    number -= self.ROMA_HASH[r]
            else:
                number += self.ROMA_HASH[r]
        return number


# leetcode submit region end(Prohibit modification and deletion)
