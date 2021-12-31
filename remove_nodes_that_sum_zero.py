#https://www.careercup.com/question?id=5717797377146880
from linked_list import Node,LinkedList

def remove_nodes_that_sum_zero(l1):
    cur = l1.head
    positive_nodes_sum, negative_nodes_sum = 0,0
    while cur:
        if cur.data >0 :
            positive_nodes_sum += cur.data
        elif cur.data <0:
            negative_nodes_sum += -(cur.data)
        
        cur = cur.next
    #print(positive_nodes_sum,negative_nodes_sum)
    


if __name__ == "__main__":  
    linkedList1 = LinkedList()
    
    linkedList1.push(1)
    linkedList1.push(3)
    linkedList1.push(5)
    linkedList1.push(-1)
    linkedList1.push(-3)
    linkedList1.push(-5)
    linkedList1.push(7)
    linkedList1.print_list()
    remove_nodes_that_sum_zero(linkedList1)
