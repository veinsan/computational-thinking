# NIM/Nama : 19624156/Riantama Putra
# Tanggal : 31/10/2024
# Deskripsi : Problem 03

nomor = int(input("Masukkan Nomor Urut: "))
x = int(input("Masukkan batas bawah (x): "))
y = int(input("Masukkan batas atas (y): "))

def prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

faktor_prima = []
for i in range(2, nomor + 1):
    if nomor % i == 0 and prima(i):
        faktor_prima.append(i)

valid = False
valid_ids = []

for i in range(x, y + 1):
    iya = False
    for faktor in faktor_prima:
        if i % faktor == 0:
            iya = True
            break
    if iya:
        valid_ids.append(i)
        valid = True

if valid:
    print(f"Id pengguna yang valid = {valid_ids}")
else:
    print("Tidak ada Id Pengguna yang valid.")