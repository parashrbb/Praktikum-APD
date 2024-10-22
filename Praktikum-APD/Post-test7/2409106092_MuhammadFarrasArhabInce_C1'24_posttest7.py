from prettytable import PrettyTable

accounts = {
    "penjual": {'password': '1', 'role': 'admin', 'tiket': []},
    "pembeli": {'password': '2', 'role': 'pengguna', 'tiket': []},
}

Tiket_Wisata = {
    "Pulau Kumala": {'lokasi': 'Tenggarong', 'harga': 'Rp 20000'},
    "Ladaya": {'lokasi': 'Tenggarong', 'harga': 'Rp 25000'},
    "Pasir Putih": {'lokasi': 'Palu', 'harga': 'Rp 30000'},
    "Museum Mulawarman": {'lokasi': 'Tenggarong', 'harga': 'Rp 15000'},
    "Planetarium Jagad Raya": {'lokasi': 'Tenggarong', 'harga': 'Rp 40000'}
}

# Menambahkan Warna
class style():
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CRED      = '\33[31m'
    CGREEN    = '\33[32m'
    CWHITE    = '\33[37m'
    CBLUE     = '\33[34m'
    CYELLOW   = '\33[33m'
    CRED2     = '\33[91m'
    CGREEN2   = '\33[92m'

def tampilan_awal():
    print(" ")
    print(style.CRED + "====================================================================================================")
    print(style.CWHITE + "Selamat datang di pembelian tiket wisata!!")
    print("Silahkan pilih 'Daftar akun' jika belum membuat akun, dan jika sudah memiliki akun silahkan login")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print(style.CRED + "====================================================================================================")

def registrasi():
    print(" ")
    print(style.CRED + "================================")
    print(style.CWHITE + "Halo Pengguna Baru :)")
    print("Mari buat Akun terlebih dahulu!")
    print(style.CRED + "================================")
    Username = input(style.CWHITE + "Username: ")
    if Username in accounts:
        print(style.CRED2 + "Nama sudah terpakai untuk registrasi silahkan coba lagi")
    else:
        Password = input(style.CWHITE + "Password: ")
        Role = input("Masukkan Role (admin/pengguna): ")
        if Role not in ['admin', 'pengguna']:
            print(style.CRED2 + "Peran tidak valid, Anda 'admin' atau 'pengguna'??")
            return
        accounts[Username] = {'password': Password, 'role': Role, 'tiket': []}
        print(style.CGREEN + f"Yayyy! Anda berhasil terdaftar sebagai {Role}, dengan Username {Username}")

def login():
    print(" ")
    print(style.CRED + "==========================")
    print(style.CWHITE + "HI! Yuk login dulu :)")
    Username = input("Username: ")
    Password = input("Password: ")
    print(style.CRED + "==========================")
    if Username in accounts and accounts[Username]['password'] == Password:
        return Username
    else:
       print(style.CRED2 + "Maaf, Username atau Password salah!")

def tampilan_admin(Username):
    print(" ")
    print(style.CRED + "========================================")
    print(style.CWHITE + f"Selamat datang admin, {Username}!")
    print("Silahkan Pilih")
    print("1. Tambah Destinasi")
    print("2. Lihat Destinaasi")
    print("3. Edit Destinasi")
    print("4. Hapus Destinasi")
    print("5. Exit")
    print(style.CRED + "========================================") 
 
def tampilan_pengguna(Username):
    print(" ")
    print(style.CRED + "========================================")
    print(style.CWHITE + f"Selamat datang pengguna, {Username}!")
    print(style.CWHITE + "1. Beli tiket Masuk")
    print("2. Lihat tiket Masuk yang sudah dibeli")
    print("3. Lihat Destinasi Wisata")
    print("4. Batalkan Tiket")
    print("5. Exit")
    print(style.CRED + "========================================")

def Tambah_Destinasi():
    print(" ")
    print(style.CRED + "===========================")
    Destinasi_Wisata = input(style.CWHITE + "Destinasi: ")
    Lokasi_Wisata = input("Lokasi Wisata: ")
    Harga_Tiket = input("Harga Tiket Masuk: ")
    print(style.CRED + "===========================")
    Tiket_Wisata[Destinasi_Wisata] = {'lokasi': Lokasi_Wisata, 'harga': Harga_Tiket}
    print(style.CGREEN + "Wisata berhasil ditambahkan :)!")

def Beli_Tiket(Username):
    print(" ")
    Destinasi_Wisata = input("Destinasi: ")
    if Destinasi_Wisata in Tiket_Wisata:
        accounts[Username]['tiket'].append(Tiket_Wisata[Destinasi_Wisata])
        print(style.CGREEN + "Tiket Wisata berhasil dibeli :)!")

def Lihat_Destinasi():
    print(" ")
    table = PrettyTable()
    table.field_names = ["Destinasi", "Lokasi Wisata", "Harga Tiket"]
    for destinasi, info in Tiket_Wisata.items():
        table.add_row([destinasi, info['lokasi'], info['harga']])
    print(table)
    if not Tiket_Wisata:
        print(style.CRED2 + "Waduh... saat ini belum ada Destinasi yang tersedia, silahkan tambah Destinasi terlebih dahulu.")

