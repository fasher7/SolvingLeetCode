class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            self = ListNode(list1.val)
            list1 = list1.next
        else:
            self = ListNode(list2.val)
            list2 = list2.next
        current = self
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        else:
            current.next = list2
        return self
    
def create_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

nums1 = [1, 2, 4]
nums2 = [1, 3, 4]

list1 = create_linked_list(nums1)
list2 = create_linked_list(nums2)
ml = Solution()
list3 = ml.mergeTwoLists(list1, list2)

print("Merged Linked List:")
print_linked_list(list3)