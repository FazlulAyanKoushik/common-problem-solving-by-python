"""
Instructions:
    Write a method to find and return the middle node in the Linked List WITHOUT using the length attribute.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return new_node

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        return new_node

    def find_middle_node(self):
        """
        This method uses two pointers, slow and fast, and advances them at different speeds through the list.
        The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
        By the time the fast pointer reaches the end of the list, the slow pointer will be at the middle node.

        return: middle node or None
        """
        if self.head is None or self.head.next.next is None:
            print("Short Linked List")
            return None

        slow = self.head.next
        fast = self.head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(11)
    linked_list.append(12)
    linked_list.append(13)
    linked_list.append(21)
    linked_list.append(19)
    linked_list.append(31)
    linked_list.append(41)

    middle_node = linked_list.find_middle_node()
    if middle_node is not None:
        print(middle_node.value)
