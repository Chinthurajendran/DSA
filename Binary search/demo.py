def binnery_search(list,key):
    if len(list) >1:
        low = 0
        hight = len(list)-1
        found = False
        while list[low] < list[hight] and not found:
            mid = (low+hight)//2
            if key ==  list[mid]:
                found = True
            elif key > list[mid]:
                low = mid+1
            else:
                hight = mid-1
    if found == True:
        print('Found')
    else:
        print('not found')
        
list = [1,2,5,48,0,8]
key = 1
binnery_search(list,key)
