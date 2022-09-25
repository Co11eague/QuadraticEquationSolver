import re
import sys
from math import *
from tkinter import *
from tkinter import messagebox


# Programa sprendžia kvadratines lygtis, bei iš kai kurių sprendinių sudaro kvadratinę lygtį. Tai pat paaiškinamas sprendimo būdas.
# ___________________________________________________________________________________________________
# Funkcija iškviečia laukelį, kuriame galime pasirinkti ar norime išjungti programą.
def isejimas():
    ats = messagebox.askyesno("Išėjimas", "Ar norite išeiti iš šios programos?")
    if ats:
        pg.destroy()


# ___________________________________________________________________________________________________
# Funkcija, kuri išsprendžia kvadratinę lygtį bei parašo, kaip tai buvo padaryta
def sprendimas(*args):
    # Tikrinama, kad nebūtų raidžių bei simbolių, kaip ;'\]
    try:
        float(variable.get())
        float(variable1.get())
        float(variable2.get())
    except:
        # Jeigu yra tokių simbolių visi skaičiai nunuliuojami, ir parašoma atitinkama eilutė
        eilute = "Įvesti netinkami simboliai"
        if variable.get() != "-" and variable1.get() != "-" and variable2.get() != "-" or re.search('[a-zA-Z]+',
                                                                                                    variable.get()) is not None or re.search(
            '[a-zA-Z]+', variable1.get()) is not None or re.search('[a-zA-Z]+', variable2.get()) is not None:
            variable.set("0")
            variable1.set("0")
            variable2.set("0")
            af.config(text=eilute)
            return
    # Skaičiai įsistatomi į kintamuosius
    a = float(variable.get())
    b = float(variable1.get())
    c = float(variable2.get())
    # Tikrinami ar sveikieji ar ne
    if a % 1 == 0:
        a = int(a)
    if b % 1 == 0:
        b = int(b)
    if c % 1 == 0:
        c = int(c)
    if c == 0 and a != 0:
        x1 = 0.0
        x2 = (-b / a)
        eilute = "Kadangi koficientas c = 0,\ntai susidaro nepilna kvadratinė lygtis:\nax² + bx = 0\nx(ax + b) = 0\n" + str(
            a) + "x² + " + str(b) + "x = 0\nx(" + str(a) + "x + " + str(b) + ") = 0\n" + str(a) + "x + " + str(
            b) + " = 0\n" + str(a) + "x = " + str(-b) + "\n\nx₁ = 0.0\nx₂ = " + str(x2)
    # Jei koficientas b=0 ir negaunamos kompleksinės, naudojame šią formulę.
    elif b == 0 and a != 0 and -(c / a) > 0:
        x1 = -sqrt(-(c / a))
        x2 = -x1
        eilute = "Kadangi koficientas b = 0,\ngauta lygtis sprendžiama taip:\nax² + c = 0\nx² = -(c/a)\nx₁,₂ = √-(c/a)\n" + str(
            a) + "x² + " + str(c) + " = 0\nx² = -(" + str(c) + " / " + str(a) + ")\n\nx₁ = " + str(
            x1) + "\nx₂ = " + str(x2)
    # Jei koficientas a=0, gaunama paprasta lygtelė, kuri išsprendžiama labai paprastai.
    elif a == 0 and b != 0:
        x1 = -c / b
        x2 = x1
        eilute = "Kadangi koficientas a = 0,\ngauta lygtis sprendžiama taip:\nbx + c = 0\nx₁,₂ = -c/b\n\n" + str(
            b) + "x + " + str(c) + " = 0\n" + str(b) + "x = " + str(-c) + "\nx₁ = x₂ = " + str(x1)
    # Patikriname, kad koficientai a ir b nebutų lygūs 0
    elif a == 0 and b == 0:
        eilute = "A ir b koficientai negali būti lygūs 0"
        x1 = "0.0"
        x2 = "0.0"
    # Jeigu nebėra paprastesnių metodų spręsti kvadratinę lygtį, tai įmamės spręsti per diskriminantą
    else:
        D = b ** 2 - 4 * a * c
        # Jei diskriminantas lygus 0 - vienas sprendinys
        if D == 0:
            x1 = -b / (2 * a)
            x2 = x1
            eilute = "Suskaičiuotos kvadratinės lygties\ndiskriminantas lygus 0:\nD = b² - 4ac\nD = " + str(
                b) + "² - 4 * " + str(a) + " * " + str(
                c) + "\nD = 0\n\nTodėl atsakymas gaunamas vienas:\nx₁,₂ = -b/(2a)\nx₁,₂ = " + str(
                -b) + " / (2 * " + str(a) + ")\n\nx₁,₂ = " + str(x1)
        # Jei diskriminantas daugiau negu 0 - du sprendiniai
        elif D > 0:
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)
            eilute = "Suskaičiuotos kvadratinės lygties\ndiskriminantas lygus " + str(
                D) + ":\n" + "D = b² - 4ac\nD = " + str(b) + "² - 4 * " + str(a) + " * " + str(c) + "\nD = " + str(
                D) + "\n\nIš to gaunami du sprendiniai:\nx₁,₂ = (-b ± √D)/(2a)\nx₁ = (" + str(-b) + " + √" + str(
                D) + ") / (2 * " + str(a) + ")\nx₂ = (" + str(-b) + " - √" + str(D) + ") / (2 * " + str(
                a) + ")\n\nx₁ = " + str(x1) + "\nx₂ = " + str(x2)
        # Jei diskriminantas mežiau nei 0 - sprendiniai su kompleksinėmis šaknimis
        else:
            # Suskaičiuojame alfa
            alfa = round(-(b / (2 * a)), 8)
            # Jei koficientas a=1, naudojame paprastesnį sprendimo būdą
            if a == 1:
                beta = round(sqrt(c - alfa ** 2), 8)
                simb = "i"
                eilute = "Suskaičiuotos kvadratinės lygties\ndiskriminantas lygus " + str(
                    D) + ":\n" + "D = b² - 4ac\nD = " + str(b) + "² - 4 * " + str(a) + " * " + str(c) + "\nD = " + str(
                    D) + "\n\nTas reiškia, kad lygties sprendiniai\nbus su kompleksinėmis šaknimis.\nPirma susirandame alfa ir beta:\nα = -(b/(2a)) β = √(c - α²)\nα =" + str(
                    -b) + " / (2 * " + str(a) + ")\nβ = √(" + str(
                    c) + " - α²)\n\nTada surandame lygties sprendinius:\nx₁,₂ = α ± βi\nx₁ = " + str(
                    alfa) + " + " + str(beta) + "i\nx₂ = " + str(alfa) + " + " + str(beta) + "i"
            # Kitaip naudojame eilinį sprendimo būdą
            else:
                beta = round(sqrt(-D) / (2 * a), 8)
                simb = "j"
                eilute = "Suskaičiuotos kvadratinės lygties\ndiskriminantas lygus " + str(
                    D) + ":\n" + "D = b² - 4ac\nD = " + str(b) + "² - 4 * " + str(a) + " * " + str(c) + "\nD = " + str(
                    D) + "\n\nTas reiškia, kad lygties sprendiniai\nbus su kompleksinėmis šaknimis.\nPirma susirandame alfa ir beta:\nα = -(b/(2a)) β = (√(-D))/(2a)\nα =" + str(
                    -b) + " / (2 * " + str(a) + ")\nβ = (√(" + str(-D) + "))/(2 * " + str(
                    a) + ")\n" + "\nTada surandame lygties sprendinius:\nx₁,₂ = α ± βj\nx₁ = " + str(
                    alfa) + " + " + str(beta) + "j\nx₂ = " + str(alfa) + " + " + str(beta) + "j"
            # Pastaba!Žinau, kad galime naudoti cmath biblioteką ir būtų imanoma iš karto gauti kompleksinę šaknį, tačiau šiuo atveju laikiau, kad tai yra neleistina
            # Surašome sprendinius į tekstinę eilutę
            x1 = str(alfa) + " + " + str(beta) + simb
            x2 = str(alfa) + " - " + str(beta) + simb
    # Jeigu sprendiniai nėra tekstinėje eilutėje juos suapvaliname
    if x1 != str(x1) and x2 != str(x2):
        x1 = (round(x1, 8))
        x2 = (round(x2, 8))
    # Nustatome atsakymus
    variable3.set(x1)
    variable4.set(x2)
    af.config(text=eilute)


