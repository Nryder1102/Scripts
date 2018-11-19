def batavrg():
    pname = input("What's the Player's name? >")
    hits = eval(input("How many hits? >"))
    atbats = eval(input("How many at-bats? >"))
    avg = hits / atbats
    Pname = pname + "'s"
    print(Pname,"batting average is",avg)

    
