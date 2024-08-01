class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def reverse_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

def insertion_sort(linked_list):
    sorted_list = LinkedList()
    current = linked_list.head
    while current:
        next_node = current.next
        sorted_list = insert_sorted(sorted_list, current.value)
        current = next_node
    linked_list.head = sorted_list.head

def insert_sorted(sorted_list, value):
    new_node = Node(value)
    if not sorted_list.head or sorted_list.head.value >= value:
        new_node.next = sorted_list.head
        sorted_list.head = new_node
    else:
        current = sorted_list.head
        while current.next and current.next.value < value:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    return sorted_list

def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    current1, current2 = list1.head, list2.head

    while current1 and current2:
        if current1.value < current2.value:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    if current1:
        tail.next = current1
    if current2:
        tail.next = current2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Створення і заповнення списків
list1 = LinkedList()
list1.append(5)
list1.append(4)
list1.append(3)

list2 = LinkedList()
list2.append(8)
list2.append(7)
list2.append(6)

# Реверсування списку
reverse_list(list1)
print("Reversed List 1:")
list1.print_list()

# Сортування списку
insertion_sort(list1)
print("Sorted List 1:")
list1.print_list()

# Об'єднання двох відсортованих списків
insertion_sort(list2)
print("Sorted List 2:")
list2.print_list()

merged_list = merge_sorted_lists(list1, list2)
print("Merged List:")
merged_list.print_list()