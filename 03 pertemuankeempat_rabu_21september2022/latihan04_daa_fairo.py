# -*- coding: utf-8 -*-
"""Latihan04_DAA_Fairo

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yu6tTBGzG3edbWVXW5zm0Xq00pHJFyTn

Latihan! Buat fungsi swap dengan menambahkan variabel ketiga bernama var3!
"""

var1 = 1
var2 = 2
var3 = 3
var1,var2,var3 = var3,var2,var1

print(var1,var2,var3)

"""Latihan! Urutkan deret bilangan di bawah ini menggunakan metode sorting bubble sort! [100,20,60,90,40,30,10]"""

def gelembung(list):
  elemenakhir = len(list)-1
  for x in range(elemenakhir,0,-1):
    for y in range(x):
      if list[y]>list[y+1]:
        list[y],list[y+1]=list[y+1],list[y]
  return list

list = [100,20,60,90,40,30,10]

list

gelembung(list)

"""Latihan! Urutkan deret bilangan di bawah ini menggunakan metode sorting insertion sort! [89,12,57,16,25,11,75]"""

def listinsert(num):
  for x in range(1,len(num)):
    y = x-1
    lanjut = num[x]

    while(num[y]>lanjut) and (y >=0):
      num[y+1] = num[y]
      y = y-1
    num[y+1] = lanjut
  return num

num = [89,12,57,16,25,11,75]
num

listinsert(num)
num

"""Latihan! Tentukan prosedur pengurutan deret secara ascending menggunakan metode sorting selection sort! [89,12,57,16,25]"""

def seleksi(list):
  for x in range(len(list)-1,0,-1):
    y = 0
    for z in range(1, x +1):
      if list[z]>list[y]:
        y = z
    list[x],list[y] = list[y],list[x]
  return list

list = [89,12,57,16,25]
list

seleksi(list)

"""Latihan! Cari "a" dari deret huruf di bawah ini menggunakan metode searching linear [y,u,i,w,o,a,q,u,j,p]"""

def search(list,item):
  idx = 0
  found = False

#match the value with each data element
  while idx < len(list) and found is False:
    if list[idx] == item:
      found = True
    else:
      idx = idx +1
  return found

list = ["y","u","i","w","o","a","q","u","j","p"]
print(search(list,"a"))

"""Latihan! Cari "a" dari deret huruf di bawah ini menggunakan metode searching binary search! [y,u,i,w,o,a,q,u,j,p]"""

def binary(list,item):
  pertama = 0
  akhir = len(list)-1
  found = False

  while pertama <= akhir and not found:
    mid = (pertama+akhir)//2
    if list[mid] == item:
      found = True
    else:
      if item < list[mid]:
        akhir =mid -1
      else:
        pertama = mid +1
  return found

list = ["y","u","i","w","o","a","q","u","j","p"]
sort_list = BubbleSort(list)
print(BinarySearch(list,"a"))

"""Latihan! Cari "u" dari deret huruf di bawah ini menggunakan metode searching interpolation search! [y,u,i,w,o,a,q,u,j,p]"""

def search(arr, K):
  kecil = 0 
  besar = len(arr) - 1

  while kecil <= besar and K >= arr[kecil] and K <= arr[besar]:
    probe = kecil + ((K - arr[kecil]) * (besar - kecil)) // (arr[besar] - arr[kecil])
    if arr[probe] == K:
      return True
    elif probe < K:
      kecil = probe + 1
    elif probe > K:
      besar = probe - 1
  return False

def inter(arr, K):
  arr.sort()
  sorted_arr = arr
  return search([ord(ch) for ch in sorted_arr], ord(K))

a = ["y","u","i","w","o","a","q","u","j","p"]
#print([ord(ch) for ch in a])
inter(a, "u")