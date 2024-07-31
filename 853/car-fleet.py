
## n -> num of cars away from starting mile 0
## all cars travelling to reach target
## two integer arrays, position, and speed of length n 


## sort 

def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    
    n: int = len(position)
    car_sets: list[tuple[int,int]] = []
    stack: list = []
    for i in range(n):
        car_sets.append((position[i], speed[i]))
        
    sorted_cars: list[tuple[int,int]] = sorted(car_sets, key=lambda x: x[0])
    print(sorted_cars)
    
    for i in range(n):
        time_to_dest: float = (target - sorted_cars[n-1-i][0]) / sorted_cars[n-1-i][1]
        if not stack:
            stack.append(sorted_cars[n-1-i])
        else:
            latest = stack[-1]
            time_to_dest_in_stack = (target - latest[0]) / latest[1]
            print(time_to_dest)
            print(time_to_dest_in_stack)
            if time_to_dest >  time_to_dest_in_stack:
                stack.append(sorted_cars[n-1-i])
                ##colliding 
    print(stack)
    return len(stack)
                

        
    
print(carFleet(target=12, position= [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]))