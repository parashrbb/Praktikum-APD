# Fitur Menghapus Terminal agar terlihat rapih
import os
# Fitur Mmembuat Table
# os.system("pip install PrettyTable")
from prettytable import PrettyTable
# Fitur Membuat ketika input password jadi bintang ****
# os.system("pip install pwinput")
import pwinput

class style():
    CRED      = '\33[31m'
    CGREEN    = '\33[32m'
    CWHITE    = '\33[37m'
    CYELLOW   = '\33[33m'
    CBLUE     = '\33[34m'
    ENDC      = '\033[0m'

# Data pengguna dan tiket kereta
pengguna = {}

# Menyimpan username dan password admin
akun_admin = ["admin", "admin123"]

# Tiket Kereta Yang Tersedia Dari Awal menggunakan nested dictionary
tiket_kereta = {
    1: {"nama": "Stasiun Gear", "rute": "Samarinda-Balikpapan", "harga": 150000, "kursi": 70},
    2: {"nama": "Stasiun ISO", "rute": "Samarinda-Banjarmasin", "harga": 280000, "kursi": 50},
    3: {"nama": "Stasiun Unmul", "rute": "Balikpapan-Palangkaraya", "harga": 500000, "kursi": 30},
    4: {"nama": "Stasiun Teknik", "rute": "Tenggarong-Samarinda", "harga": 100000, "kursi": 30},
    5: {"nama": "Stasiun Infor", "rute": "Balikpapan-Banjarmasin", "harga": 450000, "kursi": 40},
    6: {"nama": "Stasiun Python", "rute": "Tenggarong-Sangkulirang", "harga": 350000, "kursi": 50}
}

#stasiun yang tersedia
stasiun_tersedia = [info["nama"] for info in tiket_kereta.values()]

# Data pemesanan tiket
data_pemesanan = []

# fungsi os
def hapus():
    os.system('cls' if os.name == 'nt' else 'clear')

def goodbye():
    print(style.CBLUE + """
                     _                       | 
                    (_| _  _  _|   |_  \/ _  | 
                    __|(_)(_)(_|   |_) / (/_ o 
        """ + style.ENDC)
    

def logo_tiket_tersedia():
    print(style.CBLUE + """
  ___  _  _           _     ___                       _  _      
 |_ _|<_>| |__ ___  _| |_  |_ _| ___  _ _  ___ ___  _| |<_> ___ 
  | | | || / // ._>  | |    | | / ._>| '_><_-</ ._>/ . || |<_> |
  |_| |_||_\_\\___.   |_|    |_| \___.|_|  /__/\___.\___||_|<___|
        """ + style.ENDC)

# Menu Paling Awal
def tampilan_awal():
    hapus()
    print(style.CBLUE + "======================================================================" + style.ENDC)
    print(style.CWHITE + "\tSelamat datang di pemesanan tiket stasiun Mulawarman >_<")
    print("\t\t    Silahkan Pilih Menu >_<")
    print(style.CBLUE + "======================================================================")
    print(style.CWHITE + "1. Masuk\n2. Daftar\n3. Keluar" + style.ENDC)

# Menu Daftar
def daftar():
    hapus()
    print(style.CBLUE + "=" * 35)
    print(style.CWHITE + "\tHalo pengguna baru!")
    print("\t  Silahkan Daftar")
    print(style.CBLUE + "=" * 35)
    username_baru = input(style.CWHITE + "Masukkan Username: ")
    # Cek apakah username sudah ada atau digunakan untuk admin
    if username_baru in pengguna or username_baru == akun_admin[0]:
        print(style.CRED + "\nUsername sudah digunakan!" + style.ENDC)
    else:
        password_baru = pwinput.pwinput(style.CWHITE + "Masukkan Password: ")
        if len(password_baru) < 8:
            print(style.CRED + "\nPassword tidak boleh kurang dari 8 karakter." + style.ENDC)
        else:
            pengguna[username_baru] = {'password': password_baru, 'role': 'pengguna', 'tiket': []}
            print(style.CGREEN + "\nPendaftaran berhasil! Anda terdaftar sebagai pengguna.")
    
    input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)

