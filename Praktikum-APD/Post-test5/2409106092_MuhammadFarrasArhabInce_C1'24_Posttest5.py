accounts = []
Tiket_Wisata = []

# Menambahkan Warna
class style():
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

while True:
    print(style.CRED + "====================================================================================================")
    print(style.CWHITE + "Selamat datang di pembelian tiket wisata!!")
    print("Silahkan pilih 'Daftar akun' jika belum membuat akun, dan jika sudah memiliki akun silahkan login")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print(style.CRED + "====================================================================================================")
    pilihan = input(style.CBLUE + "Pilih opsi : ")
    print(" ")

    if pilihan == "1":
        print(style.CRED + "================================")
        print(style.CWHITE + "Halo Pengguna Baru :)")
        print("Mari buat Akun terlebih dahulu!")
        print(style.CRED + "================================")
        Username = input(style.CWHITE + "Username: ")
        accountt = False
        for account in accounts:
            if account[0] == Username:
                accountt = True
                break
        if accountt:
            print(style.CRED2 + "Nama sudah terpakai untuk registrasi silahkan coba lagi")
        else:
            Password = input(style.CWHITE + "Password: ")
            Role = input("Masukkan Role (admin/pengguna): ")
            if Role not in ['admin', 'pengguna']:
                print(style.CRED2 + "Peran tidak valid, Anda 'admin' atau 'pengguna'??")
                print(" ")
                continue
            accounts.append([Username, Password, Role, []])
            print(style.CGREEN + f"Yayyy! Anda berhasil terdaftar sebagai {Role}, dengan Username {Username}")
            print(" ")

    elif pilihan =="2":
        print(style.CRED + "==========================")
        print(style.CWHITE + "HI! Yuk login dulu :)")
        Username = input("Username: ")
        Password = input("Password: ")
        print(style.CRED + "==========================")
        print(" ")
        for account in accounts:
            if account[0] == Username and account[1] == Password:
                while True:
                    print(style.CRED + "========================================")
                    print(style.CWHITE + f"Selamat datang {Role} {Username}!")
                    print("Silahkan Pilih")
                    if account[2] == 'admin':
                        print("1. Tambah Destinasi")
                        print("2. Lihat Destinaasi")
                        print("3. Edit Destinasi")
                        print("4. Hapus Destinasi")
                    else:
                        print(style.CWHITE + "1. Beli tiket Masuk")
                        print("2. Lihat tiket Masuk yang sudah dibeli")
                        print("3. Lihat Destinasi Wisata")
                    print("5. Exit")
                    print(style.CRED + "========================================")

                    status = input(style.CBLUE + "Pilih opsi: ")
                    print(" ")

                    if status == "1":
                        if account[2] == 'admin':
                            print(style.CRED + "===========================")
                            Destinasi_Wisata = input(style.CWHITE + "Destinasi: ")
                            Lokasi_Wisata = input("Lokasi Wisata: ")
                            Harga_Tiket = input("Harga Tiket Masuk: ")
                            print(style.CRED + "===========================")
                            Tiket_Wisata.append([Destinasi_Wisata, Lokasi_Wisata, Harga_Tiket])  
                            print(style.CGREEN + "Wisata berhasil ditambahkan :)!\n")
                        else:
                            Destinasi_Wisata = input("Destinasi: ")
                            for tiket in Tiket_Wisata:
                                if tiket[0] == Destinasi_Wisata:
                                   account[3].append([Destinasi_Wisata, tiket[1], tiket[2]])  
                                   print(style.CGREEN + "Tiket Wisata berhasil dibeli :)!\n")
                                   break
                            else:
                                print(style.CRED2 + "Destinasi tidak tersedia.\n")

                    elif status == "2":
                        if account[2] == 'admin':
                            for tiket in Tiket_Wisata:  
                                print(style.CRED + "==========================================")
                                print(style.CWHITE + f"Destinasi: {tiket[0]}\nLokasi Wisata: {tiket[1]}\nHarga Tiket Masuk: {tiket[2]}")
                                print(style.CRED + "==========================================")
                                print(" ")
                            if not Tiket_Wisata:
                                print(style.CRED2 + "Waduh... saat ini belum ada Destinasi yang tersedia, silahkan tambah Destinasi terlebih dahulu.\n")
                        else:
                            for tiket in account[3]:
                                print(style.CRED + "==========================================")  
                                print(style.CWHITE + f"Destinasi: {tiket[0]}\nLokasi Wisata: {tiket[1]}\nHarga Tiket Masuk: {tiket[2]}")
                                print(style.CRED + "==========================================")
                                print(" ")
                            if not account[3]:
                                print(style.CRED2 + "Waduh... saat ini kamu belum mempunyai tiket, silahkan beli tiket terlebih dahulu.\n")
                    elif status == "3":
                        if account[2] == 'admin':
                            if not Tiket_Wisata:
                                print(style.CRED2 + "Tidak ada Destinasi yang bisa diedit.")
                            else:
                                edit = int(input(style.CYELLOW + "Destinasi nomor berapa yang ingin kamu edit: ")) - 1
                                if 0 <= edit < len(Tiket_Wisata):
                                    print(style.CRED + "==========================================")
                                    Destinasi_Baru = input(style.CWHITE + "Masukkan Destinasi yang baru: ")
                                    Lokasi_Baru = input("Masukkan lokasi yang baru: ")
                                    Harga_Baru = input("Masukkan harga yang baru: ")
                                    print(style.CRED + "==========================================")
                                    print(style.CWHITE + "Apa kamu yakin ingin mengedit Destinasi ?")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    print(style.CRED + "==========================================")
                                    Memastikan_Edit = input(style.CBLUE + "Pilih: ")
                                    if Memastikan_Edit == "1":
                                        Tiket_Wisata[edit] = [Destinasi_Baru, Lokasi_Baru, Harga_Baru]
                                        print(style.CGREEN + "Destinasi yang kamu pilih sudah di edit! :)\n")
                                    elif Memastikan_Edit == "2":
                                        print(style.CRED2 + "Aksi untuk mengedit Destinasi dibatalkan")
                                        print(" ")
                                    else:
                                        print(style.CRED2 + "Tolong pilih '1' atau '2'")
                                else:
                                    print(style.CRED2 + "Tidak ada nomor Destinasi yang kamu pilih, silahkan input ulang.\n")
                        else:
                            for tiket in Tiket_Wisata:
                                print(style.CRED + "==========================================")
                                print(style.CWHITE + f"Destinasi: {tiket[0]}\nLokasi Wisata: {tiket[1]}\nHarga Tiket Masuk: {tiket[2]}")
                                print(style.CRED + "==========================================")
                                print(" ")
                            if not Tiket_Wisata:
                                print(style.CRED2 + "Waduh saat ini belum ada Destinasi yang tersedia.\n")

                    elif status == "4":
                        if account[2] == 'admin':
                            if not Tiket_Wisata:
                                print(style.CRED2 + "Tidak ada Destinasi yang bisa dihapus.")
                            else:
                                hapus = int(input(style.CYELLOW + "Destinasi nomor berapa yang ingin dihapus?: ")) - 1
                                if 0 <= hapus < len(Tiket_Wisata):
                                    print(" ")
                                    print(style.CRED + "=============================================")
                                    print(style.CWHITE + "Apa kamu yakin ingin menghapus Destinasi? ")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    print(style.CRED + "=============================================")
                                    Memastikan_Hapus = input(style.CBLUE + "Pilih: ")
                                    if Memastikan_Hapus == "1":
                                        del Tiket_Wisata[hapus] 
                                        print(style.CGREEN + "Destinasi yang kamu pilih sudah dihapus!\n")
                                    elif Memastikan_Hapus == "2":
                                        print(style.CYELLOW + "Aksi untuk menghapus Destinasi dibatalkan")
                                    else:
                                        print(style.CRED2 + "Mohon pilih '1' atau '2'")
                                else:
                                    print(style.CRED2 + "Tidak ada nomor Destinasi yang kamu maksud, silahkan input ulang.\n")
                        else:
                            print(style.CRED2 + "Maaf, Tidak ada aksi yang bisa anda lakukan.\n")
                    
                    elif status == "5":
                        print(style.CRED2 + "Aplikasi Pembelian Tiket Wisata ditutup.\n")
                        break

                    else:
                        print(style.CRED2 + "Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
                break
        else:
            print(style.CRED2 + "Username dan password anda salah :( silahkan coba lagi\n")

    elif pilihan == "3":
        print(style.CRED + "=================================================")
        print(style.CWHITE + "Apakah kamu yakin ingin keluar dari aplikasi? ")
        print("1. Iya")
        print("2. Tidak")
        print(style.CRED + "=================================================")
        pilih = input(style.CBLUE + "Input pilihan: ")
        print(" ")
        if pilih == "1":
            print(style.CYELLOW + "Terimakasih sudah menggunakan aplikasi, semoga harimu menyenangkan! XD")
            break
        elif pilih == "2":
            continue
        else:
            print(style.CRED2 + "Input tidak valid, silahkan pilih '1' atau '2'\n")
    else:
        print(style.CRED2 + "Input tidak valid, silahkan pilih 1, 2, atau 3\n")