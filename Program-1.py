print("-------- Program 1 --------")
print("Program perulangan sederhana")
print("")
print("Nama  : Danu Adiputra")
print("NIM   : 311810929")
print("Kelas : TI.18.B.2")
print("")
print("Catatan : ")
print("Laba perusahaan bulan ke- 1 dan 2 = 0%")
print("Laba perusahaan bulan ke- 3 dan 4 = 1%")
print("Laba perusahaan bulan ke- 5 sampai 7 = 5%")
print("Laba perusahaan bulan ke- 8 = 3%")

a=100000000
for x in range(1,9):
    if (x>=1and x<=2):
        b=a*0
        print("Laba bulan ke ",x," : ",b)
    if (x>=3and x<=4):
        c=a*0.1
        print("Laba bulan ke ",x," : ",c)
    if (x>=5 and x<=7):
        d=a*0.5
        print("Laba bulan ke ",x," : ",d)
    if (x==8):
        e=a*0.3
        print("Laba bulan ke ",x," : ",e)
total=b+b+c+c+d+d+d+e
print("Total laba yang didapat adalah : ",total)
