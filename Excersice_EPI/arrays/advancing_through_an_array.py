def can_reach_end(a):
    furthest_reached_so_far, last_index = 0, len(a)-1
    i = 0
    while i <= furthest_reached_so_far and furthest_reached_so_far < last_index:
        furthest_reached_so_far = max(furthest_reached_so_far, a[i]+i)
        i += 1
    return furthest_reached_so_far >= last_index

a = [4,4,0,0,0,6,7,8]
a1 = [3,3,1,0,2,0,1]
a2 = [3,2,0,0,2,0,1]
print(can_reach_end(a))