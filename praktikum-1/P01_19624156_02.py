# NIM/Nama : 19624156/Riantama Putra
# Tanggal : 17/10/2024
# Deskripsi : Problem 02

N = int(input("Masukkan Nilai N: "))
T = int(input("Masukkan Nilai T: "))

Leo = int(input("Masukkan waktu lari Tuan Leo: "))
Deb = int(input("Masukkan waktu lari Nona Deb: "))
Sal = int(input("Masukkan waktu lari Nona Sal: "))

jumlah_terkualifikasi = 0
if Leo <=T:
    jumlah_terkualifikasi +=1
if Deb <=T:
    jumlah_terkualifikasi +=1
if Sal <=T:
    jumlah_terkualifikasi +=1

if jumlah_terkualifikasi > 0:
    hadiah = N / jumlah_terkualifikasi
    print(f"Terdapat {jumlah_terkualifikasi} peserta yang terkualifikasi dan masing-masing akan mendapatkan {hadiah:.0f} dollar kompeng.")
else:
    print("Tidak ada peserta yang terkualifikasi.")
