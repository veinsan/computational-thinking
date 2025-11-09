# NIM/Nama : 19624156/Riantama Putra
# Tanggal : 31/10/2024
# Deskripsi : Problem 01

n = int(input("Masukkan banyak data: "))

luas = [0] * n
for i in range (n):
    luas[i] = int(input(f"Masukkan luas tanah ke-{i+1}: "))

min = int(input("Tentukan luas tanah minimum: "))

kicik = None

for l in luas:
    if l >= min:
        if kicik is None or l < kicik:
            kicik = l

if kicik is None:
    print(f"Tuan Leo tidak dapat membangun rumah.")
else:
    print(f"Luas tanah terkecil yang dapat dipilih adalah {kicik}.")