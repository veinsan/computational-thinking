# NIM/Nama : 19624156/Riantama Putra
# Tanggal : 21/11/2024
# Deskripsi :

#Program WaktuTidurNonaDeb
#Menghitung waktu bangun berdasarkan aktivitas sehari-hari Nona Deb

#KAMUS
#jam_tidur, menit_tidur : int
#total_tidur : float
#tambahan_waktu_tidur : float
#minum_kopi : bool
#olahraga, basket : bool

#definisi dan realisasi fungsi hitung_tambahan_tidur
def hitung_tambahan_tidur (banyak_tugas, olahraga, basket):
    #menghitung tambahan waktu tidur berdasarkan aktivitas
    tambahan_waktu_tidur = 0
    tambahan_waktu_tidur += banyak_tugas
    if olahraga:
        tambahan_waktu_tidur += 2
    if basket:
        tambahan_waktu_tidur += 0.5
    return tambahan_waktu_tidur

#definisi dan realisasi prosedur waktu_bangun
def waktu_bangun (jam_tidur, menit_tidur, tambahan_waktu_tidur, minum_kopi):
    #menyesuaikan waktu tidur jika minum kopi
    if minum_kopi:
        jam_tidur += 3
    #total waktu tidur
    total_tidur = 3 + tambahan_waktu_tidur
    total_menit = int(total_tidur*60)
    menit_bangun = menit_tidur + total_menit
    jam_bangun = jam_tidur + (menit_bangun // 60)
    menit_bangun = menit_bangun % 60
    jam_bangun = jam_bangun % 24
    print(f"Nona Deb bangun pada pukul {jam_bangun}:{menit_bangun:02}")

#program utama
def main():
    print("Waktu mulai tidur Nona Deb:")
    jam_tidur = int(input("Jam: "))
    menit_tidur = int(input("Menit: "))
    banyak_tugas = int(input("Banyak Tugas: "))
    olahraga = input("Apakah berolahraga hari ini (ya/tidak)? ").strip().lower() == "ya"
    basket = input("Apakah menonton basket hari ini (ya/tidak)? ").strip().lower() == "ya"
    minum_kopi = input("Apakah minum kopi (ya/tidak)? ").strip().lower() == "ya"
    tambahan_waktu_tidur = hitung_tambahan_tidur(banyak_tugas, olahraga, basket)
    waktu_bangun (jam_tidur, menit_tidur, tambahan_waktu_tidur, minum_kopi)
main()