# Menu Masuk 
def login():
    hapus()
    print(style.CBLUE + "=" * 45)
    print(style.CWHITE + "\t     Halo Selamat Datang!!")
    print("\t\tSilahkan Login")
    print(style.CBLUE + "=" * 45)
    username = input(style.CWHITE + "Username: ")
    password = pwinput.pwinput(style.CWHITE + "Kata Sandi: " + style.ENDC)

    # Cek apakah username dan password cocok dengan akun admin
    if username == akun_admin[0] and password == akun_admin[1]:
        return akun_admin[0]  # Kembalikan username admin jika cocok

    # Jika bukan admin, cek dalam data pengguna biasa
    elif username in pengguna and pengguna[username]['password'] == password:
        return username
    else:
        print(style.CRED + "\nUsername atau kata sandi salah!")

    input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)

# Tampilan Admin
def tampilan_admin():
    hapus()
    print(style.CBLUE + "=" * 30)
    print(style.CWHITE + f"Selamat Datang Admin!")
    print("1. Lihat Tiket Tersedia\n2. Tambah Tiket\n3. Perbarui Informasi Tiket\n4. Hapus Tiket\n5. Data pemesanan\n6. Exit") 
    print(style.CBLUE + "=" * 30 + style.ENDC)

# Tampilan Pengguna
def tampilan_pengguna(username):
    hapus()
    print(style.CBLUE + "=" * 30)
    print(style.CWHITE + f"Selamat Datang Pengguna {username}!")
    print("1. Lihat Tiket Tersedia\n2. Booking Tiket\n3. Tiket yang dipesan\n4. Batalkan Tiket\n5. Exit") 
    print(style.CBLUE + "=" * 30 + style.ENDC)

# Fungsi Melihat tiket yang tersedia (data dari dictionary 'tiket_kereta')
def lihat_tiket():
    hapus()
    # Table yang bagian atas
    table = PrettyTable(["ID", "Nama Stasiun", "Rute", "Harga", "Kursi"])
    # Table bagian isi
    for ID_Tiket, info in tiket_kereta.items():
        table.add_row([ID_Tiket, info["nama"], info["rute"], info["harga"], info["kursi"]])
    # Menampilkan Table
    logo_tiket_tersedia()
    print(table)
    input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)

