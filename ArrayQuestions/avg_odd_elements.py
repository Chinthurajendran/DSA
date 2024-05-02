def avg_even(arr):
    sum = 0
    count = 0
    for i in range(len(arr)):
        if arr[i]%2!=0:
            sum = sum +arr[i]
            count +=1
    if count>0:
        avg = sum/count
        return avg
    else:
        return "no odd element in array"

arr=[1,5,3,7,3]
result = avg_even(arr)
print(result)