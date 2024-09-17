nama = "Muhammad Farras Arhab Ince"
nim  = "2409106092"
hargagula = 21000

Diskon = {
    "diskon_gulaku" : 0.07,
    "diskon_manis_kita" : 0.11,
    "diskon_gunung_madu" : 0.13
}

diskongulaku = hargagula * Diskon["diskon_gulaku"]
diskonmaniskita = hargagula * Diskon["diskon_manis_kita"]
diskongunungmadu = hargagula * Diskon["diskon_gunung_madu"]

HSDgulaku = hargagula - diskongulaku
HSDmaniskita = hargagula - diskonmaniskita
HSDgunungmadu = hargagula - diskongunungmadu

print(f"{nama} dengan NIM {nim} ingin membeli gula seharga Rp {hargagula}")
print(f"jika dia membeli Gulaku ia harus membayar {HSDgulaku} setelah mendapat diskon 7%")
print(f"jika dia membeli Manis Kita ia harus membayar {HSDmaniskita} setelah mendapat diskon 11%")
print(f"jika dia membeli Gunung Madu ia harus membayar {HSDgunungmadu} setelah mendapat diskon 13%" )
