# Min-Projek 1 - DDP2025
## _Sistem Manajemen Pencatatan Hutang_

Nama: Rivalio Chendra          
NIM: 2509116039      
Kelas: Sistem Informasi A'2025    
<br><br>

### Deskripsi
Program ini adalah aplikasi sederhana untuk pencatatan hutang menggunakan bahasa pemrograman Python.  
Konsep yang digunakan adalah **CRUD** (Create, Read, Update, Delete).
<br><br>

### Flowchart Program
<img width="1451" height="1077" alt="Flowchart pencatat hutang" src="https://github.com/user-attachments/assets/da2d898e-7c17-4180-b5ae-326bf266d297" />
<br><br>

### Alur Program  
<img width="1392" height="174" alt="Screenshot 2025-09-14 203952" src="https://github.com/user-attachments/assets/0a115cbd-390a-494b-b346-9f2a0cc7545b" />           
Menampilkan pilihan menu ke user. Selalu ditampilkan di awal program. Menunggu input dari user. User harus ketik 1, 2, 3, atau 4.  
<br><br>

- **Pilihan 1: Tambah hutang**
<img width="1459" height="94" alt="image" src="https://github.com/user-attachments/assets/98f819ef-18c1-4c68-b192-59897b2ee12a" />
Prompt untuk mengetik nama orang yang berutang.
<br><br>
<img width="1461" height="97" alt="image" src="https://github.com/user-attachments/assets/03a797c7-5c97-4375-9653-534780a7039b" />
Prompt untuk mengetik jumlah hutang.                             
<br><br>
<img width="1434" height="125" alt="image" src="https://github.com/user-attachments/assets/5852e81c-51b8-46e9-bd8c-79cb291b3319" />
Menampilkan data baru yang baru ditambahkan (ID ditetapkan 4 di kode ini).
<br><br>

**Pilihan 2: Lihat hutang**
<img width="1439" height="128" alt="image" src="https://github.com/user-attachments/assets/9576f198-52bc-4ca1-900a-023be8c47e26" />
Header untuk daftar yang akan ditampilkan. Tiga baris ini menampilkan masing-masing data awal.
<br><br>

- **Pilihan 3: Ubah hutang**
<img width="1383" height="165" alt="image" src="https://github.com/user-attachments/assets/b48c87a3-59a7-40ec-b910-ac776f5c642d" />
Menunjukkan daftar supaya user tahu ID mana yang mau diubah. Prompt untuk mengetik ID yang ingin diedit.
<br><br>
<img width="1417" height="188" alt="image" src="https://github.com/user-attachments/assets/d89887ba-1ddb-4c65-a6a3-092eec3c81a7" />
Tulis nama baru dari data yang mau di ubah.
<br><br>
<img width="1404" height="210" alt="image" src="https://github.com/user-attachments/assets/83f37309-d86f-4066-9fc7-6b52cfbbc5de" />
Masukan jumlah hutang baru.
<br><br>
<img width="1394" height="236" alt="image" src="https://github.com/user-attachments/assets/648f5cae-ce13-48f7-9650-a5b22f9c71af" />
Jika seperti ini, berarti data berhasil diubah.
<br><br>

**Kemungkinan keluaran setelah input ID**
  <img width="1390" height="175" alt="image" src="https://github.com/user-attachments/assets/eaab7ae3-330e-49ad-94ee-4dd0420914a0" />
Muncul jika user memasukkan ID 1, 2, atau 3 dan proses penggantian nama/jumlah sukses.
<br><br>
<img width="1387" height="179" alt="image" src="https://github.com/user-attachments/assets/18ea2d08-2e98-44c3-96ef-91c06fd2a48d" />
Muncul jika user mengetik sesuatu yang bukan angka (contoh: abc), karena program mencoba mengubah input ke integer dan gagal.
<br><br>

- **Pilihan 4: Hapus hutang**
<img width="1404" height="165" alt="image" src="https://github.com/user-attachments/assets/b1cb6147-db84-47db-968d-95421bf24a54" />
Menampilkan daftar supaya user memilih ID yang akan dihapus.
Prompt untuk mengetik ID yang akan dihapus.
<br><br>
<img width="1319" height="172" alt="image" src="https://github.com/user-attachments/assets/e550c571-3061-4770-86fc-b988b513106b" />
Contoh: "Data Dapa berhasil dihapus!", muncul bila ID 1/2/3 dipilih dan pop() berhasil menghapus item, menampilkan nama yang dihapus.
<br><br>

**Kemungkinan keluaran setelah input ID**
  <img width="1405" height="181" alt="image" src="https://github.com/user-attachments/assets/16388273-813c-4ff0-b105-767238661afe" />
Muncul bila user memasukkan angka selain 1,2,3.
<br><br>
<img width="1421" height="183" alt="image" src="https://github.com/user-attachments/assets/de157e76-f1d3-4d8a-98a4-9541792e5b80" />
Muncul bila input ID bukan angka (gagal konversi ke int).
<br><br>
<br><br>
<img width="1362" height="150" alt="image" src="https://github.com/user-attachments/assets/75dd5a94-0952-44ef-9e4b-bc7fa6f9dd4a" />
Muncul bila user memasukkan pilihan selain "1", "2", "3", atau "4" (entah itu huruf, angka ataupun simbol)
