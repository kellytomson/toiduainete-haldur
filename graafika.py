# Toiduainete haldur
# Siin failis toimub ainult visuaalne osa
from tkinter import *
from tkinter import ttk
from retseptid import *
from toiduained import *
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
praegune_aken = None

# Toiduainete aken ##########################################################################################################

def ava_toiduainete_aken():
    global praegune_aken

    toiduainete_aken = root
    praegune_aken = toiduainete_aken
    raam.destroy()
    toiduainete_aken.title('Toiduained')
    toiduainete_aken.geometry('200x200')
    ttk.Label(toiduainete_aken, text="See on toiduainete aken").grid(column=5, row=2)
    ttk.Label(toiduainete_aken, text="Mida soovid teha?").grid(column=5, row=3)
    ttk.Button(toiduainete_aken, text="Lisada", command=lisa_toode_aken).grid(column=5, row=4)
    ttk.Button(toiduainete_aken, text="Eemaldada", command=eemalda_toode_aken).grid(column=5, row=5)
    ttk.Button(toiduainete_aken, text="Eemaldada kõik aegunud tooted", command=eemalda_kõik_aegunud).grid(column=5, row=6)
    ttk.Button(toiduainete_aken, text="Tagasi", command=põhiaken).grid(column=5, row=7)

# Retseptide aken ############################################################################################################

def ava_retseptide_aken():
    global praegune_aken

    retseptide_aken = root
    praegune_aken = retseptide_aken
    raam.destroy()
    retseptide_aken.title('Retseptid')
    retseptide_aken.geometry('200x200')
    ttk.Label(retseptide_aken, text="See on retseptide aken").grid(column=5, row=2)
    ttk.Label(retseptide_aken, text="Mida soovid teha?").grid(column=5, row=3)
    ttk.Button(retseptide_aken, text="Lisada", command=lisa_retsept_aken).grid(column=5, row=4)
    ttk.Button(retseptide_aken, text="Eemaldada", command=None).grid(column=5, row=5)
    ttk.Button(retseptide_aken, text="Vaata retsepte", command=vaata_retsepte_aken).grid(column=5, row=5)
    ttk.Button(retseptide_aken, text="Tagasi", command=põhiaken).grid(column=5, row=6)

# Põhiaken ###################################################################################################################

def põhiaken():
    global root, raam, pealkiri, button1, button2

    if praegune_aken is not None:
        praegune_aken.destroy()
    root = Tk()
    root.geometry('200x200')
    raam = ttk.Frame(root, padding=10)
    raam.grid()
    pealkiri = ttk.Label(raam, text="Toiduainete haldur").grid(column=5, row=2)
    ttk.Button(raam, text="Toiduained", command=ava_toiduainete_aken).grid(column=5, row=3)
    ttk.Button(raam, text="Retseptid", command=ava_retseptide_aken).grid(column=5, row=4)
    return root

# Lisa toode aken #############################################################################################################

def lisa_toode_aken():
    lisa_toode_aken = Toplevel(root)
    lisa_toode_aken.title('Lisa toode')
    lisa_toode_aken.geometry('400x200')

    ttk.Label(lisa_toode_aken, text='Toote nimi: ').grid(column=5, row=2) 
    sisend1 = ttk.Entry(lisa_toode_aken)
    sisend1.grid(column=8, row=2)

    ttk.Label(lisa_toode_aken, text='Aegub: ').grid(column=5, row=4)
    sisend2 = ttk.Entry(lisa_toode_aken)
    sisend2.grid(column=8, row=4)

    ttk.Label(lisa_toode_aken, text='Kuupäev tuleb lisada kujul 31.12.2021').grid(column=5, row=5)

    def toote_lisamine():
        toode = sisend1.get()
        kuupäev = sisend2.get().split('.')
        lisa_toode(toode, int(kuupäev[2]), int(kuupäev[1]), int(kuupäev[0]))
        
    ttk.Button(lisa_toode_aken, text="Enter", command=toote_lisamine).grid(column=5, row=6)

# Eemalda toode aken ###########################################################################################################

def eemalda_toode_aken():
    eemalda_toode_aken = Toplevel(root)
    eemalda_toode_aken.title('Eemalda toode')
    eemalda_toode_aken.geometry('200x200')
    sisend = ttk.Entry(eemalda_toode_aken)
    sisend.grid(column=8, row=2)
    
    def toote_eemaldamine():
        toode = sisend.get()
        eemalda_toode(toode)

    ttk.Button(eemalda_toode_aken, text="Enter", command=toote_eemaldamine).grid(column=5, row=6)   

# Lisa retsept aken ############################################################################################################

def lisa_retsept_aken():
    lisa_retsept_aken = Toplevel(root)
    lisa_retsept_aken.title('Lisa retsept')
    lisa_retsept_aken.geometry('400x200')
    
    ttk.Label(lisa_retsept_aken, text='Retsepti pealkiri: ').grid(column=5, row=2) 
    ttk.Label(lisa_retsept_aken, text='Retsepti koostisosad: ').grid(column=5, row=3) 
    
    sisend1 = ttk.Entry(lisa_retsept_aken)
    sisend1.grid(column=8, row=2)
    sisend2 = ttk.Entry(lisa_retsept_aken)
    sisend2.grid(column=8, row=3)
    
    def retsepti_lisamine():
        pealkiri = sisend1.get()
        koostisosad = sisend2.get()
        lisa_retsept(pealkiri, koostisosad)
        
    ttk.Button(lisa_retsept_aken, text="Enter", command=retsepti_lisamine).grid(column=5, row=6)

# Vaata retsepte aken ##########################################################################################################

def vaata_retsepte_aken():
    vaata_retsepte_aken = Toplevel(root)
    vaata_retsepte_aken.title('Vaata retsepte')
    vaata_retsepte_aken.geometry('300x300')
    fail = open("retseptid.txt", "r", encoding = "UTF-8")
    i = 0

    for rida in fail:
        i += 1
        rida = rida.strip().replace(",",": ",1)
        ttk.Label(vaata_retsepte_aken, text=rida).grid(column=5, row=i) 

    fail.close()

# Käivitame põhiakna ###########################################################################################################
põhiaken().mainloop()