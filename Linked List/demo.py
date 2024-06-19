def binnery(list,key):
    if len(list) > 1:
        low = 0 
        hight = len(list)-1
        found =  False

        while low <= hight and not found:
            mid = (low+hight)//2

            if key  == list[mid]:
                found = True
            elif key > list[mid]:
                low = mid+1
            else:
                hight =  mid -1
        
        if found ==  True:
            print("true")
        else:
            print("Fasle")


list=[2,6,3,5,7,23,56,78,88,22,100]
key = 1
binnery(list,key)
