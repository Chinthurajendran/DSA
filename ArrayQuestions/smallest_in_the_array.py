def smallest(arr):
    for i in arr:
        smallest = arr[0]
        if i < smallest:
            smallest = i
    return smallest

arr=[2,7,5,3,9]
print(min(arr))
result = smallest(arr)
print(result)