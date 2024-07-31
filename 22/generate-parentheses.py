def generateParenthesis(n: int) -> list[str]:
    
    ## n: pair of parenthesis
    ## return all correct combinations of parenthesis
    ## 
    
    ## loop through for i in range of n
    p_list: list[str] = []
    
    for i in range(n - 1):
        if i == 0:
            p_list.append("(")
        else:
            p_list.append(p_list[i-1])