nama = "Muhammad Farras Arhab Ince"
nim  = "2409106092"
hargagula = 21000

Diskon = {
    "diskongulaku" : 0.07,
    "diskonmaniskita" : 0.11,
    "diskongunungmadu" : 0.13
}

diskongulaku = hargagula * Diskon["diskongulaku"]
diskonmaniskita = hargagula * Diskon["diskonmaniskita"]
diskongunungmadu = hargagula * Diskon["diskongunungmadu"]

HSDgulaku = hargagula - diskongulaku
HSDmaniskita = hargagula - diskonmaniskita
HSDgunungmadu = hargagula - diskongunungmadu

print(f"{nama} dengan NIM {nim} ingin membeli gula seharga Rp {harga_gula}")
print(f"jika dia membeli Gulaku ia harus membayar {HSDgulaku} setelah mendapat diskon 7%")
print(f"jika dia membeli Manis Kita ia harus membayar {HSDmaniskita} setelah mendapat diskon 11%")
print(f"jika dia membeli Gunung Madu ia harus membayar {HSDgunungmadu} setelah mendapat diskon 13%" )