# ___________________________________________________________________________________________________
# Programa, kuri iš kvadratinių lygčių sprendinių sudaro kvadratinę lygtį
def reversed1():
    x1 = variable3.get()
    x2 = variable4.get()
    # Tikrinama, ar įvesti teisingi simboliai
    try:
        float(x1)
        float(x2)
    except:
        if x1 == "" or x2 == "" or x1 != "-" and x2 != "-" and x1[-1] != "j" and x1[-1] != "i" and x2[-1] != "i" and x2[
            -1] != "j" or re.search('[a-zA-Z]+', x1[:-1]) is not None or re.search('[a-zA-Z]+', x2[:-1]) != None:
            variable3.set("0.0")
            variable4.set("0.0")
            variable.set("0")
            variable1.set("0")
            variable2.set("0")
            eilute = "Negalima naudoti nereikalingų simbolių"
            af.config(text=eilute)
            return
    # Jeigu įvestos kompleksinės šaknys, žiūrime ar įmanoma padaryti kvadratinę lygtį
    if x1[-1] == "j" and x2[-1] == "j" or x1[-1] == "i" and x2[-1] == "i":
        simb = x1[-1]
        x1 = eval(x1[:-1])
        x2 = eval(x2[:-1])
        if float(x1) == -float(x2):
            c = -(float(x2) * (float(x1)))
            b = 0
            a = 1
            eilute = "Norint iš lygčių atsakymų sudaryti\nlygtį naudojamės šia formule:\n(x - x1)(x + x2) = 0\n\n(x - " + str(
                x1) + simb + ")(x + " + str(x2) + simb + ") = 0\nx² - " + str(x2) + "x" + simb + " - " + str(
                x1) + "x" + simb + " + " + str(c) + " = 0\n\nx² + " + str(b) + "x + " + str(c) + " = 0"
        else:
            b = 0
            c = 0
            a = 0
            eilute = "Kvadratinė lygtis su tokiais\nkompleksiniais skaiciais\nman yra per sudėtinga"
    # Tikrinama ar gerai suvestos kompleksinės šaknys
    elif x1[-1] == "j" or x1[-1] == "i" and x1[-1] != x2[-1] or x2[-1] == "i" or x2[-1] == "j" and x1[-1] != x2[-1]:
        b = 0
        c = 0
        a = 0
        eilute = "Blogai surašyti\nkvadratinės lygties sprendiniai"
    # Jei tai nėra kompleksinės šaknys sprendžiama kitaip
    else:
        x1 = float(x1)
        x2 = float(x2)
        # Nustatoma ar skaičius sveikas
        if x1 % 1 == 0:
            x1 = int(x1)
        if x2 % 1 == 0:
            x2 = int(x2)
        x1 = -x1
        x2 = -x2
        b = x2 + x1
        c = x2 * x1
        a = 1
        eilute = "Norint iš lygčių atsakymų sudaryti\nlygtį naudojamės šia formule:\n(x + (-x1))(x + (-x2)) = 0\n\n(x + " + str(
            x1) + ")(x + " + str(x2) + ") = 0\nx² + " + str(x2) + "x + " + str(x1) + "x + " + str(
            c) + " = 0\n\nx² + " + str(b) + "x + " + str(c) + " = 0"
    # Nustatomi skaičiai
    variable.set(str(a))
    variable1.set(str(b))
    variable2.set(str(c))
    af.config(text=eilute)


