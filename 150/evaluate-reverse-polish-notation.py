
def evalRPN(tokens: list[str]) -> int:
    
    
    ## loop through tokens
    ## start from the bottom
    ## check if it is a number, if it is, store it as value 1
    ## after a num there will always be an operand
    ## division towards 0 --> use float then transform to int
    if len(tokens) == 1:
        return int(tokens[0])
    stack: list = []
    t_v: int = 0

    for _, value in enumerate(tokens):
        if value not in ["-", "*", "/", "+"]:
            stack.append(int(value))
        else:
            v_1: int = stack.pop()
            v_2: int = stack.pop()
            if value == "/":
                t_v = int(v_2 / v_1)
            elif value == "*":
                t_v = int(v_2 * v_1)
            elif value == "+":
                t_v = int(v_2 + v_1)
            elif value == "-":
                t_v = int(v_2 - v_1)
            stack.append(t_v)
    return t_v
        
print(evalRPN(["18"]))
# print(evalRPN(["4","13","5","/","+"]))
# print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))