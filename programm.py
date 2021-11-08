from retseptid import *
from toiduained import *

while True:
    print("ava külmkapp = k\nava retseptiraamat = r")
    sisend = input("Sisesta soovitud tegevus: ")
    print()
    
    if sisend == "k":
        while True:
            print("lisa toode = l\neemalda toode = e\neemalda kõik aegunud tooted =a\nlahku külmkapist = h") 
            valik = input("Sisesta soovitud tegevus: ")
            print()
            if valik == "l":
                nimi = input("Sisesta uus toote nimi: ")
                aasta = int(input("Sisesta toote aegumiskuupäeva aasta: "))
                kuu = int(input("Sisesta toote aegumiskuupäeva kuu: "))
                päev = int(input("Sisesta toote aegumiskuupäeva päev: "))
                print()
                lisa_toode(nimi, aasta, kuu, päev)
                
            elif valik == "e":
                toode = input("Sisesta toote nimi, mida soovid eemaldada: ")
                eemalda_toode(toode)
            
            elif valik == "a":
                eemalda_kõik_aegunud()
                
            elif valik == "h":
                break
            
            else:
                print("Vigane sisend")
                print()
                print("Sisendi valikud on:")
        
    elif sisend == "r":
        while True:
            vaata_retsepte()
            print()
            print("lisa retsept = l\neemalda retsept = e\nvaata retsepti koostisosasid = v\nlahku retseptiraamatust = h")
            print()
            valik1 = input("Sisesta soovitud tegevus: ")
            print()
            if valik1 == "l":
               lisa_retsept()
               
            elif valik1 =="e":
                retsept1 = input("Sisesta retsepti nimi, mida soovid kustutada:")
                eemalda_retsept(retsept1)
                
            elif valik1 =="v":
                retsept2 = input("Sisesta retsept, mille koostisosasid soovid teada: ")
                print(järjend_sõneks(leia_retsepti_koostised(retsept2)))
                print()
                kasutad = input("Kas kasutasid retsepti ja soovid need toiduained eemaldada sahvrist?(jah/ei)\n")
                if kasutad == "jah":
                        eemalda_tooted_retsepti_järgi(leia_retsepti_koostised(retsept2))
                            
                elif kasutad =="ei":
                    break
           
                else:
                    print("Vigane sisend")
                    
            elif valik1 == "h":
                    break
                        
            else:
                print("Vigane sisend")
                print()
                print("Sisendi valikud on:")
                
    else:
        print("Vigane sisend")
        print()
        print("Sisendi valikud on:")
        
        