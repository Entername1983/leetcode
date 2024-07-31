
## return: number of days we have to wait after ith day to get a warmer temperature.
## if no warmer day return 0
## temps always positive, always at least one value
### didn't need to store the temperature, only the index in the stack (can get the temp by using index and temperatures array)


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    
    res: list[int] = [0 for _ in range(len(temperatures))]
    stack: list[tuple] = []
    
    for i in range(len(temperatures) - 1):
        stack.append((temperatures[i], i))
        while stack and stack[-1][0] < temperatures[i + 1]:
            temp = stack.pop()
            res[temp[1]] = i + 1 - temp[1]
    return res

print("-----------------------------")
print(dailyTemperatures([73,74,75,71,69,72,76,73]), "[1,1,4,2,1,1,0,0]")
print("-----------------------------")
print(dailyTemperatures([30,40,50,60]), " [1,1,1,0]")
print("-----------------------------")
print(dailyTemperatures([30,60,90]), " [1,1,0]")
print("-----------------------------")
