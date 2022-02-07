from cmath import sqrt

meno = input("vytajte v kalkulačke.\nZadajte vaše meno: ")

def kontrola(cislo):
    try:
        float(cislo)
        is_it = True
    except ValueError:
        is_it = False
    
    if is_it == False:
        print(f"{meno},MUSÍTE ZADAŤ ČÍSLO!!!")
        quit()
  
class priklad:
    def __init__(self,cislo1,cislo2,znamienko):
        self.cislo1 = cislo1 
        self.cislo2 = cislo2
        self.znamienko = znamienko

while True:
    a = (input("Zadajte prvé číslo: "))
    kontrola(a)
    b = (input("Zadajte druhé číslo: "))
    kontrola(b)
    c = (input("Zadajte číslo operácie \n1)_+_\n2)_-_\n3)_*_\n4)_/_\n5)_^_\n6_√/"))
    kontrola(c)

    p1 = priklad(a,b,c)

    if int(p1.znamienko) == 1:
        print (f"{float(p1.cislo1)} + {float(p1.cislo2)} = ",float(p1.cislo1) + float(p1.cislo2))
    elif int(p1.znamienko) == 2:
        print (f"{p1.cislo1} - {p1.cislo2} = ",p1.cislo1 - p1.cislo2)
    elif int(p1.znamienko) == 3:
        print (f"{p1.cislo1} * {p1.cislo2} = ",p1.cislo1 * p1.cislo2)
    elif int(p1.znamienko) == 4:
        print (f"{float(p1.cislo1)} / {float(p1.cislo2)} = ",float(p1.cislo1) / float(p1.cislo2))
    elif int(p1.znamienko) == 5:
        print (f"{float(p1.cislo1)} ^ {float(p1.cislo2)} = ",float(p1.cislo1) ** float(p1.cislo2))
    elif int(p1.znamienko) == 6:
        print (f"√{float(p1.cislo1)} = ",sqrt(float(p1.cislo1)),f"\n√{float(p1.cislo2)} = ",sqrt(float(p1.cislo2)))
    else:
        print("musíte zadať číslo od 1 do 6")
        quit()
    pokracovanie = str(input(f"{meno} želáte si pokračovať?\n1.)áno\n2.)nie "))
    if pokracovanie == "nie" or "2":
        break
    
    elif pokracovanie != "nie" or "2" or "nn":
        print("tak podme na to")