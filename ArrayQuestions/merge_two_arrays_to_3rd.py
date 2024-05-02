def merge(arr1,arr2):
    arr1.extend(arr2)
    return arr1

arr1 = [1,2,3,4]
arr2 = [5,6,7,8]
result = merge(arr1,arr2)
print(result)

