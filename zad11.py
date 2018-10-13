czipsy = {'name':'lays',
            'waga': 100,
            'smak': 'zielona cebulka'}
for key, value in czipsy.items():
    print("{0}:{1}".format(key, value))


for key in czipsy:
    print("{0}:{1}".format(key, czipsy[key]))
