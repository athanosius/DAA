from operator import truediv

import numpy as np

def searchBinary(myList,item):
    first = 0
    last = len(myList)-1
    foundFlag = False
    while( first<=last and not foundFlag):
        mid = (first +last)//2
        if myList[mid] == item :
            foundFlag = True
        
        else:
            if item < myList[mid] :
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag

searchBinary([9,8,10,100,1000,2000,3000],10) #True 
searchBinary([9,8,10,100,1000,2000,3000],5) #False
