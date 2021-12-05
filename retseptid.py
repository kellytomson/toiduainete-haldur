def lisa_retsept(pealkiri, koostisosad):
    f = open("retseptid.txt", "a", encoding = "UTF-8")
    f.write(pealkiri+','+ koostisosad +"\n")
    f.close()
 
def eemalda_retsept(retsepti_nimi):
    f = open("retseptid.txt", "r+", encoding = "UTF-8")
    read = f.readlines()
    f.seek(0)
    retsepti_nimi = retsepti_nimi.lower()
    for i in read:
            if i.split(",")[0] != retsepti_nimi:
                f.write(i)
    f.truncate()
    f.close()
    
def külmkapi_sisu():#abi fun
    f = open("toiduained.txt", "r", encoding ="UTF-8")
    külmkapis = []
    for rida in f:
        toiduaine = rida.split("  ",1)[0] #hetkel split kahe tühikuga
        külmkapis.append(toiduaine)
    return külmkapis

def leia_retsepti_koostised(retsepti_nimi):#abi funktsioon, mis tagastab retsepti koostisosad
    f = open("retseptid.txt", "r", encoding = "UTF-8")
    read = f.readlines()
    f.seek(0)
    retsepti_nimi = retsepti_nimi.lower()
    for i in read:
            if i.split(",",1)[0] == retsepti_nimi:
                return i.strip().split(",",1)[1].split(",")
    f.close()

def järjend_sõneks(y):#abi fun
    a = ""
    for i in range(len(y)):
        if a == "":
            a += y[i]
        else:
            a = a+", "+y[i]
    return a

def kontrolli_toiduained(retsepti_nimi):
    külmkapp  = külmkapi_sisu()
    koostisosad = leia_retsepti_koostised(retsepti_nimi)
    puuduvad = []
    for el in koostisosad:
        if el not in külmkapp:
            puuduvad.append(el)
    if puuduvad != []:
        print("Puuduvad toiduained on:", järjend_sõneks(puuduvad))
    else:
        print("Kõik on olemas")
        
def vaata_retsepte():
    f = open("retseptid.txt", "r", encoding = "UTF-8")
    for rida in f:
        print(rida.strip().replace(",",":",1))
    f.close()
