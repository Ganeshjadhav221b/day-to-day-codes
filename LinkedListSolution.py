from linked_list import Node,LinkedList
            
def merge_two_sorted_lists(l1,l2):
    newList = LinkedList()
    cur1 = l1.head
    cur2 = l2.head
    while True:
        if cur1 == None:
            while cur2:
                newList.push(cur2.data)
                cur2 = cur2.next
            break
        if cur2 == None:
            while cur1:
                newList.push(cur1.data)
                cur1 = cur1.next
            break
        if cur1.data<cur2.data:
            newList.push(cur1.data)
            cur1 = cur1.next
        else:
            newList.push(cur2.data)
            cur2 = cur2.next
        
    return newList

def detect_loop(l1):
    pointer1 = l1.head
    pointer2 = l1.head.next
    while True:
        if pointer1 is pointer2:
            return True
        if pointer1.next == None or pointer2 == None or pointer2.next == None:
            return False
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
        
    return False

def remove_loop(l1):
    if not detect_loop(l1):
        print("List had no loop.")
        return l1
    pointer1 = l1.head
    pointer2 = l1.head.next
    while True:
        if pointer1.next is pointer2.next:
            pointer1.next = None
            return l1
        if pointer1.next == None or pointer2 == None or pointer2.next == None:
            return l1
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
    return l1

def kth_node_from_end(l1,k=0):
    ##Approach uses length
    cur = l1.head
    for i in range(len(l1)-k):
        cur = cur.next
    return cur.data

    ##Approach uses 2 pointers
    ##Maintain two pointers – reference pointer and main pointer. Initialize both reference and main pointers to head.
    #First, move the reference pointer to k nodes from head.
    #Now move both pointers one by one until the reference pointer reaches the end.
    #Now the main pointer will point to nth node from the end. Return the main pointer.


def mid_of_list(l1):
    cur1 = l1.head
    cur2 = l1.head
    while True:
        if cur2.next == None or cur2.next.next == None:
            return cur1.data
        cur1 = cur1.next
        cur2 = cur2.next.next
    return cur.data

def delete_mid_of_list(l1):
    cur1 = l1.head
    cur2 = l1.head
    while True:
        if cur2.next == None or cur2.next.next == None:
            #cur1 is the middle node. To remove it, we just replace the data from the next node and remove the next node
            cur1.data = cur1.next.data
            cur1.next = cur1.next.next
            return l1
        cur1 = cur1.next
        cur2 = cur2.next.next
    return l1



def remove_duplicates_from_list(l1):
    pass


if __name__ == "__main__":  
    linkedList1 = LinkedList()
    
    linkedList2 = LinkedList()

    linkedList1.push(1)
    linkedList1.push(5)
    linkedList1.push(3)
    #linkedList1.push(7)

    linkedList2.push(4)
    linkedList2.push(2)
    linkedList2.push(6)

    #linkedList1.print_list()
    #linkedList2.print_list()

    newList = merge_two_sorted_lists(linkedList1, linkedList2)
    newList.print_list()
    #[1,3,5]
    linkedList1.head.next.next.next = linkedList1.head
    #print(detect_loop(linkedList2))
    #linkedList1.print_list()
    linkedList1 = remove_loop(linkedList1)
    #print(detect_loop(linkedList1))
    #linkedList1.print_list()
    #print("kth_node_from_end",kth_node_from_end(newList,2))
    #print("Middle of list",mid_of_list(newList))
    list_with_mid_removed = delete_mid_of_list(newList)
    #print("List after removing the middle element",list_with_mid_removed)
    list_with_no_duplicates = remove_duplicates_from_list(sorted_list)
    
    
