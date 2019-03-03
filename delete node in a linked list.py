class __Node__(self):
    self.data = data 
    self.next = next 

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        self.head = None 
        current = self.head 
        previous = None 
        while current and current != node:
            previous = current 
            current = current.next 
            
            if previous == None:
                self.head = current.next 
            else:
                previous.next = current.next 
