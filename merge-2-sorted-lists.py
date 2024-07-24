
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
        if not list1:
            return list2
        if not list2:
            return list1
        ptr_one: ListNode = list1
        ptr_two: ListNode = list2
        initial_check = False
        while ptr_one.next is not None and ptr_two.next is not None:
            if initial_check is False:
                if ptr_one.val >= ptr_two.val:
                    head_ptr = ptr_one
                else:
                    head_ptr = ptr_two
            initial_check = True
            if ptr_one.val > ptr_two.val:
                print("ptr one larger or equal to ptr two")
                temp_head = ptr_two.next
                ptr_two.next = ptr_one
                ptr_one = temp_head
                print(f"pointer one value {ptr_one.val}, pointer two {ptr_two.val}")
            else:
                print("ptr 2 smaller tahn 1")
                temp_head = ptr_one.next
                ptr_one.next = ptr_two
                ptr_two = temp_head
                print(f"pointer one value {ptr_one.val}, pointer two {ptr_two.val}")
        print(head_ptr)
        return head_ptr

solution = Solution()
list_nodes = solution.initializeLinkedList(list1 = [1,2,4], list2 = [1,3,4])
solution.mergeTwoLists(list_nodes[0], list_nodes[1])