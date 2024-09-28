attemps = 0
while attemps < 3:
    username = input("Masukkan Username Anda : ")
    password = int(input("Masukkan Password Anda : "))
    if username == "paras" and password == 92:
        lanjut = input("ingin lanjut atau berhenti?")
        if lanjut == "berhenti":
            print("program sudah dihentikan")
        else:
            print("Anda berhasil :)")
        hari = str(input("Masukkan hari yang anda inginkan : "))
        uang = int(input("berapa uang yang anda miliki? : "))
        if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis":
            if uang >= 40000:
                print(f"yayy! {username}, anda dapat membeli tiket di hari {hari}")
                break
            else:
                print(f"yahh.. {username}, uang anda tidak cukup untuk hari {hari} :(")
                break
        elif hari == "jumat":
            if uang >= 45000:
                print(f"yayy! {username}, anda dapat membeli tiket di hari jumat")
                break
            else:
                print(f"yahh.. {username}, uang anda tidak cukup untuk hari jumat :(")
                break
        elif hari == "sabtu":
            if uang >= 50000:
                print(f"yayy! {username}, anda dapat membeli tiket di hari sabtu")
                break
            else:
                print(f"yahh.. {username}, uang anda tidak cukup untuk hari sabtu :(")
                break
        elif hari == "minggu":
            if uang >= 55000:
                print(f"yayy! {username}, anda dapat membeli tiket di hari minggu")
                break
            else:
                print(f"yahh.. {username}, uang anda tidak cukup untuk hari minggu :(")
                break
        else:
            print("nama hari yang anda masukkan tidak valid")
            break
    else:
        print("username atau password yang anda masukkan salah")
        lanjut = input("ingin lanjut atau berhenti? : ")
        if lanjut == "berhenti":
            print("program sudah dihentikan")
        else:
            attemps = attemps + 1
            print(f"percobaan yang sudah anda lakukan adalah {attemps} kali")
