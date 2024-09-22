nama = str(input("masukkan nama anda : "))
hari = str(input("masukkan hari yang anda inginkan : "))
uang = int(input("berapa uang yang anda miliki : "))

if hari == "senin" or "selasa" or "rabu" or "kamis":
    if uang >= 40000:
        print("yayy! anda dapat membeli tiket di hari ")
    else:
        print("yahh uang anda tidak cukup :(")
elif hari == "jumat":
    if uang >= 45000:
        print("yayy! anda dapat membeli tiket di hari {hari}")
    else:
        print("yahh uang anda tidak cukup :(")
elif hari == "sabtu":
    if uang >= 50000:
        print("yayy! anda dapat membeli tiket di hari {hari}")
    else:
        print("yahh uang anda tidak cukup :(")
elif hari == "minggu":
    if uang >= 55000:
        print("yayy! anda dapat membeli tiket di hari {hari}")
    else:
        print("yahh uang anda tidak cukup :(")