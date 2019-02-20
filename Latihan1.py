print("Program menampilkan bilangan acak yang lebih kecil dari 0.5")
print("")
print("Nama  : Danu Adiputra")
print("NIM   : 311810929")
print("Kelas : TI.18.B.2")
print("")
import random

jumlah = int(input("Masukkan jumlah N : "))
N = 0
for N in range(jumlah):
    N += 1
    i = random.uniform(0.0, 0.5)
    print("Data ke- ", N, "=>", i)
print("Selesai")