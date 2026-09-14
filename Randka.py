print("Czy zaprosze cie na randke")

imie = str(input("imie: "))

wiek = int(input("wiek: "))
if wiek < 13:
    waga = int(input("waga: "))
    if waga < 60:
        wzrost = float(input("wzrost: "))
        if wzrost < 190:
            czylubi_anime = int(input("czy lubi anime - 0/1: "))
            if czylubi_anime == 1:
                print("zapraszam na randke")
            else:
                print("podaj insta")
        else:
            print("nie ma opcji")
    else:
        print("wykluczone")            
else:
    print("no chyba zartujesz")
