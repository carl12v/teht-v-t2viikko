def CheckLeap(Year):
  if((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):
    print("Vuosi on karkaus vuosi");
  else:
    print ("Vuosi ei ole karkaus vuosi")
Year = int(input("Kirjoita vuosi: "))
CheckLeap(Year)