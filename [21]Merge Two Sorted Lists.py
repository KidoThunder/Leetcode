# Merge two sorted linked lists and return it as a new sorted list. The new list
#  should be made by splicing together the nodes of the first two lists. 
# 
#  Example: 
# 
#  
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#  
#  Related Topics Linked List 
#  👍 4590 👎 610


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# leetcode submit region end(Prohibit modification and deletion)
