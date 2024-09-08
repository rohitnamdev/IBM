import math
def find_LCM(arr):
    a, b = arr
    return abs(a * b) // math.gcd(a, b)

def find_lcm_of_adjacent(arr): 
    res = set()
    for i in range(len(arr)-1):
        r = find_LCM(arr[i:i+2])
        # print(arr[i:i+2])
        res.add(r)
    return res
arr = [5,7,3,2,9,12]
res = find_lcm_of_adjacent(arr)
print(max(res))