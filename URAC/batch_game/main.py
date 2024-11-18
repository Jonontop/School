import random

stvar_01 = False
stvar_02 = False
klet2 = False

print("Dobrodošel v igri!")
print("Nahajaš se v Slovenski obveščevalno-varnostna agenciji!")
print("Iščejo te varnostniki ter agenti zbeži preden te ujamejo!")

def main(klet2):
    print("nahajaš se v skladišču!")
    print("Vnesi število od -1 do 3 da greš v izbrano nadstropje")
    vnos = input("vnos: ")

    if vnos == "-1":
        klet(stvar_01)
    elif vnos == "0":
        pritlicje()
    elif vnos == "1":
        prvonad(stvar_02)
    elif vnos == "2":
        drugonad(klet2)
    elif vnos == "3":
        tretjenad()
    elif vnos == "-2":
        if klet2:
            kletdrugo()
        print("Napaka poskusi ponovno!")
        main(klet2)
    else:
        print("Napaka poskusi ponovno!")
        main(klet2)


def klet(stvar_01):
    print("prišel si v klet!")
    print("pojdi LEVO, DESNO, NAPREJ, NAZAJ")
    vnos = input("vnos: ")

    if vnos == "DESNO":
        print("Ojoj zašel si v orožarno kjer je polno varnostnikov")
        print("STRELJAJ ali POBEGNI")
        vnos = input("Vnos: ")
        if vnos == "STRELJAJ":
            if stvar_01:
                print("PAW PAW PAW!")
                print("Umrl si!")
            else:
                print("Aretirali so te, saj nimaš orožja!")

        elif vnos == "POBEGNI":
            print("pobegnil si... za zdaj!")
            klet(stvar_01)

    elif vnos == "LEVO":
        print("Nahajaš se v garderobi!")
        if stvar_01:
            print("V kotu leži Sturmgewehr 44")
        print("POBERI ali ZAPUSTI")
        vnos = input("Vnos: ")
        if vnos == "POBERI":
            if stvar_01:
                print("Si že pobral!")
                klet(stvar_01)
            else:
                stvar_01 = True
                print("Pobral si orožje!")
                klet(stvar_01)

        elif vnos == "ZAPUSTI":
            print("Zapustil si garderobo!")
            klet(stvar_01)

    elif vnos == "NAPREJ":
        print("Nahajaš se v garaži!")
        print("Tu je veliko oboroženih vozil!")
        print("ZBEŽI ali NAZAJ")
        vnos = input("Vnos: ")
        if vnos == "ZBEŽI":
            print("Pobegnil si!!")
            print("WROOM WROOM!")
            print("OJOJ! ujeli so te!")

        elif vnos == "NAZAJ":
            main(klet2)

        else:
            print("Napaka")
            pritlicje()

    elif vnos == "NAZAJ":
        main(klet2)

    else:
        print("NAPAKA!")
        klet(stvar_01)


def pritlicje(): #dokončaj!!!!
    print("Nahaj še v pritliču SOVE!")
    print("Bodi previden tu je ogromno agentov!")
    print("Vnesi VEN, LEVO, DESNO, NAZAJ")
    vnos = input("Vnos: ")

    if vnos == "VEN":
        print("Rešil si se agentov!")
        print("Bodi previden da te ne ujamejo ko boš spal!")

    elif vnos == "LEVO":
        return
    elif vnos == "DESNO":
        return
    elif vnos == "NAZAJ":
        return
    else:
        print("Napaka")
        pritlicje()


def prvonad(stvar_02): #dokončaj!!!
    print("Nahajaš se v 1. nadstropju SOVE!")
    print("Poišči kartoteko Jona Pečarja Anželaka!")
    print("NAPREJ, NAZAJ, LEVO, DESNO")
    vnos = input("Vnos: ")
    if vnos == "NAPREJ":
        print("HUDIČA!")
        print("Zaklenjeno!")
        prvonad(stvar_02)
    elif vnos == "LEVO":
        print("prišel si v arhiv SOVE!")
        print("Jon-ova kartoteka je na omari!")
        print("POBERI ali ZAPUSTI")
        vnos = input("Vnos: ")
        if vnos == "POBERI":
            stvar_02 = True
            print("Pobral si Jon-ovo kartoteko!")
            prvonad(stvar_02)
        elif vnos == "ZAPUSTI":
            print("Zapustil si arhiv!")
            prvonad(stvar_02)

        else:
            print("Napaka!")
            prvonad(stvar_02)
    elif vnos == "DESNO":
        return

    elif vnos == "NAZAJ":
        main(klet2)

    else:
        print("Napaka!")
        prvonad(stvar_02)


def drugonad(klet2):
    print("Nahajaš se v 2. nadstropju!")
    print("Tu imajo veliko predavanj, tako da potiho!")
    print("NAPREJ, NAZAJ, LEVO, DESNO")
    vnos = input("Vnos: ")
    if vnos == "NAZAJ":
        main(klet2)
    elif vnos == "NAPREJ":
        print("Tu imajo pogovor!")
        print("Govorijo o skriti kleti!")
        print("Odklenil si 2. nadstropje kleti!")
        klet2 = True
        main(klet2)
    elif vnos == "LEVO":
        print("Pristal si v šefovi pisarni!")
        print("Tu ni več poti naprej!")
        print("ARETIRAN SI!")

    elif vnos == "DESNO":
        print("Nahajš se v sobi z božjim očesom!")
        print("Božje oko je program s katerim lahko slediš človeku!")
        print("Strogo zaupna programska oprema!")
        print("UPORABI ali ZAPUSTI")
        vnos = input("Vnos: ")
        if vnos == "UPORABI":
            print("Previden bodi")
            print("Vnesi ime svoje žrtve!")
            bozoko = input("Vnos: ")

            if random.randint(1,4) == 1:
                print("Iščem za "+bozoko)
                print("rezultat: ")
                print("Obtožbe: none")
                print("Zapor: none")

            elif random.randint(1, 4) == 2:
                print("Iščem za " + bozoko)
                print("rezultat: ")
                print("Obtožbe: Umor")
                print("Zapor: 25 let")

            elif random.randint(1,4) == 3:
                print("Iščem za " + bozoko)
                print("rezultat: ")
                print("Obtožbe: Atentat")
                print("Zapor: 5 let")

            elif random.randint(1,4) == 4:
                print("Iščem za " + bozoko)
                print("rezultat: ")
                print("Obtožbe: Ponarejanje Denarja")
                print("Zapor: 55 let")

            else:
                print("Iščem za " + bozoko)
                print("rezultat: ")
                print("Obtožbe: Ugrabitev")
                print("Zapor: 15 let")
        else:
            print("Napaka!")
            drugonad(klet2)
    else:
        print("Napaka!")
        drugonad(klet2)


def tretjenad():
    print("V gradnji!")

def kletdrugo():
    print("V gradnji! ")


main(klet2)
