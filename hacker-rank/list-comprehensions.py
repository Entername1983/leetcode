## x, y, z -> 3 axis in a cuboid
## n -> sum of elements x, y, z to avoid


def cuboid_thing(x: int, y: int, z: int, n: int) -> list:
    
    # i = 0
    # the_list = []
    # while i <= x:
    #     j = 0
    #     while j <= y:
    #         k = 0
    #         while k <= z:
    #             if i + j + k != n:
    #                 the_list.append([i, j, k])
    #             k += 1
    #         j += 1
    #     i += 1
    # print(the_list)
    the_list = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(the_list)
cuboid_thing(1, 1, 2, 3)