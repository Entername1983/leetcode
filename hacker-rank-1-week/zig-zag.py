
# k = (n+1)/2
# first k elements increasing, last deecreasing

def findZigZagSequence(a: list[int], n: int):
    
    a.sort()
    print("a", a)
    print("n", n)
    mid = int((n + 1)/2) - 1 ## finding the mid point

    a[mid], a[n-1] = a[n-1], a[mid] ## taking highest point and putting it in the middle.  FIRST ERROR
    print("list again", a)

    st = mid + 1 ## guess this is start-  Think there is no need to add + 1 here SECOND ERROR

    ed = n - 2
    
    print("start", st, "end", ed)
    while(st <= ed): ## this will run forever as they are both being incremented at the same time
        print("looping")
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

findZigZagSequence([1, 2, 3, 4, 5, 6, 7], 7)