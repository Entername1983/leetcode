
## if open bracket, add to queue
## if closed bracket, pop item from queue, check if matches if doesn't match return false
## if closed bracket and queue is empty return false
## at the end check if queue is empty

def isValid(s: str) -> bool:
    pairings: dict = {'(':')', '{':'}', '[':']'}
    open_brackets: list = ['(', '{', '[']
    stack: list = []
    for p in s:
        if p in open_brackets:
            stack.append(p)
        else:
            if not stack:
                return False
            latest_item: str = stack.pop()
            if p != pairings[latest_item]:
                return False
    if stack:
        return False
    return True

isValid("()")
print("next")
isValid("()[]{}")
print("next")
isValid("]")
