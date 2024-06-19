def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
selection_sort(arr)
print("Sorted array is:", arr)