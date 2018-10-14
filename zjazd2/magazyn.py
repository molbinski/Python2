def tabela():
    magazyn = [
           {"name" : "kabel" , "id": 1 , "masa" : 5.05 , "ilosc" : 2 , "cena" : 12.5},
           {"name" : "radio" , "id": 2 , "masa" : 11.5 , "ilosc" : 1 , "cena" : 85.25},
           {"name" : "kalkulator" , "id": 3 , "masa" : 17.2 , "ilosc" : 1 , "cena" : 0.25},
           {"name" : "lampa" , "id": 4 , "masa" : 48.7 , "ilosc" : 9 , "cena" : 65.8},
           {"name" : "waga" , "id": 5 , "masa" : 45.3 , "ilosc" : 11 , "cena" : 25.0},
           {"name" : "dysk" , "id": 6 , "masa" : 23.9 , "ilosc" : 55 , "cena" : 47.99},
           {"name" : "pendrive" , "id": 7 , "masa" : 75.6 , "ilosc" : 44 , "cena" : 25.99},
           {"name" : "myszka" , "id": 8 , "masa" : 44.4 , "ilosc" : 1 , "cena" : 199.99},
           {"name" : "klawiatura" , "id": 9 , "masa" : 99.9 , "ilosc" : 7 , "cena" : 65.99}
            ]
    return magazyn


#pprint.pprint(magazyn)
def prepare_raport(magazyn):
    total_ilosc = 0
    total_masa = 0
    total_cena = 0

    for poz in magazyn:
        total_ilosc = total_ilosc + poz['ilosc']
        total_masa = total_masa + poz['masa']
        total_cena = total_cena + poz['cena']
    return total_cena, total_masa, total_ilosc

def export_to_file(total_cena, total_masa, total_ilosc):
    print("suma wszystkich produktow to: " + str(total_ilosc))
    print("masa wszystkich produkow to: " + str(total_masa))
    print("cena wszystkich produkow to: " + str(total_cena))

def main():
    magazyn = tabela()
    total_cena, total_masa, total_ilosc = prepare_raport(magazyn)
    export_to_file(total_cena, total_masa, total_ilosc)
if __name__ == "__main__":
    main()
