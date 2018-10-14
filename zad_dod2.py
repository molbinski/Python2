samochody =['syrena', 'poloneza', 'opel', 'mazda']


while True:
    twoj_samochod = raw_input("Podaj swoja marke samochodu: ")

    if twoj_samochod in samochody:
        print("tak")
    else:
        print("nie")
