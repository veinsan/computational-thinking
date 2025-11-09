# NIM/Nama : 19624156/Riantama Putra
# Tanggal : 31/10/2024
# Deskripsi : Problem 02

udah = [""] * 100
terhitung = [""] * 100
dua = 0
boleh = 0
kehitung = 0

while True:
    tiket = input ("Masukkan nomor tiket pengunjung: ")
    if tiket == "XXX":
        break

    dipakai = False
    for i in range (boleh):
        if udah[i] == tiket:
            dipakai = True
            break

    if dipakai:
        print("Pengunjung tersebut tidak bisa mendapat konsumsi lagi.")
        dihitung = False
        for j in range (kehitung):
            if terhitung[j] == tiket:
                dihitung = True
                break
        if not dihitung:
            dua += 1
            if kehitung < len (terhitung):
                terhitung [kehitung] = tiket
                kehitung += 1
    else:
        print ("Pengunjung tersebut bisa mendapat konsumsi.")
        if boleh < len(udah):
            udah[boleh] = tiket
            boleh += 1

print(f"Total pengunjung yang mendapat konsumsi: {boleh} ")

if dua > 0:
    print(f"Total pengunjung yang mencoba mendapat konsumsi lebih dari satu kali: {dua}")