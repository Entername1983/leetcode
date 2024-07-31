## N petrol pumps in a circle
## pumps are numbered 0 to N - 1
## know the amoutn of petrol a pump has
## the distance from that pump to the next
## input list of lists
## distance can travel == gas in the tank + gas at the station
## if i > N --> i = 0

def truckTour(petrolpumps):
    print(petrolpumps)
    visited = 0
    gas = 0
    N = len(petrolpumps)
    for i, value in enumerate(petrolpumps):
        gas = 0
        visited = 0
        print(f"station index {i}, gas at station {value[0]}, needed{value[1]}")
        start = i
        while True: ## while we haven't visited all the pumps
            print("start", start)
            if start == N:
                start = 0
            gas += petrolpumps[start][0]
            if gas < petrolpumps[start][1]: ## can't get to the next station, reset everything and exit this loop
                print("not enought gas")

                break
            else: ## we can make it to the next station
                print("speed ahead")
                print("visited")
                start += 1
                visited += 1
            if visited == N:
                print(f"started from {i}, succesfully")
                return i


print(truckTour([[6352, 12787], [13129, 17300], [72374, 38672], [97868, 99865], [58225, 28774]]))
