class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):

    # Sanity Checks
    if ((not llist_1) or (not llist_1.head)) and ((not llist_2) or (not llist_2.head)):
        return set()

    if (not llist_1) or (not llist_1.head):
        return add_nodes_to_set(llist_2.head)

    if (not llist_2) or (not llist_2.head):
        return add_nodes_to_set(llist_1.head)

    res = set()  # The result set
    list1_runner = llist_1.head
    list2_runner = llist_2.head

    # If we use inner function, we'll save time spent in the union operation but then it'd need to be implemented twice
    # Once for union and once for intersection
    # Choosing to sacrifice a bit of time efficiency (still keeping the time complexity still linear)
    # for 'Do Not Repeat Code' principle

    # Time complexity is O(n+m) where n and m are the size of llist1 and llist2 respectively.
    # Space complexity is O(1) as no additional space is needed.

    # def _add_nodes(runner):
    #     nonlocal res
    #     while runner:
    #         res.add(runner.value)
    #         runner = runner.next

    res = res.union(add_nodes_to_set(list1_runner))
    res = res.union(add_nodes_to_set(list2_runner))
    return res


def add_nodes_to_set(runner):
    res = set()
    while runner:
        res.add(runner.value)
        runner = runner.next
    return res

def intersection(llist_1, llist_2):

    # Sanity checks
    if (not llist_1) or (not llist_1.head) or (not llist_2) or (not llist_2.head):
        return set()

    # We could have gotten the size of both linked lists and chosen to create elements_set with smaller element
    # so as to improve space efficiency
    # But looking at the code getting size would have made the code a bit slower as size() iterates through
    # entire linked list.
    # A workaround would be to include a size variable in linkedlist that increases/decreases on adding/removing a node
    # If we have a scenario that one list is significantly longer than the other one to the point that
    # one of them cannot be stored in memory, then storing elements from the smaller list would make sense

    # Time complexity is O(n+m) where n and m are the size of llist1 and llist2 respectively.
    # Space Complexity is O(n) where n is the size of llist1

    list1_elements_set = add_nodes_to_set(llist_1.head)
    res = set()
    list2_runner = llist_2.head
    while list2_runner:
        if list2_runner.value in list1_elements_set:
            res.add(list2_runner.value)
        list2_runner = list2_runner.next

    return res


# Test case 1

linked_list_01 = None
linked_list_02 = LinkedList()

print(union(linked_list_01,linked_list_02))
# set()

print(intersection(linked_list_01,linked_list_02))
# set()

# Test case 2

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2))
# {32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21}

print(intersection(linked_list_1,linked_list_2))
# {4, 21, 6}

# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4))
# {65, 2, 35, 3, 4, 6, 1, 7, 8, 9, 11, 21, 23}

print (intersection(linked_list_3,linked_list_4))
# set()