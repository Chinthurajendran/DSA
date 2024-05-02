def largest(arr):
    return max(arr)

def sec_largest(arr):
    largests = 0
    for i in arr:
        if i > largests:
            largests = i
    return largests
arr=[2,7,5,3,9]
result = largest(arr)
print(result)
result2 = sec_largest(arr)
print(result2)