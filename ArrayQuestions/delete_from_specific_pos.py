def delete(arr):
    for i in range(len(arr)):
        if i == 4:
            del arr[i]
    return arr

def sec_delete(arr,index):
    del arr[index]
    return arr


arr = [2, 3, 4, 2, 3, 7]
print(arr)
index = 4

result = delete(arr)
result2=sec_delete(arr,index)

print(result)
print()
print(result2)
print()
