
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
        
        
class Solution:
    #Not sure if this is necessary, description says node lists are given but examples only show lists    
    def initializeLinkedList(self, list1: Optional[list], list2: Optional[list]) ->  Optional[list[ListNode]]:
        list_nodes: list[ListNode] = []
        for raw_list in [list1, list2]:
            i: int = len(raw_list) - 1
            next_node = None
            while i >= 0:
                new_node = ListNode(raw_list[i], next_node)
                next_node = new_node
                i -= 1
            list_nodes.append(new_node)
        return list_nodes  
    
    
    ## 1 2 4, 1 3 4
    ## compare ptr_1 and ptr_2
    ## ptr_1 val and 2 are the same, so insert ptr_two as the next value 
    ## list_1 becomes 1 1 3 4, list 2 is 2 4
    ## compare ptr_1_val (which is now the second 1 ) to 2, two is larget so goes to next for ptr_1_val
    ## list becomes 1 1 2 4, list 2 is 3 4
    ## compare 
    ## traverse through the first list
    ## compare the value each pointer.  The lowest value gets inserted as next 
    

    
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ## if there is only one list, return that list
        if not list1:
            return list2
        if not list2:
            return list1
        ## keeping track of the head of the merged list as wont be able to return to it
        new_list: ListNode = ListNode(val=None, next=None)
        head_new_list = new_list
        ## head of new list only needs to be initialized
        while True:
            ## if list 1 value is lower than list 2 value, then list 1 value should go next
            ## move the list 1 head to the next item in list
            ## if there are no more items in the list, we can add teh remaining list 2 items
            print(list1.val, list2.val)
            if list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
                if list1 is None:
                    new_list = new_list.next
                    new_list.next = list2
                    break
            else:
                new_list.next = list2
                list2 = list2.next
                if list2 is None:
                    new_list = new_list.next
                    new_list.next = list1
                    break
            new_list = new_list.next
            
            
        current_node = head_new_list
        while current_node:
            print(current_node.val)
            current_node = current_node.next
        return head_new_list.next
            
            
            
solution = Solution()
list_nodes = solution.initializeLinkedList(list1 = [1,2,4], list2 = [1,3, 4])
solution.mergeTwoLists(list_nodes[0], list_nodes[1])