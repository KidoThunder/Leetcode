# Write a function to find the longest common prefix string amongst an array of 
# strings. 
# 
#  If there is no common prefix, return an empty string "". 
# 
#  Example 1: 
# 
#  
# Input: ["flower","flow","flight"]
# Output: "fl"
#  
# 
#  Example 2: 
# 
#  
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#  
# 
#  Note: 
# 
#  All given inputs are in lowercase letters a-z. 
#  Related Topics String 
#  👍 2600 👎 1864


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not any(strs):
            return ""

        strings = sorted(strs, key=lambda x: len(x))
        common_prefixes = strings[0]
        result_prefix = str()

        for i, common_prefix in enumerate(common_prefixes):
            res = self.get_common_prefix(strings, common_prefix, i)
            if res is not None:
                result_prefix += res
                continue
            else:
                return result_prefix
        return result_prefix

    def get_common_prefix(self, strings, common_prefix, times):
        for s in strings:
            if not s[times:].startswith(common_prefix):
                return None
        return common_prefix


# leetcode submit region end(Prohibit modification and deletion)
r = Solution()
sr = r.longestCommonPrefix(["a"])
print(sr)