# ___________________________________________________________________________________________________
# Viskas apie mane
def apiemane():
    global phito
    naujas = Toplevel(pg, relief=RAISED, bd=5)
    naujas.geometry("%dx%d%+d%+d" % (800, 300, ilgis / 4, plotis / 4))
    naujas.resizable(False, False)
    naujas.overrideredirect(True)
    naujas.config(bg="linen")
    info11 = PhotoImage(file="output_RuZCcv.gif")
    du = Button(naujas, font=("Arial", "17", "bold"), image=info11, command=naujas.destroy)
    du.pack(side=RIGHT, padx=5)
    du.image = info11
    a1 = Frame(naujas, bd=5, relief=RIDGE, bg="#F6F6F6")
    a1.pack(side=LEFT, fill=X, expand=True, padx=10)
    phito = PhotoImage(file="output_qDSvmK.gif")
    Label(a1, bg="#F6F6F6", text="About creator", font=("Times", "25", "bold underline")).pack()
    Label(a1, image=phito, bd=5, highlightthickness=0, relief=RIDGE).pack(side=LEFT, padx=7, pady=7)
    Label(a1, bg="#F6F6F6", font=("Times", "11", "bold"), justify=LEFT,
          text="First Name - Kristupas\nLast Name - Jakubonis\nDate of Birth - 2002/04/02\nCity - Pasvalys\nEducation place - Pasvalys gymnasium named after Petras Vileisis\nPhone - +370 65608566\nEmail - kr.jakubonis@gmail.com\nHobbies - swimming, playing computer games, learning advanced Math,\n watching movies/TV series, programming, listening to music").pack(
        side=LEFT)


