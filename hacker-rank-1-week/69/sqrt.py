## give non integer x 
## return square root of x, rounded down to nearest integer
## integer should be non negative
## can't use built in exponent function or operator


# 0 1 2 3 4 5 6 7 8  --> m = 4   4^2 --> 16  so we look for the square root lower  start stays the same, end = 4
# 0 1 2 3 4          --> m = 2   2^2 --> 4   so we look for the square root higher start = 2, end says the same
#       3 4 
#       2

# looking for 1 
# 0 1
# if end - start == 1:
# if end * end == 1 return end
# else return start
def mySqrt(x: int) -> int:
    ## take midway point in range --> call it m.  
    ## square it call it m^2:
    #### if equal to x --> return that value
    #### if superior to x --> set m as the new end of the range
    #### if inferior to x --> set m as the new start of the range
    
    start: int = 0
    end: int = x
    while start < end:
        if end - start == 1:
            if end * end == x:
                return end
            else:
                return start
        m: int = (end - start) // 2 + start ## find middle point rounded down
        m_2: int = m * m
        if m_2 == x:
            return m
        elif m_2 > x:
            end = m
        elif m_2 < x:
            start = m
    return x
    
print(mySqrt(1), "1")

print(mySqrt(0), "0")

print(mySqrt(8), "2")

print(mySqrt(4), "2")