arr  = [6,1,2,3,4,5]
ans = arr[0]
for i in arr:
    if ans>i:
        ans=i
def findMinimum(arr):
    ans = arr[0]
    for i in arr:
        if ans>i: ans=i
    return ans
print(findMinimum(arr))
