class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    #Insertion at Start
    def InsertAtStart(self, data):
        temp = Node(data)
        
        if self.head is None:
            self.head = temp
            return
        temp.next = self.head
        self.head = temp

    #Inserting Anywhere        
    def InsertAtMiddle(self, previous, data):
        if previous is None:
            print("Previous Element is not in LinkedList")
            return
        new_node = Node(data)
        new_node.next = previous.next
        previous.next = new_node
     
    #Inserting at End  
    def InsertAtEnd(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
            
        last.next = new_node
    
    #Deletion of LinkedList(Deleting a given key)
    def Deletion(self,data):
        temp = self.head
        
        if temp is not None:
            if temp.item == data:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if temp.item == data:
                break
            prev = temp
            temp = temp.next
            
        if temp == None:
            return
        
        prev.next = temp.next
        temp = None
        
    #Deletion of LinkedList(Deletion on given position)
    def Deletion1(self,pos):
        if self.head == None:
            return
        temp = self.head
        
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(pos - 1):
            temp = temp.next
            if temp == None:
                break
        
        if temp is None:
            return
        if temp.next is None:
            return
        
        next = temp.next.next
        
        temp.next = None
        temp.next = next
    
    #Printing LinkedList    
    def PrintLinkedList(self):
        temp = self.head
        while temp:
            print(temp.item)
            temp = temp.next
            
    #Function to delete a LinkedList
    def DeleteLinkedList(self):
        current = self.head
        
        while current:
            prev = current.next
            del current.item
            current = prev
            
        print("LinkedList Deleted")
        
    #Function to Find Length of Linked list
    def Length(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        print("Length = ",count)
        
    #Search an Element in Linked list
    def Search(self,data):
        temp = self.head
        
        while temp != None:
            if temp.item == data:
                return "Element is Present"
            temp = temp.next
        return False
        
l1 = LinkedList()
l1.head = Node(1)
second = Node(2)
third = Node(3)
l1.head.next = second
second.next = third
print("Before Inserting")
l1.PrintLinkedList()
print("After Inserting")
l1.InsertAtEnd(5)
l1.InsertAtStart(5)
l1.PrintLinkedList()
print("After Deletion")
l1.Deletion(3)
l1.PrintLinkedList()
print("After deletion using position")
l1.Deletion1(3)
l1.PrintLinkedList()
l1.Length()
print(l1.Search(2))
