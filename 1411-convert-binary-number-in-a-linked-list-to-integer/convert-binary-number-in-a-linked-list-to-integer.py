class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        result=0
        temp=head
        while temp:
            result=result*2+temp.val
            temp=temp.next
        return result
        