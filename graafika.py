# Toiduainete haldur
# Siin failis toimub ainult visuaalne osa
from tkinter import *
from tkinter import ttk


# Aken toiduainetega tegelemiseks
def ava_toiduainete_aken():
    toiduainete_aken = Toplevel(root)
    toiduainete_aken.title('Toiduained')
    toiduainete_aken.geometry('200x200')
    ttk.Label(toiduainete_aken, text="See on toiduainete aken").grid(column=5, row=2)
    ttk.Label(toiduainete_aken, text="Mida soovid teha?").grid(column=5, row=3)
    ttk.Button(toiduainete_aken, text="Lisada", command=None).grid(column=5, row=4)
    ttk.Button(toiduainete_aken, text="Eemaldada", command=None).grid(column=5, row=5)


# Aken retseptidega tegelemiseks
def ava_retseptide_aken():
    retseptide_aken = Toplevel(root)
    retseptide_aken.title('Retseptid')
    retseptide_aken.geometry('200x200')
    ttk.Label(retseptide_aken, text="See on retseptide aken").grid(column=5, row=2)
    ttk.Label(retseptide_aken, text="Mida soovid teha?").grid(column=5, row=3)
    ttk.Button(retseptide_aken, text="Lisada", command=None).grid(column=5, row=4)
    ttk.Button(retseptide_aken, text="Eemaldada", command=None).grid(column=5, row=5)


# Põhiaken
root = Tk()
root.geometry('200x200')
raam = ttk.Frame(root, padding=10)
raam.grid()
ttk.Label(raam, text="Toiduainete haldur").grid(column=5, row=2)
ttk.Button(raam, text="Toiduained", command=ava_toiduainete_aken).grid(column=5, row=3)
ttk.Button(raam, text="Retseptid", command=ava_retseptide_aken).grid(column=5, row=4)

root.mainloop()
