auto1= {'opel': 9,
        'kia': 7}
cena_paliwa = 5.01

while True:
    auto = raw_input("Podaj swoja marke samochodu: ")
    if auto in auto1:
        print("podaj ile przejechales ")
        ile_km = raw_input(": ")
        wynik = float(((ile_km)*9/100)*cena_paliwa)
        print(wynik)
        #else
        #print("nie ma takiego auta ")
