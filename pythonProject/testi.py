rahaa_taskussa = int(input("paljonko sinulla on rahaa?"))
maistuuko_kahvi = input("Maistuuko kahvi? ")
laten_hinta = 5
kahvin_hinta = 3

if rahaa_taskussa >= laten_hinta and maistuuko_kahvi == "joo":
    print("Osta latte")
    print("juo latte")
    rahaa_taskussa = rahaa_taskussa - laten_hinta
elif rahaa_taskussa >= kahvin_hinta:
    print("osta normikahvi")
    rahaa_taskussa = rahaa_taskussa - kahvin_hinta
else:
    print("lähden kotiin")

if rahaa_taskussa == 0:
    print("rahat loppu")
else:
    print(f"Sinulla on vielä {rahaa_taskussa} euroa taskusa.")