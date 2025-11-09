# NIM/Nama : 19624156/Riantama Putra
# Tanggal : 21/11/2024
# Deskripsi :

#Program SubprogramBaru
#Mengatur subprogram secara dinamis, menjalankan, dan menukarnya

#KAMUS
#nama_subprogram : list of str
#pesan_subprogram : list of str
#jumlah_subprogram : int
#perintah, nama1, nama2, variabel: str

#definisi dan realisasi fungsi generate_subprogram
def generate_subprogram(jumlah_subprogram):
    nama_subprogram = [""] * jumlah_subprogram
    pesan_subprogram = [""] * jumlah_subprogram
    for i in range (jumlah_subprogram):
        nama_subprogram [i] = input("Masukkan nama subprogram: ")
        pesan_subprogram [i] = input("Masukkan pesan: ")
    return nama_subprogram, pesan_subprogram

def jalankan_subprogram(nama_subprogram, pesan_subprogram):
    selesai = False
    while not selesai:
        perintah = input("Masukkan perintah: ")
        if perintah == "stop":
            selesai = True
        elif perintah == "!!!":
            nama1 = input("Masukkan nama subprogram pertama: ")
            nama2 = input("Masukkan nama subprogram kedua: ")
            if nama1 in nama_subprogram and nama2 in nama_subprogram:
                #tukar posisi nama1 dan nama2
                idx1 = nama_subprogram.index(nama1)
                idx2 = nama_subprogram.index(nama2)
                pesan_subprogram[idx1], pesan_subprogram[idx2] = pesan_subprogram [idx2], pesan_subprogram[idx1]
                print(f"Subprogram {nama1} dan {nama2} telah ditukar")
            else:
                print("Salah satu atau kedua subprogram tidak ditemukan.")
        elif perintah in nama_subprogram:
            idx = nama_subprogram.index(perintah)
            variabel = input ("Masukkan nilai variabel: ")
            print(f"{pesan_subprogram[idx]} {variabel}")
        else:
            print(f"Subprogram {perintah} tidak ditemukan")
    
#program utama
def main():
    jumlah_subprogram = int(input("Masukkan jumlah subprogram: "))
    nama_subprogram, pesan_subprogram = generate_subprogram(jumlah_subprogram)
    jalankan_subprogram(nama_subprogram, pesan_subprogram)
main()