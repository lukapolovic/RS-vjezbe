pozivni_brojevi = {
    "01": {"mjesto": "Grad Zagreb i Zagrebačka županija", "vrsta": "Fiksna mreža"},
    "020": {"mjesto": "Dubrovačko-neretvanska županija", "vrsta": "Fiksna mreža"},
    "021": {"mjesto": "Splitsko-dalmatinska županija", "vrsta": "Fiksna mreža"},
    "022": {"mjesto": "Šibensko-kninska županija", "vrsta": "Fiksna mreža"},
    "023": {"mjesto": "Zadarska županija", "vrsta": "Fiksna mreža"},
    "031": {"mjesto": "Osječko-baranjska županija", "vrsta": "Fiksna mreža"},
    "032": {"mjesto": "Vukovarsko-srijemska županija", "vrsta": "Fiksna mreža"},
    "033": {"mjesto": "Virovitičko-podravska županija", "vrsta": "Fiksna mreža"},
    "034": {"mjesto": "Požeško-slavonska županija", "vrsta": "Fiksna mreža"},
    "035": {"mjesto": "Brodsko-posavska županija", "vrsta": "Fiksna mreža"},
    "040": {"mjesto": "Međimurska županija", "vrsta": "Fiksna mreža"},
    "042": {"mjesto": "Varaždinska županija", "vrsta": "Fiksna mreža"},
    "043": {"mjesto": "Bjelovarsko-bilogorska županija", "vrsta": "Fiksna mreža"},
    "044": {"mjesto": "Sisačko-moslavačka županija", "vrsta": "Fiksna mreža"},
    "047": {"mjesto": "Karlovačka županija", "vrsta": "Fiksna mreža"},
    "048": {"mjesto": "Koprivničko-križevačka županija", "vrsta": "Fiksna mreža"},
    "049": {"mjesto": "Krapinsko-zagorska županija", "vrsta": "Fiksna mreža"},
    "051": {"mjesto": "Primorsko-goranska županija", "vrsta": "Fiksna mreža"},
    "052": {"mjesto": "Istarska županija", "vrsta": "Fiksna mreža"},
    "053": {"mjesto": "Ličko-senjska županija", "vrsta": "Fiksna mreža"},
    "091": {"mjesto": "A1 Hrvatska", "vrsta": "Mobilna mreža"},
    "092": {"mjesto": "Tomato", "vrsta": "Mobilna mreža"},
    "095": {"mjesto": "Telemach", "vrsta": "Mobilna mreža"},
    "097": {"mjesto": "bonbon", "vrsta": "Mobilna mreža"},
    "098": {"mjesto": "Hrvatski Telekom", "vrsta": "Mobilna mreža"},
    "099": {"mjesto": "Hrvatski Telekom", "vrsta": "Mobilna mreža"},
    "0800": {"mjesto": "Besplatni pozivi", "vrsta": "Posebne usluge"},
    "060": {"mjesto": "Komercijalni pozivi", "vrsta": "Posebne usluge"},
    "061": {"mjesto": "Glasovanje telefonom", "vrsta": "Posebne usluge"},
    "064": {"mjesto": "Usluge s neprimjerenim sadržajem", "vrsta": "Posebne usluge"},
    "065": {"mjesto": "Nagradne igre", "vrsta": "Posebne usluge"},
    "069": {"mjesto": "Usluge namijenjene djeci", "vrsta": "Posebne usluge"},
    "072": {"mjesto": "Jedinstveni pristupni broj za cijelu državu za posebne usluge", "vrsta": "Posebne usluge"}
}

def ocisti_broj(broj):
    cisti_broj = "".join(znak for znak in broj if znak.isdigit())

    if cisti_broj.startswith("00385"):
        ostatak = cisti_broj[5:]
        if not ostatak.startswith("0"):
            ostatak = "0" + ostatak
        cisti_broj = ostatak
    
    elif cisti_broj.startswith("385"):
        ostatak = cisti_broj[3:]
        if not ostatak.startswith("0"):
            ostatak = "0" + ostatak
        cisti_broj = ostatak
    
    return cisti_broj

def validiraj_pozivni_broj(broj):
    for pozivni in pozivni_brojevi.keys():
        if broj.startswith(pozivni):
            return pozivni
    return None

def validiraj_broj_telefona(broj):
    cisti_broj = ocisti_broj(broj)
    
    pozivni_broj = validiraj_pozivni_broj(cisti_broj)
    if pozivni_broj is None:
        return {
            "pozivni_broj": None,
            "broj_ostatak": None,
            "vrsta": None,
            "mjesto": None,
            "operater": None,
            "validan": False
        }

    broj_ostatak = cisti_broj[len(pozivni_broj):]
    vrsta = pozivni_brojevi[pozivni_broj]["vrsta"]
    validan = True

    if vrsta == "Posebne usluge":
        if len(broj_ostatak) != 6:
            validan = False
    elif vrsta in ["Fiksna mreža", "Mobilna mreža"]:
        if not (6 <= len(broj_ostatak) <= 7):
            validan = False
    
    if vrsta == "Mobilna mreža":
        mjesto = None
        operater = pozivni_brojevi[pozivni_broj]["mjesto"]
    elif vrsta == "Posebne usluge": 
        mjesto = None
        operater = None
    elif vrsta == "Fiksna mreža":
        mjesto = pozivni_brojevi[pozivni_broj]["mjesto"]
        operater = None

    return {
        "pozivni_broj": pozivni_broj,
        "broj_ostatak": broj_ostatak,
        "vrsta": vrsta,
        "mjesto": mjesto,
        "operater": operater,
        "validan": validan
    }

test_brojevi = [
    "+38591234567",      # ✅ Mobilna mreža, 091 prefix, 7 znamenki -> validan
    "0038595123456",     # ✅ Mobilna mreža, 095 prefix, 6 znamenki -> validan
    "(01)234567",        # ❌ Fiksna mreža, 01 prefix, 6 znamenki -> nevalidan (treba 6-7, ovo je 6, pa može biti validan)
    "080012345",         # ❌ Posebne usluge, 0800 prefix, 5 znamenki -> nevalidan
    "+385 098 123 456",  # ✅ Mobilna mreža, 098 prefix, 6 znamenki -> validan
    "0221234567",        # ✅ Fiksna mreža, 022 prefix, 7 znamenki -> validan
    "065123456",         # ❌ Posebne usluge, 065 prefix, 6 znamenki -> validan
    "00385051123456",    # ✅ Fiksna mreža, 051 prefix, 6 znamenki -> validan
    "00385060123456",    # ✅ Posebne usluge, 060 prefix, 6 znamenki -> validan
    "123456789"          # ❌ Ne postoji prefix -> nevalidan
]


for broj in test_brojevi:
    print(broj)
    print(validiraj_broj_telefona(broj))
    print()
