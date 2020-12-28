from datetime import datetime
from llist import sllist, sllistnode


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

        # Print the linked list

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while laste.next:
            laste = laste.next
        laste.next = NewNode

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if HeadVal is not None:
            if HeadVal.data == Removekey:
                self.head = HeadVal.next
                HeadVal = None
                return

        while HeadVal is not None:
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if HeadVal == None:
            return

        prev.next = HeadVal.next

        HeadVal = None


input_number = [8, 5, 3, 1, 9, 2, 6, 4, 7]
test = [3, 8, 9, 1, 2, 5, 4, 6, 7]


def move(s_list: sllist):
    current_node = s_list.popleft()
    picked = []
    for _ in range(3):
        picked.append(s_list.popleft())
    found = False
    val = current_node
    while not found:
        if val == 1:
            val = max(s_list)
        else:
            val -= 1
        if val not in picked:
            destination_node = 0
            node = s_list.first
            while destination_node == 0:
                if node.value == val:
                    destination_node = node
                else:
                    node = node.next
            found = True
    # print(current_node, picked, destination_node)
    for val in picked:
        x = sllistnode(val)
        s_list.insertnodeafter(x, destination_node)
        destination_node = x
    s_list.append(current_node)
    return s_list


def run(list_in, times):
    s_list = sllist(list_in)
    s_list.extendright([i for i in range(max(list_in) + 1, pow(10, 6) + 1)])
    max_val = pow(10, 6)
    past = datetime.now()
    current_node = s_list.first
    for i in range(times):
        if i % pow(10, 2) == 0:
            print(i)
            print((datetime.now() - past).total_seconds())
            past = datetime.now()
        cur_val = current_node.value
        picked = []
        for _ in range(3):
            node = current_node.next
            picked.append(s_list.remove(node))
        found = False
        while not found:
            if cur_val == 1:
                cur_val = max_val
            else:
                cur_val -= 1
            if cur_val not in picked:
                next_node = current_node.next
                while next_node.value != cur_val:
                    next_node = next_node.next
                    if next_node is None:
                        next_node = s_list.first
                found = True
        for item in picked:
            s_list.insertnodeafter(sllistnode(item), next_node)
        current_node = current_node.next

    return 0


def run2(list_in, times):
    s_list = sllist(list_in)
    s_list.extendright([i for i in range(max(list_in) + 1, pow(10, 6) + 1)])
    past = datetime.now()
    for i in range(times):
        if i % pow(10, 2) == 0:
            print(i)
            print((datetime.now() - past).total_seconds())
            past = datetime.now()
        s_list = move(s_list)


    return 0


run(test, pow(10, 3))
