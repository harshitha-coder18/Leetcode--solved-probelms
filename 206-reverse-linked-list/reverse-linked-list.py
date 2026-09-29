class Solution:
    def reverseList(self, head):
        prev = None
        temp = head
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        return prev