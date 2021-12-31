import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data,sep=' ',end=' ')
            cur = cur.next
        print()

    def __str__(self):
        cur = self.head
        while cur:
            print(cur.data,sep=' ',end=' ')
            cur = cur.next
        print()
        return ""
        
    def reverse_list(self):
        cur = self.head
        if len(self)<2:
            return cur
        prev = None
        nextNode = None
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        self.head = prev

    def reverse_list_recursive(self):
        if len(self)<2:
            return self.head
        self.reverse_list_recursive_util(self.head,None)

    def reverse_list_recursive_util(self,cur,prev):
        if cur == None:
            return
        nextNode = cur.next
        cur.next = prev
        if nextNode == None:
            self.head = cur
        self.reverse_list_recursive_util(nextNode,cur)

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def sort(self,reverse = False):
        pass

    def remove(self,element=sys.maxsize):
        cur = self.head
        if element == sys.maxsize:
            return False
        while cur.next != None:
            #if its first element then update the head.
            if cur.data == element:
                self.head = cur.next
                return True
            
            if cur.next.data == element:
                #If last element is to be removed, then set None as current elenent's next
                cur.next = None if cur.next.next == None else cur.next.next
                return True
            cur = cur.next

        #element not found
        return False
        

    def pop(self,index=-1):
        cur = self.head
        count = 0
        if index<0:
            return False
        
        while cur.next != None:
            #if its first element then update the head.
            if index == 0:
                self.head = cur.next
                return True
            if count == index-1:
                #If last element is to be removed, then set None as current elenent's next
                cur.next = None if cur.next.next == None else cur.next.next
                return True
            count += 1
            cur = cur.next
            
        #Index not in range
        return False
    
if __name__ == "__main__":  
    linkedList = LinkedList()
    linkedList.push(8)
    linkedList.push(6)
    linkedList.push(3)
    linkedList.push(4)
    #linkedList.print_list()
    #linkedList.reverse_list()
    #linkedList.print_list()
    #linkedList.reverse_list_recursive()
    #linkedList.print_list()
    #print(linkedList.remove(9))
    linkedList.print_list()
    linkedList.sort()
