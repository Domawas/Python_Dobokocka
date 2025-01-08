from random import randint

def dobas(dobasok, db=23000):
    i = 0
    while i < db:
        dob1 = randint(1, 6)
        dob2 = randint(1, 6)
        dobasok.append(dob1 + dob2) 
        i += 1

def statisztika(dobasok):
    
    elofordulas = [0] * 11 
    for dob in dobasok:
        elofordulas[dob - 2] += 1 

    max_dobas = max(elofordulas)  

    for i in range(2, 13):  
        if elofordulas[i - 2] > 0:  
            csillagok = '*' * (elofordulas[i - 2] * 50 // max_dobas) 
            
            print(f"{i:2} {csillagok:<50} ({elofordulas[i - 2]:>4} db)")
