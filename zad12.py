czipsy = {'name':'lays',
            'waga': 100,
            'smak': 'zielona cebulka'}
def print_dict(d):
    for key in czipsy:
        print("{0}:{1}".format(key, czipsy[key]))

if __name__ == "__main__":
    czipsy = {'name':'lays',
            'waga': 100,
            'smak': 'zielona cebulka'}

print_dict(czipsy)