# ___________________________________________________________________________________________________
# ___________________________________________________________________________________________________
# ___________________________________________________________________________________________________
# Pagrindinė programa
# Nustatomas langas
pg = Tk()
ilgis = pg.winfo_screenwidth()
plotis = pg.winfo_screenheight()
pg.geometry("%dx%d" % (ilgis, plotis))
pg.config(background="#F6F6F6")
pg.resizable(False, False)
pg.attributes("-fullscreen", True)
pg.config(bg='cornsilk')
# ___________________________________________________________________________________________________
# Pasirenkamieji mygtukai
info1 = PhotoImage(file="output_RuZCcv.gif")
info2 = PhotoImage(file="output_5r88Ta.gif")
d2 = Button(pg, image=info2, command=apiemane)
d2.place(x=ilgis - 90, y=0)
d2.image = info2
d = Button(pg, image=info1, command=isejimas)
d.place(x=ilgis - 45, y=0)
d.image = info1
# ___________________________________________________________________________________________________
# Antraštė
da = Frame(pg, bd=5, relief=RIDGE, bg="#F6F6F6")
da.pack(pady=ilgis / 30)
Label(da, text="Kvadratinių lygčių sprendimas", bg="#F6F6F6", font=("Times", "25", "bold underline")).pack(padx=5,
                                                                                                           pady=5)
# ___________________________________________________________________________________________________
# Nustatomi kintamieji, bei pradinės jų reikšmės
variable = StringVar()
variable1 = StringVar()
variable2 = StringVar()
variable3 = StringVar()
variable4 = StringVar()
variable.set("0")
variable1.set("0")
variable2.set("0")
variable3.set("0.0")
variable4.set("0.0")
# ___________________________________________________________________________________________________
# Pradinis rėmas
c = Frame(pg, bd=5, relief=RIDGE, bg="#F6F6F6")
c.pack(pady=ilgis / 150, anchor="n", padx=plotis / 50)
# ___________________________________________________________________________________________________
# C įvestis
e = Entry(c, textvariable=variable, relief=SUNKEN, bd=5, font="Arial 40 bold", width=7, justify=RIGHT)
e.grid(row=0, column=1, padx=10, pady=10)
Label(c, text="x² +", font="Arial 40", bg="#F6F6F6").grid(row=0, column=2, pady=10)
# B įvestis
e1 = Entry(c, textvariable=variable1, relief=SUNKEN, bd=5, font="Arial 40 bold", width=7, justify=RIGHT)
e1.grid(row=0, column=3, pady=10)
Label(c, text="x +", font="Arial 40", bg="#F6F6F6").grid(row=0, column=4, pady=10)
# C įvestis
e3 = Entry(c, textvariable=variable2, relief=SUNKEN, bd=5, font="Arial 40 bold", width=7, justify=CENTER)
e3.grid(row=0, column=5, pady=10)
Label(c, text="= 0", font="Arial 40", bg="#F6F6F6").grid(row=0, column=6, pady=10)
# ___________________________________________________________________________________________________
# Paveiksliukas - rodyklė
photo = PhotoImage(file="output_0EXJ9A.gif")
photo.subsample(4)
nuotrauka = Label(c, bg="#F6F6F6", image=photo, bd=0, highlightthickness=0)
nuotrauka.grid(row=1, column=0, padx=15, pady=15, columnspan=7)
# ___________________________________________________________________________________________________
# Sprendiniai x1,x2
Label(c, text="x₁ =", bg="#F6F6F6", font="Arial 40").grid(row=2, column=3, pady=15)
Label(c, text="x₂ =", bg="#F6F6F6", font="Arial 40").grid(row=3, column=3, pady=15)
e4 = Entry(c, relief=SUNKEN, bd=5, font="Arial 18 bold", width=27, textvariable=variable3, justify=LEFT)
e4.grid(row=2, column=4, padx=5, pady=10, columnspan=3)
e5 = Entry(c, relief=SUNKEN, bd=5, font="Arial 18 bold", width=27, justify=LEFT, textvariable=variable4)
e5.grid(row=3, column=4, padx=5, pady=10, columnspan=3)
# ___________________________________________________________________________________________________
# Rėmas paaiškinimo blokui
lo = Frame(c, bd=5, relief=RIDGE, bg="#F6F6F6")
lo.grid(row=1, column=0, rowspan=3, padx=10, pady=10, columnspan=3, sticky="s")
# ___________________________________________________________________________________________________
# Paaiškinimo blokas
af = Label(lo, height=17, width=39, text="Gauto atsakymo paaiškinimas", bg="white", font="Arial 12", justify=LEFT)
af.pack()
# ___________________________________________________________________________________________________
# Nustatoma, kad kai atleidi klavišą kreipiamasi į komandą
e.bind("<KeyRelease>", sprendimas)
e1.bind("<KeyRelease>", sprendimas)
e3.bind("<KeyRelease>", sprendimas)
e4.bind("<KeyRelease>", reversed1)
e5.bind("<KeyRelease>", reversed1)
mainloop()


# ___________________________________________________________________________________________________
class DevNull:
    def write(self, msg):
        pass


sys.stderr = DevNull()
# Patikrink rezoliucija
