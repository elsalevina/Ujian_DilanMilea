# NOMOR 3 : JARAK DILAN & MILEA

import requests
import json

#cari kode provinsi
url_kodeprov = "https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json"
data_kodeprov = requests.get(url_kodeprov)

kodeprov = data_kodeprov.json()
kodeprov_keys = list(kodeprov.keys())
kodeprov_values = list(kodeprov.values())
kodeprov_new = dict(zip(kodeprov_values,kodeprov_keys))

# Cari kode provinsi Dilan
Dilan = {
    "Kelurahan": "SAMPORA", #urban
    "Kecamatan": "CISAUK",  #sub_district
    "Kabupaten": "TANGERANG", #city
    "Provinsi": "BANTEN"   
}

kodeprov_Dilan = kodeprov_new[Dilan["Provinsi"]]
# print(kodeprov_Dilan) #36

# Cari kode provinsi Milea
Milea = {
    "Kelurahan": "CITARUM",
    "Kecamatan": "BANDUNG WETAN",
    "Kabupaten": "BANDUNG",
    "Provinsi": "JAWA BARAT"
}

kodeprov_Milea = kodeprov_new[Milea["Provinsi"]]
# print(kodeprov_Milea) #32


# Data lain

url_kodepos = "https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json"
data_kodepos = requests.get(url_kodepos)

kodepos = data_kodepos.json()
kodepos_provDilan = kodepos[kodeprov_Dilan]
kodepos_provMilea = kodepos[kodeprov_Milea]

# cari kode pos Dilan
for i in range(len(kodepos_provDilan)):
    if kodepos_provDilan[i]["urban"] == Dilan["Kelurahan"] and kodepos_provDilan[i]["sub_district"] == Dilan["Kecamatan"] and kodepos_provDilan[i]["city"] == Dilan["Kabupaten"]:
        kodeposDilan = kodepos_provDilan[i]["postal_code"]

# cari kode pos Milea
for i in range(len(kodepos_provMilea)):
    if kodepos_provMilea[i]["urban"] == Milea["Kelurahan"] and kodepos_provMilea[i]["sub_district"] == Milea["Kecamatan"] and kodepos_provMilea[i]["city"] == Milea["Kabupaten"]:
        kodeposMilea = kodepos_provMilea[i]["postal_code"]

# Jarak antara Dilan dan milea
url_jarak = "https://www.zipcodeapi.com/rest/S6swoDDV3B05dhdN3rIfaZJuqVari8LjRdkJb7J5S6RK27L49hLYrd4z100Jb5dF/distance.json/"
data_jarak = requests.get(url_jarak+kodeposDilan+'/'+kodeposMilea+'/km')

jarak = data_jarak.json()
jarakDilanMilea = jarak['distance']

print(f"Kode Pos lokasi Dilan adalah {kodeposDilan}")
print(f"Kode Pos lokasi Milea adalah {kodeposMilea}")
print(f"Jarak Dilan & Milea adalah {jarakDilanMilea} km")