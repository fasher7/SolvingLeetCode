class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        current1 = head
        current2 = head
        while current2 and current2.next:
            current1 = current1.next
            current2 = current2.next.next
            if current1 == current2:
                return True
        return False

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

list = create_linked_list([3, 2, 0, -4, -2])
print_linked_list(list)
hs = Solution()
isCycle = hs.hasCycle(list)
print(isCycle)