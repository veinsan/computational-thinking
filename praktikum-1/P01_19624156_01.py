# NIM/Nama : 19624156/Riantama Putra
# Tanggal : 17/10/2024
# Deskripsi : Problem 01

A = int(input("Masukkan nilai kuis pertama: "))
B = int(input("Masukkan nilai kuis kedua: "))
C = int(input("Masukkan nilai kuis ketiga: "))

N = (A+B+C)/3

if (N >= 80):
    print ("Tuan Leo mendapatkan nilai Lulus Memuaskan.")
elif (N>=70):
    print ("Tuan Leo mendapatkan nilai Lulus.")
else:
    print("Tuan Leo mendapatkan nilai Tidak Lulus.")
