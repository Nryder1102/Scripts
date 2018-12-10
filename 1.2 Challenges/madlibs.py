import random
def madlibs():
    pnone = input("Enter a proper noun(Name): ")
    none = input("Enter 1st noun: ")
    ntwo = input("Enter 2nd noun: ")
    vone = input("Enter 1st verb ending in 'ing': ")
    vtwo = input("Enter 2nd verb ending in 'ing': ")
    aone = input("Enter 1st adjective: ")
    atwo = input("Enter 2nd adjective: ")
    pone = input("Enter 1st place: ")
    ptwo = input("Enter 2nd place: ")

    nlist = [none,ntwo]
    noun = random.choice(nlist)

    vlist = [vone,vtwo]
    verb = random.choice(vlist)

    alist = [aone,atwo]
    adjective = random.choice(alist)

    plist = [pone,ptwo]
    place = random.choice(plist)

    print(pnone,"was", verb,"their",adjective,noun,"to", place,"today.")
