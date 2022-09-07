
#1. getSum adalah perintah untuk mendapatkan hasil jumlah seluruh angka. Bagaimana jika kita membutuhkan fungsi 
# getKali untuk mengalikan seluruh angka?

def getKali(myList):
    sum = 1
    for item in myList:
        sum = sum*item
    return sum

getKali([1,2,3,4])

#2. getSum adalah perintah untuk mendapatkan hasil jumlah seluruh angka. Bagaimana jika kita membutuhkan fungsi 
#  getBagi untuk membagikan seluruh angka?

 def getBagi(myList):
    sum = 48
    for item in myList:
        sum = sum/item
    return sum

getBagi([1,2,3,4])
