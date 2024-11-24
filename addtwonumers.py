# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Add two numbers represented by linked lists and return the result as a linked list.
        
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Initialize dummy head and carry variable
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both linked lists
        while l1 is not None or l2 is not None:
            # Extract values or use 0 if the node is None
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            
            # Calculate the sum and the carry
            total = carry + x + y
            carry = total // 10
            
            # Create a new node with the sum's unit digit
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes in the lists
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        # If there's a carry left, add a new node with that value
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the result list, starting from dummy_head.next
        return dummy_head.next
if __name__ == "__main__":
    solution=Solution()
    result=solution.addTwoNumbers(l1=[2,4,3],l2=[5,6,4])
    print(result)