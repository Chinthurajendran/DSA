def insert_array(arr,poss,elm):
    for i in range(len(arr)):
        if i == poss:
            arr[i] = elm
    return arr

arr = [3,4,5,2,5,7]
poss = 4
elm = 1
result=insert_array(arr,poss,elm)
print(arr)
