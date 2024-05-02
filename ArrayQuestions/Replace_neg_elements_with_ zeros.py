def neg_elements(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i]=0
    return arr

arr=[2,-2,3,-4,2]
reuslt = neg_elements(arr)
print(reuslt)

def replace_negative(arr):
    for i in range(len(arr)):
        if arr[i]< 0 :
            arr[i]=0
    return arr

arr=[2,-2,3,-4,2]
result=replace_negative(arr)
print(result)