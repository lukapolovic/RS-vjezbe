godina = int(input("Unesite godinu: "))

if(((godina % 4 == 0) & (godina % 100 != 0)) | (godina % 400 == 0)):
    print(f"Godina {godina}. je prijestupna")
else:
    print(f"Godina {godina}. nije prijestupna")