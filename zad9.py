samochody =['syrena', 'poloneza', 'opel', 'mazda']

print(samochody[0])
print(samochody[1])

for s in samochody:
    print(s)

for idx in range( len(samochody)):
    print("idx: " + str(idx) + " : " + samochody[idx])

print (samochody[3])

l = samochody[2:]
for s in samochody[2]:
    print(s)
