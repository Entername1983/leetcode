


# def largestRectangleArea(heights: list[int]) -> int:
    
#     if len(heights) == 1:
#         return heights[0]
    
#     stack: list[tuple[int, int]] = [(heights[0], 0)] ## min height, index
#     max_v: int = 0
#     ## if a < b continue old one + new stack
#     ## if a = b continue old one
#     ## if a > b stop stack, count total and append + new stack
    
#     for i, value in enumerate(heights):
#         if i == 0: 
#             continue ## ignore first one since already in stack
#         print(f"i: {i}, value {value}, stack {stack}")
#         top_stack: tuple[int, int] = stack[-1]

#         ## if top of stack h > value
#         while stack and top_stack[0] > value:
#             ## calculate the max
#             print(top_stack, i)
#             max_l = top_stack[0] * (i - top_stack[1] )
#             print(max_l)
#             max_v = max(max_v, max_l)
#             stack.pop()
#             stack.append((value, top_stack[1]))
#         if top_stack[0] == value:
#             continue
        
#         while stack and stack[-1][0] < value:
#             max_l = top_stack[0] * (i  - top_stack[1] + 1)
#             max_v = max(max_v, max_l)


#             stack.pop()
#         ## if top of stack h < value


#     return max_v
    
    
    
    
def largestRectangleArea(heights: list[int]) -> int:
    maxArea: int = 0
    
    stack = []
    
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h: ## while there are items in the stack and the top of the stack is superior to the next value
             index, height = stack.pop()  ## remove the top of the stack
             maxArea = max(maxArea, height * (i - index)) ## compare its index to the last index we are at, which gives us the width
             start = index ## set start for next item the last item poppeds index (work our way backwards)
        stack.append((start, h))   ## append item where new value is smaller than one stored in stack
    
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    
    return maxArea
    # orig_stack: list = [heights[0]]
    
    # print("before recursion")
    # def findPerms(array: list, stack: list) -> None:  ## finds permutations, when done appends to perms
    #     print("array", array, "stack", stack)
    #     if not array:
    #         max_value = stack[-1] * len(stack)
    #         perms.append(max_value)
    #         print("Found a max value, appending!!!", max_value)
    #     else:
    #         last_item = stack[-1]
    #         print("top of stack", stack[-1])
    #         if last_item < array[0]:
    #             ## create new stack 
    #             new_stack = [array[0]]
    #             findPerms(array[1:], new_stack)
                
    #             ## continue old one
    #             stack.append(last_item) ## we are just appending the last item because it has a lower value, we just care about the smallest block
    #             findPerms(array[1:], stack)
                
    #         elif last_item == array[0]:
    #             stack.append(last_item)
    #             findPerms(array[1:], stack)
                
    #         else:
    #             ## we reached the max value of a stack.  Append 
    #             max_value = stack[-1] * len(stack)
    #             perms.append(max_value)
    #             print("Found a max value, appending", max_value)
                
    #             stack.append(array[0])
    #             findPerms(array[1:], stack)
                    
    # findPerms(heights[1:], orig_stack)
    # print(perms)
    # perms.sort()
    
    # return perms[-1]



# print(largestRectangleArea([2,1,5,6,2,3]), '10')
print(largestRectangleArea([2,1,2]), '3')
