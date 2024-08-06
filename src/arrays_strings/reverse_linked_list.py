"""206. Reverse Linked List
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Example 2:
    Input: head = [1,2]
    Output: [2,1]

    Example 3:
    Input: head = []
    Output: []

    Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

    Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from typing import Optional


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = new_node

    def print_list(self):
        if self.head is None:
            return "The list is empty"
        current = self.head
        itr = ''
        while current:
            itr += str(current.val) + ' -> '
            current = current.next

        print(itr)

    def linked_list(self):
        linked_lists = []
        if self.head is None:
            print("The list is empty")
        itr: Node = self.head
        while itr:
            linked_lists.append(itr.val)
            itr = itr.next

        return linked_lists

    def get_linked_list(self):
        node_lists = []
        if self.head is None:
            print("The list is empty")
        itr: Node = self.head
        while itr:
            node_lists.append(itr)
            itr = itr.next

        return node_lists


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = head
        itr = head
        print("Hello")
        if not itr:
            print("Empty node")

        while itr:
            new_node = Node(itr.val)
            if itr == head:
                new_node.next = None
            new_node.next = previous
            itr = itr.next
            previous = new_node


if __name__ == '__main__':
    # Example usage:
    linked_list = ListNode()
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_lists = linked_list.linked_list()
    print("linked_lists", linked_lists)
    print("get nodes", linked_list.get_linked_list())
    solution = Solution()
    solution.reverseList(head=linked_list.head)
