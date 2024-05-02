class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    tail = dummy
    
    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    
    if head1 is not None:
        tail.next = head1
    elif head2 is not None:
        tail.next = head2
    
    return dummy.next

def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

# Example usage:
# Creating two sorted linked lists
list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

# Merging the sorted lists
merged_head = merge_sorted_lists(list1, list2)

# Printing the merged list
print_list(merged_head)
