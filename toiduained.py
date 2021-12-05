# Siin failis toimub kõik toiduainetega seoses
import datetime
import os

#võtab filepathiks antud faili kausta 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def lisa_toode(uus_toode, aasta, kuu, päev):
    kuupäev = str(datetime.date(aasta, kuu, päev))
    kuupäev_täna = str(datetime.date.today())
    rida = uus_toode + ' ' + ' ostetud:' + kuupäev_täna + ' aegub:' + kuupäev
    # Kirjutame uue toiduaine koos aegumis-kuupäevaga faili
    fail = open('toiduained.txt', 'a', encoding='utf-8')
    fail.write('\n' + rida)
    fail.close()
    print('Toode lisatud!')

def eemalda_toode(ei_toode):
    fail = open('toiduained.txt', 'r+', encoding='utf-8')
    read = fail.readlines()
    fail.seek(0)
    for rida in read:
        tooted = rida.split()
        toode = tooted[0]
        if toode != ei_toode:
            fail.write(rida)
    # 'truncate' eemaldab kõik faili lõppu jäänud ülearused read
    fail.truncate()
    fail.close()
    print('Toode eemaldatud!')

def eemalda_kõik_aegunud():
    fail = open('toiduained.txt', 'r+', encoding='utf-8')
    read = fail.readlines()
    fail.seek(0)
    for rida in read:
        rida_copy = rida
        kuupäev = rida.split()[2].split(':')[1].split('-')
        kuupäev = datetime.date(int(kuupäev[0]), int(kuupäev[1]), int(kuupäev[2]))
        kuupäev_täna = datetime.date.today()
        # Jätame alles ainult tooted, mille säilivuskuupäev ei ole veel ületanud tänast päeva
        if kuupäev > kuupäev_täna:
            fail.write(rida_copy)
    fail.truncate()
    fail.close()

def eemalda_tooted_retsepti_järgi(koostisosad):
    for el in koostisosad:
        eemalda_toode(el)
 