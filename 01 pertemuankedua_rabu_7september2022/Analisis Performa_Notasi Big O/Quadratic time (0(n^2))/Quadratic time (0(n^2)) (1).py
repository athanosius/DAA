
#1. Buatlah suatu fungsi untuk membagi 2 himpunan angka, jika getSum untuk menjumlahkan angka!

def getBagi(myList):
  sum = 50
  for row in myList:
    for item in row:
      sum /= item
  return sum

getBagi([[3],[9]])