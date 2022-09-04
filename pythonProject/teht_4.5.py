username = input("Kirjoita käyttäjä nimesi : ")
password = input("Kirjoita salsanasi : ")
print ("Päivää," , username, "Olet nyt kirjautunut sisään")

command = input("kirjoita komento :")
if command == "Kirjaudu ulos":
    print ("Sinut on nyt kirjauduttu ulos",username)
    username == ""
    password == ""

username = input("Kirjoita käyttäjä nimesi : ")
password = input("Kirjoita salsanasi : ")

while (username != "username" and password != "password"):

    print (" Salasanasi ja käyttäjäsi ovat väärin ole hyvä ja kirjoita uudelleen ")
    username = input("Kirjoita käyttäjä nimesi : ")
    password = input("Kirjoita salsanasi : ")

else:
    print ("Päivää," , username, "Olet nyt kirjatunut sisään salasanallasi")