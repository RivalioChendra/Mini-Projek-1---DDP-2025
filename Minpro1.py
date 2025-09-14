# Data hutang awal
daftar_hutang = [
    (1, "Dapa", "50000"),
    (2, "Darma", "75000"),
    (3, "Zyrus", "100000")
]

print("1. Tambah Hutang")
print("2. Lihat Hutang")
print("3. Ubah Hutang")
print("4. Hapus Hutang")
pilihan = input("Pilih menu: ")

if pilihan == "1":  # CREATE
    id_baru = 4  # ID berikutnya
    nama = input("Nama: ")
    jumlah = input("Jumlah: ")
    daftar_hutang.append((id_baru, nama, jumlah))
    print("Data berhasil ditambah!")
    print("ID:", id_baru, "| Nama:", nama, "| Jumlah:", jumlah)

elif pilihan == "2":  # READ
    print("Daftar Hutang:")
    id, nama, jumlah = daftar_hutang[0]
    print("ID:", id, "| Nama:", nama, "| Jumlah:", jumlah)
    id, nama, jumlah = daftar_hutang[1]
    print("ID:", id, "| Nama:", nama, "| Jumlah:", jumlah)
    id, nama, jumlah = daftar_hutang[2]
    print("ID:", id, "| Nama:", nama, "| Jumlah:", jumlah)

elif pilihan == "3":  # UPDATE
    print("Daftar Hutang:")
    id, nama, jumlah = daftar_hutang[0]
    print("ID:", id, "| Nama:", nama, "| Jumlah:", jumlah)
    id, nama, jumlah = daftar_hutang[1]
    print("ID:", id, "| Nama:", nama, "| Jumlah:", jumlah)
    id, nama, jumlah = daftar_hutang[2]
    print("ID:", id, "| Nama:", nama, "| Jumlah:", jumlah)

    nomor = input("Masukkan ID yang mau diubah: ")
    try:
        nomor = int(nomor)
        if nomor == 1:
            nama = input("Nama baru: ")
            jumlah = input("Jumlah baru: ")
            daftar_hutang[0] = (1, nama, jumlah)
            print("Data berhasil diubah!")
        elif nomor == 2:
            nama = input("Nama baru: ")
            jumlah = input("Jumlah baru: ")
            daftar_hutang[1] = (2, nama, jumlah)
            print("Data berhasil diubah!")
        elif nomor == 3:
            nama = input("Nama baru: ")
            jumlah = input("Jumlah baru: ")
            daftar_hutang[2] = (3, nama, jumlah)
            print("Data berhasil diubah!")
        else:
            print("ID tidak ditemukan!")
    except ValueError:
        print("ID harus berupa angka!")

elif pilihan == "4":  # DELETE
    print("Daftar Hutang:")
    id, nama, jumlah = daftar_hutang[0]
    print("ID:", id, "| Nama:", nama, "| Jumlah:", jumlah)
    id, nama, jumlah = daftar_hutang[1]
    print("ID:", id, "| Nama:", nama, "| Jumlah:", jumlah)
    id, nama, jumlah = daftar_hutang[2]
    print("ID:", id, "| Nama:", nama, "| Jumlah:", jumlah)

    nomor = input("Masukkan ID yang mau dihapus: ")
    try:
        nomor = int(nomor)
        if nomor == 1:
            terhapus = daftar_hutang.pop(0)
            print("Data", terhapus[1], "berhasil dihapus!")
        elif nomor == 2:
            terhapus = daftar_hutang.pop(1)
            print("Data", terhapus[1], "berhasil dihapus!")
        elif nomor == 3:
            terhapus = daftar_hutang.pop(2)
            print("Data", terhapus[1], "berhasil dihapus!")
        else:
            print("ID tidak ditemukan!")
    except ValueError:
        print("ID harus berupa angka!")

else:
    print("Menu tidak tersedia, masukkan angka 1-4 saja!")