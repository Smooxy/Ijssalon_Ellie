def mijn_functie_1(argument):
    return argument ** 2


print (mijn_functie_1(2))
print (mijn_functie_1(4))
print (mijn_functie_1(10))
print (mijn_functie_1(12))

def mijn_functie_2(argument1, argument2):
    return [
        argument1 + argument2,
        argument1 - argument2,
        argument1 * argument2,
        argument1 // argument2, # met 1x "/" (argument1 / argument2,) krijg ik een float
    ]

print(mijn_functie_2(12,3))
print(mijn_functie_2(12,2))
print(mijn_functie_2(10,5))
print(mijn_functie_2(100,20))