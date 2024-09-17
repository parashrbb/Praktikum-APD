nama = "Muhammad Farras Arhab Ince"
nim  = "2409106092"
harga_gula = 21000

Diskon = {
    "diskon_gulaku" : 0.07,
    "diskon_manis_kita" : 0.11,
    "diskon_gunung_madu" : 0.13
}

diskon_gulaku = harga_gula * Diskon["diskon_gulaku"]
diskon_manis_kita = harga_gula * Diskon["diskon_manis_kita"]
diskon_gunung_madu = harga_gula * Diskon["diskon_gunung_madu"]

harga_setelah_diskon_gulaku = harga_gula - diskon_gulaku
harga_setelah_diskon_manis_kita = harga_gula - diskon_manis_kita
harga_setelah_diskon_gunung_madu = harga_gula - diskon_gunung_madu

print(f"{nama} dengan NIM {nim} ingin membeli gula seharga Rp {harga_gula}")
print(f"jika dia membeli Gulaku ia harus membayar {harga_setelah_diskon_gulaku} setelah mendapat diskon 7%")
print(f"jika dia membeli Manis Kita ia harus membayar {harga_setelah_diskon_manis_kita} setelah mendapat diskon 11%")
print(f"jika dia membeli Gunung Madu ia harus membayar {harga_setelah_diskon_gunung_madu} setelah mendapat diskon 13%" )