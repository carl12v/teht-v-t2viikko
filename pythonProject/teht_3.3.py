gender = input("Sukupuolesi (nainen/mies)? ")
hg_value = int(input("Hemoglobiinisi (g/l)? "))

if gender == "nainen":
    if not (5 < hg_value < 300):
        print("virheellinen arvo")
    if hg_value < 117:
        print("Hemoglobiili arvo on alhainen")
    elif hg_value <= 175:
        print("Hg-arvo normaali.")
    else:
        print("Hemoglobiilim arvo on korkea")

elif gender == "mies":
    if not (5 < hg_value < 300):
        print("virheellinen arvo")
    if hg_value < 134:
        print("Hemoglobiili arvo on alhainen")
    elif hg_value <= 195:
        print("Hemoglobiili arvo on normaali")
    else:
        print("Hemoglobiili arvo on korkea")