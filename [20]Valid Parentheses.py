# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
#  determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  
# 
#  Note that an empty string is also considered valid. 
# 
#  Example 1: 
# 
#  
# Input: "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: "(]"
# Output: false
#  
# 
#  Example 4: 
# 
#  
# Input: "([)]"
# Output: false
#  
# 
#  Example 5: 
# 
#  
# Input: "{[]}"
# Output: true
#  
#  Related Topics String Stack 
#  👍 5314 👎 227


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    BRACKETS = {
        "{": "}",
        "(": ")",
        "[": "]"
    }

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_stack = BracketStack()
        for char in s:
            if len(bracket_stack) > 0 and bracket_stack.top() in self.BRACKETS.keys():
                if self.BRACKETS[bracket_stack.top()] == char:
                    bracket_stack.pop()
                    continue
            bracket_stack.push(char)

        if len(bracket_stack) > 0:
            return False
        return True


class BracketStack(object):
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def top(self):
        return self.list[-1]

    def pop(self):
        return self.list.pop()

    def push(self, obj):
        return self.list.append(obj)


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.isValid("(([]){})")
print(res)
