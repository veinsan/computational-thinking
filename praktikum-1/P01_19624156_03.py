# NIM/Nama : 19624156/Riantama Putra
# Tanggal : 17/10/2024
# Deskripsi : Problem 03

jumlah_digit = int(input("Masukkan jumlah digit harga: "))
harga = input("Masukkan harga: ")

angka1 = int(input("Masukkan posisi angka pertama yang akan ditukar: ")) - 1
angka2 = int(input("Masukkan posisi angka kedua yang akan ditukar: ")) - 1

valid = True
count = 0
for char in harga:
    count += 1

if count != jumlah_digit or (harga[0] == '0' and count > 1):
    valid = False

if valid:
    if angka1 < 0 or angka1 >= jumlah_digit or angka2 < 0 or angka2 >= jumlah_digit:
        print("Harga tidak valid")
    else:
        harga_list = [harga[i] for i in range(count)]
        
        harga_list[angka1], harga_list[angka2] = harga_list[angka2], harga_list[angka1]

        harga_baru = ""
        for char in harga_list:
            harga_baru += char

        print("Harga setelah diperbaiki:", harga_baru)
else:
    print("Masukan harga tidak valid")

