
def main():
    koszyk = [
        {"nazwa" : "chleb" , "cena" : 2},
        {"nazwa" : "maslo" , "cena" : 4},
        {"nazwa" : "ciastka" , "cena" : 6},
        {"nazwa" : "czekolada" , "cena" : 2},
        {"nazwa" :"piwo", "cena" : 1},
        ]
    f = open("koszyk.csv" , "w")
    sum_prod = 0
    for p in koszyk:
        sum_prod = sum_prod + p["cena"]
        linia = (p["nazwa"] + ' ' + str(p["cena"]))
        f.write(linia)
    print("suma produktow to: " + str(sum_prod))

    f.close()

if __name__ == "__main__":
    main()
