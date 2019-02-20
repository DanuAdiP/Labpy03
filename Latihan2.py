print("Nama  : Danu Adiputra")
print("NIM   : 311810929")
print("Kelas : TI.18.B.2")
print("")
print("Program menampilkan bilangan terbesar dan berhenti ketika mengetik angka 0")
max=0
while True:
    a=int(input("Masukkan bilangan = "))
    if max < a:
        max=a
    if a==0:
        break
print("Bilangan terbesarnya adalah : ",max)