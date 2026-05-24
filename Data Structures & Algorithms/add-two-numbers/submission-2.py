class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)

        dummy1.next = l1
        dummy2.next = l2 

        lA = dummy1
        lB = dummy2

        #list1 value
        val1 = 0
        place = 1
        while lA.next: 
            lA = lA.next
            val1 += place * lA.val
            place*=10
           
        #list2Value
        val2 = 0
        place = 1
        while lB.next: 
            lB = lB.next
            val2 += place * lB.val
            place*=10
        
        print(val1)
        print(val2)

        sum = val1+val2


            
        if sum == 0:
            return ListNode(0)

        head = ListNode(0)
        curr = head
        while sum > 0:
            digit = sum % 10
            sum = sum // 10
            curr.next = ListNode(digit)
            curr = curr.next
        
        return head.next