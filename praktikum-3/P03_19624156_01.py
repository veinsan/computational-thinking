# NIM/Nama : 19624156/Riantama Putra
# Tanggal : 21/11/2024
# Deskripsi :

#Program Rata-RataHargaBarang
#Menghitung rata-rata barang berdasarkan list harga yang diberikan

#KAMUS
#harga_list : list of float
#rata_rata : float
#mata_uang : string

#definisi dan realisasi fungsi rata2
def rata2 (list_harga):
    total = sum(list_harga)
    #menghasilkan rata-rata harga barang
    rata_rata = total / len (list_harga)
    return rata_rata

#definisi dan realisasi prosedur cetak_hasil
def cetak_hasil(harga, mata_uang):
    #mencetak rata-rata dengan format tertentu
    print(f"Rata-rata harga barang adalah {harga:.2f} {mata_uang}")

#program utama
def main():
    n = int(input("Masukkan banyaknya harga: "))
    list_harga = [0] * n
    for i in range (n):
        list_harga[i] += float(input(f"Masukkan harga ke-{i+1}: "))
    mata_uang = input ("Masukkan string mata uang: ")
    #pemanggilan fungsi dan prosedur
    rata_rata = rata2(list_harga)
    cetak_hasil(rata_rata, mata_uang)
main()