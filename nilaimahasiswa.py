print("===== Grade mahasiswa =====")
print("")

nama = input("Masukkan nama anda : ")
nim = input("Masukkan nim anda : ")
jurusan = input("Masukkan jurusan anda : ")
absen = int (input("Masukkan nilai absen anda : "))
uts = int (input("Masukkan nilai uts anda : "))
uas = int (input("Masukkan nilai uas anda : "))
print("")

print("====== Biodata Mahasiswa ======")
print("Nama : ", nama)
print("Nim : ", nim)
print("Jurusan : ", jurusan)
print("=="*15)
print("")

print("====== Nilai Mahasiswa ======")
print("Nilai absen : ", absen)
print("Nilai UTS : ", uts)
print("Nilai UAS : ", uas)
print("=="*15)
print("")

jumlah = absen + uts +uas
rata = jumlah / 3

print("Nilai rata-rata anda : ", rata)

if rata >= 95:
    print("Grade anda : A")
    print("Anda lulus, pertahankan kemapuan anda!")
elif rata >= 80:
    print("Grade anda : B")
    print("Anda lulus, jangan mau kalah sama yg lain")
elif rata >= 75:
    print("Grade anda : C")
    print("Anda lulus, jangan lupa belajar!")
elif rata >= 60:
    print("Grade anda : D")
    print("Anda lulus, belajar lebih giat lagi!")
else:
    print("Grade anda : E")
    print("Ayo lebih giat lagi belajarnya, jangan mau kalah sama yg lain, kamu pasti bisa!!!")
    print("Semangat!!!")