# Fungsi dari menu admin untuk menambah tiket yang tersedia
def tambah_tiket():
    hapus()
    # Tampilkan Table
    lihat_tiket()
    print(style.CBLUE + "\n=== Tambah Tiket ===" + style.ENDC)

    # Pilih stasiun
    print(style.CYELLOW + "Pilih stasiun yang tersedia:" + style.ENDC)
    # Menampilkan stasiun yang sudah berada di dictionary 'tiket_kereta'
    for i, stasiun in enumerate(stasiun_tersedia, start=1):
        print(style.CWHITE + f"{i}. {stasiun}" + style.ENDC)
    try:
        pilihan_stasiun = int(input(style.CWHITE + "Pilih nomor stasiun: " + style.ENDC)) - 1
        # Mengecek apakah pilihan stasiun berada di data stasiun_tersedia
        if 0 <= pilihan_stasiun < len(stasiun_tersedia):
            # pilihan stasiun akan disimpan di variable nama_stasiun
            nama_stasiun = stasiun_tersedia[pilihan_stasiun]
        else:
            print(style.CRED + "\nPilihan tidak valid. Silakan coba lagi." + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk kembali ke menu admin >_< " + style.ENDC)
            return
    except ValueError:
        print(style.CRED + "\nInput harus berupa angka. Silakan coba lagi." + style.ENDC)
        input(style.CWHITE + "Tekan enter untuk kembali ke menu admin >_< " + style.ENDC)
        return

    # Minta rute awal dan rute akhir
    rute_awal = input(style.CWHITE + "Rute awal: " + style.ENDC)
    rute_akhir = input(style.CWHITE + "Rute akhir: " + style.ENDC)
    # Menyimpan rute awal dan rute akhir di variable 'rute'
    rute = f"{rute_awal}-{rute_akhir}"

    # Input harga
    try:
        harga = int(input(style.CWHITE + "Harga tiket (dalam IDR): " + style.ENDC))
        if harga <= 0:
            print(style.CRED + "\nHarga harus lebih dari 0. Silakan coba lagi." + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk kembali ke menu admin >_< " + style.ENDC)
            return
    except ValueError:
        print(style.CRED + "\nInput harus berupa angka. Silakan coba lagi." + style.ENDC)
        input(style.CWHITE + "Tekan enter untuk kembali ke menu admin >_< " + style.ENDC)
        return

    # Input jumlah tiket
    try:
        kursi = int(input(style.CWHITE + "Jumlah tiket tersedia: " + style.ENDC))
        if kursi <= 0:
            print(style.CRED + "\nJumlah tiket tidak boleh dibawah angka 1. Silakan coba lagi." + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk kembali ke menu admin >_< " + style.ENDC)
            return
        elif kursi > 80:
            print(style.CRED + "\nJumlah Tiket Tersedia tidak boleh lebih dari 80." + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk kembali ke menu admin >_< " + style.ENDC)
            return
        else:
            # Menentukan ID tiket yang baru ditambahkan jika kursi yang di input sudah benar, dengan mengecek keys di tiket_kereta maxnya berapa
            id_tiket_baru = max(tiket_kereta.keys()) + 1 if tiket_kereta else 1

            # Menambahkan tiket di dictionary tiket_kereta
            tiket_kereta[id_tiket_baru] = {"nama": nama_stasiun, "rute": rute, "harga": harga, "kursi": kursi}
            print(style.CGREEN + "\nTiket berhasil ditambahkan!" + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk kembali ke menu admin >_< " + style.ENDC)
            return
    except ValueError:
        print(style.CRED + "\nInput harus berupa angka. Silakan coba lagi." + style.ENDC)
        input(style.CWHITE + "Tekan enter untuk kembali ke menu admin >_< " + style.ENDC)
        return

# Fungsi dari menu pengguna untuk booking
def booking_tiket(username):
    lihat_tiket()
    try:
        # memilih id tiket yang ingin dipesan
        print(style.CBLUE + "\n=== Booking Tiket ===" + style.ENDC)
        ID_Tiket = int(input("Masukkan ID tiket yang ingin dipesan: "))
        if ID_Tiket not in tiket_kereta:
            print(style.CRED + "\nID tiket tidak valid!" + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
            return # kembali ke menu pengguna
        
        # memasukkan jumlah tiket yang ingin dipesan
        jumlah = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
        if jumlah <= 0:
            print(style.CRED + "\nJumlah tiket harus lebih dari 0!" + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
            return # kembali ke menu pengguna
        
        # Mengecek apakah jumlah tiket yang tersedia lebih besar atau sama dengan jumlah tiket yang diminta.
        if tiket_kereta[ID_Tiket]['kursi'] >= jumlah:
            # Mengurangi Jumlah Tiket yang Tersedia akan mengubah data di dictionary tiket_kereta.
            tiket_kereta[ID_Tiket]['kursi'] -= jumlah
            # menambahkan data pemesanan
            data_pemesanan.append({
                "username": username,
                "nama_stasiun": tiket_kereta[ID_Tiket]["nama"],
                "rute": tiket_kereta[ID_Tiket]["rute"],
                "jumlah_tiket": jumlah,
                "ID_Tiket": ID_Tiket
            })
            print(style.CGREEN + f"\nTiket berhasil dipesan! Total: {jumlah} tiket di {tiket_kereta[ID_Tiket]['nama']}." + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
        else:
            print(style.CRED + f"\nJumlah tiket yang diminta melebihi kursi yang tersedia ({tiket_kereta[ID_Tiket]['kursi']})." + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
    except ValueError:
        print(style.CRED + "\nInput tidak valid! Harap masukkan angka." + style.ENDC)
        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)

# Fungsi Menu admin untuk Melihat Data Pemesanan 
def lihat_data_pemesanan():
    hapus()
    # Mengecek apakah sudah ada pemesanan yang terjadi
    print(style.CBLUE + "\n              === Pemesanan ===" + style.ENDC)
    if not data_pemesanan:
        print(style.CRED + "\nBelum ada pesanan tiket untuk saat ini." + style.ENDC)
        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
    else:
        # Membuat table Pemesanan
        table = PrettyTable(["Username", "Nama Stasiun", "Rute", "Jumlah Tiket"])
        for pemesanan in data_pemesanan:
            table.add_row([pemesanan["username"], pemesanan["nama_stasiun"], pemesanan["rute"], pemesanan["jumlah_tiket"]])
        # print tamble pemesanan
        print(table)
        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)

#Fungsi Menu admin untuk mengedit data tiket_kereta
def edit_data():
    hapus()
    lihat_tiket()

    print(style.CBLUE + "\n=== Edit Data ===" + style.ENDC)
    try:
        # memilih ID tiket yang ingin di ediy]t
        id_tiket = int(input("Masukkan ID tiket yang ingin diedit: "))
        # Mengecek apakah ada id tiket di dictionary tiket_kereta
        if id_tiket not in tiket_kereta:
            print(style.CRED + "\nID tiket tidak valid!" + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
            return
        
        # Menyimpan pilihan id_tiket di variable 'tiket'
        tiket = tiket_kereta[id_tiket]
        # Memberitahu admin id tiket apa yang akan dia edit
        print(style.CYELLOW + f"\nAnda sedang mengedit tiket dengan ID {id_tiket}:" + style.ENDC)
        print(f"Stasiun: {tiket['nama']}, Rute: {tiket['rute']}, Harga: {tiket['harga']}, Kursi Tersedia: {tiket['kursi']}")
        
        # Pilihan untuk mengedit
        print(style.CBLUE + "\n=== Apa yang anda edit? ===" + style.ENDC)
        print("1. Nama Stasiun")
        print("2. Rute")
        print("3. Harga")
        print("4. Jumlah Tiket")
        print("5. Batal")

        pilih_edit = int(input("Pilih opsi: "))
        
        # Edit Nama Stasiun
        if pilih_edit == 1:
            nama_baru = input("Masukkan nama stasiun baru: ")
            tiket['nama'] = (f"Stasiun {nama_baru}")
        # Edit Rute
        elif pilih_edit == 2:
            rute_awal = input("Masukkan rute awal baru: ")
            rute_akhir = input("Masukkan rute akhir baru: ")
            tiket['rute'] = f"{rute_awal}-{rute_akhir}"
        # Edit Harga
        elif pilih_edit == 3:
            harga_baru = int(input("Masukkan harga tiket baru: "))
            tiket['harga'] = harga_baru
        # Edit Jumlah Tiket
        elif pilih_edit == 4:
            kursi_baru = int(input("Masukkan jumlah tiket baru: "))
            if kursi_baru > 80:
                print(style.CRED + "\nJumlah Tiket Tersedia tidak boleh lebih dari 80." + style.ENDC)
                input(style.CWHITE + "Tekan enter untuk kembali ke menu admin >_< " + style.ENDC)
                return
            else: 
                tiket['kursi'] = kursi_baru
        #Batal Edit
        elif pilih_edit == 5:
            print(style.CGREEN + "\nPerubahan dibatalkan." + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
            return
        else:
            print(style.CRED + "\nPilihan tidak valid." + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
            return
        
        print(style.CGREEN + "\nTiket berhasil diperbarui!" + style.ENDC)

    except ValueError:
        print(style.CRED + "\nInput tidak valid." + style.ENDC)
    
    input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)

# Fungsi Hapus Data
def hapus_data():
    hapus()
    lihat_tiket()

    print(style.CBLUE + "\n=== Hapus Data ===" + style.ENDC)
    try:
        id_tiket = int(input("Masukkan ID tiket yang ingin dihapus: "))
        if id_tiket in tiket_kereta:
            print(style.CYELLOW + "\nApakah anda yakin akan menghapus tiket?" + style.ENDC)
            print("1. Ya\n2. Tidak")
            yakin = int(input("Hapus?: "))

            if yakin == 1:
                # Hapus tiket dari tiket_kereta
                del tiket_kereta[id_tiket]
                # Hapus tiket dari data pemesanan
                global data_pemesanan
                # Melihat apakah ID_tiket di data_pemesanan sama dengan id_tiket(yg ingin dihapus) jika iya, tiket tersebut akan di hapus
                data_pemesanan = [pemesanan for pemesanan in data_pemesanan if pemesanan["ID_Tiket"] != id_tiket]
                print(style.CGREEN + f"\nTiket dengan ID {id_tiket} berhasil dihapus beserta data pemesanan terkait!" + style.ENDC)
                input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
                return
            elif yakin == 2:
                print(style.CGREEN + "\nAnda memilih untuk batalkan penghapusan." + style.ENDC)
                input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
                return
            else:
                print(style.CRED + "\nPilihan tidak valid." + style.ENDC)
                input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
                return
        else:
            print(style.CRED + "\nID tiket tidak valid!" + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
    
    except ValueError:
        print(style.CRED + "\nInput tidak valid." + style.ENDC)
        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)

# Fungsi Melihat Pemesanan yang sudah di pesan oleh pengguna
def tiket_dipesan(username):
    hapus()
    print(style.CBLUE + f"=== Tiket yang Dipesan oleh {username} ===" + style.ENDC)
    # Mengecek apakah sudah ada pemesanan yang terjadi
    if not data_pemesanan:
        print(style.CRED + "\nAnda belum memesan tiket apa pun." + style.ENDC)
        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
    else:
        # Membuat tabel untuk menampilkan tiket yang dipesan
        table = PrettyTable(["ID Tiket", "Nama Stasiun", "Rute", "Jumlah Tiket"]) 
        # Menambahkan semua tiket yang dipesan oleh pengguna ke tabel
        for pemesanan in data_pemesanan:
            # Mengecek apakah nilai username di dalam data_pemesanan cocok dengan username yang dimiliki oleh pengguna yang sedang login.
            if pemesanan["username"] == username:
                # Tambahkan setiap pemesanan yang sesuai dengan username ke dalam tabel
                table.add_row([pemesanan["ID_Tiket"], pemesanan["nama_stasiun"], pemesanan["rute"], pemesanan["jumlah_tiket"]])

        print(table)
        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)


# Fungsi Menu Pengguna Untuk membatalkan tiket yang sudah di pesan
def batalkan_tiket(username):
    hapus()
    # Tampilkan tiket yang dipesan oleh pengguna
    tiket_dipesan(username)
    
    try:
        # Meminta ID tiket yang ingin dibatalkan
        print(style.CBLUE + "\n=== Batalkan Tiket ===" + style.ENDC)
        id_tiket = int(input(style.CWHITE + "Masukkan ID tiket yang ingin dibatalkan: " + style.ENDC))
        
        # Memeriksa apakah ID tiket ada di dalam data pemesanan pengguna
        tiket_dipesan_oleh_pengguna = [pemesanan for pemesanan in data_pemesanan if pemesanan["username"] == username and pemesanan["ID_Tiket"] == id_tiket]
        
        if not tiket_dipesan_oleh_pengguna:
            print(style.CRED + "\nTiket yang Anda pilih tidak ada dalam pemesanan Anda." + style.ENDC)
            input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
            return
        
        # Jika tiket ditemukan, batalkan pemesanan
        for pemesanan in tiket_dipesan_oleh_pengguna:
            # Menambahkan kembali jumlah kursi yang dibatalkan ke tiket yang tersedia
            tiket_kereta[pemesanan["ID_Tiket"]]["kursi"] += pemesanan["jumlah_tiket"]
            # Menghapus pemesanan dari data_pemesanan
            data_pemesanan.remove(pemesanan)

        print(style.CGREEN + "\nTiket berhasil dibatalkan dan jumlah kursi diperbarui!" + style.ENDC)
        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
    
    except ValueError:
        print(style.CRED + "\nInput tidak valid! Harap masukkan angka." + style.ENDC)
        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)


while True:
    tampilan_awal()
    
    try:
        pilihan = int(input("Pilih menu anda: "))
    except ValueError:
        print(style.CRED + "\nInput tidak valid. Tolong Masukkan Angka 1/2/3." + style.ENDC)
        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
        continue  

    if pilihan == 1:
        username = login()
        
        if username:
            while True:
                if username == akun_admin[0]:
                    tampilan_admin()
                    try:
                        status = int(input("Pilih opsi: "))
                    except ValueError:
                        print(style.CRED + "\nInput tidak valid. Silakan masukkan angka yang sesuai." + style.ENDC)
                        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< " + style.ENDC)
                        continue
                    
                    if status == 1:
                        lihat_tiket()
                    elif status == 2:
                        tambah_tiket()
                    elif status == 3:
                        edit_data()
                    elif status == 4:
                        hapus_data()
                    elif status == 5:
                        lihat_data_pemesanan()
                    elif status == 6:
                        break
                    else:
                        print(style.CRED + "\nPilihan tidak valid, coba lagi." + style.ENDC)
                        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< ")
                else:
                    tampilan_pengguna(username)
                    try:
                        status = int(input("Pilih opsi: "))
                    except ValueError:
                        print(style.CRED + "\nInput tidak valid. Silakan masukkan angka yang sesuai.")
                        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< ")
                        continue
                    
                    if status == 1:
                        lihat_tiket()
                    elif status == 2:
                        booking_tiket(username)
                    elif status == 3:
                        tiket_dipesan(username)
                    elif status == 4:
                        batalkan_tiket(username)
                    elif status == 5:
                        break
                    else:
                        print(style.CRED + "\nPilihan tidak valid, coba lagi." + style.ENDC)
                        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< ")
    elif pilihan == 2:
        daftar()
    elif pilihan == 3:
        goodbye()
        break
    else:
        print(style.CRED + "\nPilihan tidak valid, coba lagi." + style.ENDC)
        input(style.CWHITE + "Tekan enter untuk melanjutkan >_< ")