def Tiket_Sudah_Dibeli(Username):
    if accounts[Username]['tiket']:
        table = PrettyTable()
        table.field_names = ["Destinasi", "Lokasi Wisata", "Harga Tiket"]
        for tiket in accounts[Username]['tiket']:
            for destinasi, info in Tiket_Wisata.items():
                if info['lokasi'] == tiket['lokasi'] and info['harga'] == tiket ['harga']:
                    table.add_row([destinasi, tiket['lokasi'], tiket['harga']])
                    break
        print(" ")
        print(style.CGREEN2 + "Anda sudah membeli tiket:")
        print(table)
    else:
        print(style.CRED2 + "Waduh... saat ini kamu belum mempunyai tiket, silahkan beli tiket terlebih dahulu.")

def Edit_Destinasi():
    if not Tiket_Wisata:
        print(style.CRED2 + "Tidak ada Destinasi yang bisa diedit.")
    else: 
        print(" ")
        destinasi = input(style.CYELLOW + "Masukkan nama destinasi yang ingin kamu edit: ")
        if destinasi in Tiket_Wisata:
            print(style.CRED + "==========================================")
            Destinasi_Baru = input(style.CWHITE + "Masukkan Destinasi yang baru: ")
            Lokasi_Baru = input("Masukkan lokasi yang baru: ")
            Harga_Baru = input("Masukkan harga yang baru: ")
            print(style.CRED + "==========================================")
            print(style.CWHITE + "Apa kamu yakin ingin mengedit Destinasi?")
            print("1. Iya")
            print("2. Tidak")
            print(style.CRED + "==========================================")
            Memastikan_Edit = input(style.CBLUE + "Pilih: ")
            if Memastikan_Edit == "1":
                del Tiket_Wisata[destinasi]
                Tiket_Wisata[Destinasi_Baru] = {'lokasi': Lokasi_Baru, 'harga': Harga_Baru}
                print(style.CGREEN + "Destinasi yang kamu pilih sudah di edit! :)")
            elif Memastikan_Edit == "2":
                print(style.CRED2 + "Aksi untuk mengedit Destinasi dibatalkan")
            else:
                print(style.CRED2 + "Tolong pilih '1' atau '2'")
        else:
            print(style.CRED2 + "Destinasi tidak ditemukan, silahkan input ulang.")

def Hapus_Destinasi():
    destinasi = input(style.CYELLOW + "Masukkan nama destinasi yang ingin dihapus: ")
    if destinasi in Tiket_Wisata:
        print(" ")
        print(style.CRED + "=============================================")
        print(style.CWHITE + "Apa kamu yakin ingin menghapus Destinasi?")
        print("1. Iya")
        print("2. Tidak")
        print(style.CRED + "=============================================")
        Memastikan_Hapus = input(style.CBLUE + "Pilih: ")
        if Memastikan_Hapus == "1":
            del Tiket_Wisata[destinasi]
            print(style.CGREEN + "Destinasi yang kamu pilih sudah dihapus!")
        elif Memastikan_Hapus == "2":
            print(style.CRED2 + "Aksi untuk menghapus Destinasi dibatalkan")
        else:
            print(style.CRED2 + "Tolong pilih '1' atau '2'")
    else:
        print(style.CRED2 + "Destinasi tidak ditemukan.")

def Batalkan_Tiket(Username):
    if not accounts[Username]['tiket']:
        print(style.CRED2 + "Tidak ada tiket yang bisa dibatalkan.")
    else:
        print(style.CRED + "Daftar Tiket yang sudah dibeli:")
        for i, tiket in enumerate(accounts[Username]['tiket']):
            print(f"{i + 1}. Destinasi: {tiket['lokasi']}, Harga: {tiket['harga']}")
        tiket_index = int(input(style.CYELLOW + "Pilih nomor tiket yang ingin dibatalkan: ")) - 1
        if 0 <= tiket_index < len(accounts[Username]['tiket']):
            canceled_ticket = accounts[Username]['tiket'].pop(tiket_index)
            print(style.CGREEN + f"Tiket ke {canceled_ticket['lokasi']} berhasil dibatalkan!")
        else:
            print(style.CRED2 + "Nomor tiket tidak valid.")



while True:
    tampilan_awal()
    pilihan = input(style.CBLUE + "Pilih opsi : ")
    if pilihan == "1":
        registrasi()
    elif pilihan == "2":
        Username = login()
        if Username:
            while True:
                if accounts[Username]['role'] == 'admin':
                    tampilan_admin(Username)
                else:
                    tampilan_pengguna(Username)
                status = input(style.CBLUE + "Pilih opsi: ")
                if status == "1":
                    if accounts[Username]['role'] == 'admin':
                        Tambah_Destinasi()
                    else:
                        Beli_Tiket(Username)
                elif status == "2":
                    if accounts[Username]['role'] == 'admin':
                        Lihat_Destinasi()
                    else:
                        Tiket_Sudah_Dibeli(Username)
                elif status == "3":
                    if accounts[Username]['role'] == 'admin':
                        Edit_Destinasi()
                    else:
                        Lihat_Destinasi()

                elif status == "4":
                    if accounts[Username]['role'] == 'admin':
                        Hapus_Destinasi()
                    else:
                        Batalkan_Tiket(Username)
                elif status == "5":
                    print(style.CYELLOW + "Terimakasih sudah menggunakan aplikasi, semoga harimu menyenangkan! XD")
                    break
                else:
                    print(style.CRED2 + "Input tidak valid, silahkan pilih opsi yang tersedia")

    elif pilihan == "3":
        print(style.CYELLOW + "Terimakasih sudah menggunakan aplikasi, semoga harimu menyenangkan! XD")
        break
    else:
        print(style.CRED2 + "Input tidak valid, silahkan pilih opsi yang tersedia")