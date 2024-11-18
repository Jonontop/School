def nal1():
    x = 30

    if x <= 30:
        return "prepočasi"

    elif x <= 50:
        return "V mejah dovoljene hitrosti"

    elif x <= 90:
        return "povišana hitrost bodi previden"

    elif x <= 130:
        return "Visoka hitrost, lahko dobiš kazen!"

    elif x > 130:
        return "kaznovan boš!"


def nal2(x=1999):

    if x <= 1000:
        return x * 0.1
    elif x > 1000 and x < 2000:
        return x * .2
    elif x >= 2000:
        return x * .3

    return x * .1 if x <= 1000 else x * .2 if x < 2000 else x * .3


def nal3(x="geslo"):

    upper = False
    lower = False
    num = False
    special = False

    if len(x) >= 8:
        for i in x:
            if i.isupper():
                upper = True
            if i.islower():
                lower = True
            if i.isnumeric():
                num = True
            if i in ["!", "@", "#", "$", "%"]:
                special = True

        if upper and lower and num and special:
            return "Geslo je vredu"
        else:
            return "Geslo ni vredu"
    else:
        return "prekratko geslo"


def nal4():
    import random
    x = input("Vnesi: ")
    listx = ["Kamen", "Škarje", "Papir"]
    pc = random.choice(listx)

    if x in listx:
        if (x == "Papir" and pc == "Kamen") or (x == "Kamen" and pc == "Škarje") or (x == "Škarje" and pc == "Papir"):
            return "Zmagal si"
        else:
            return "Zgubil si"
    else:
        return "Napačen Vnos!"


def nal5():
    x = [input(), int(input()), int(input())]
    match x[0]:
        case "+":
            return x[1] + x[2]
        case "-":
            return x[1] - x[2]
        case "*":
            return x[1] * x[2]
        case "/":
            return x[1] / x[2]


def nal6():
    x = ['+', 3, ['*', 2, 5]]
    tmp = None
    for i in x:
        if str(type(i)) == "<class 'list'>":
            match i[0]:
                case "+":
                    tmp = i[1] + i[2]
                case "-":
                    tmp = i[1] - i[2]
                case "*":
                    tmp = i[1] * i[2]
                case "/":
                    tmp = i[1] / i[2]

    match x[0]:
        case "+":
            return x[1] + tmp
        case "-":
            return x[1] - tmp
        case "*":
            return x[1] * tmp
        case "/":
            return x[1] / tmp


def nal7():
    date = [input("Dan: "), input("Mesec: "), input("Leto: ")]

    if (date[1] == "2" and date[0] <= "28") or ((date[1] > "12") and date[0] <= "31"):
        return "Pravilen datum"


def nal8():
    magicen_kvadrat = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

    for i in magicen_kvadrat:
        if sum(i) != 15:
            return "Ni magicen kvadrat"
    return "Magicen kvadrat"


def nal9():
    stevke = ["ena", "dva", "tri", "štiri", "pet", "šest", "sedem", "osem", "devet"]
    posebne = ["enajst", "dvanajst", "trinajst", "štirinajst", "petnajst", "šestnajst", "sedemnajst", "osemnajst", "devetnajst"]
    desetice = ["deset", "dvajset", "trideset", "štirideset", "petdeset", "šestdeset", "sedemdeset", "osemdeset", "devetdeset"]
    x = input("Vnesi število: ")

    if int(x) < 10:
        return stevke[int(x) - 1]
    elif int(x) % 10 == 0:
        return desetice[int(x) // 10 - 1]
    elif 10 < int(x) < 20:
        return posebne[int(x) - 11]
    else:
        return stevke[int(x) % 10 - 1] + "in" + desetice[int(x) // 10 - 1]


def nal10():
    ura = input("Vnesi uro: ")
    minuta = input("Vnesi minute: ")  # 120 = 2h 0m

    return f"razlika med uro in minuto je {(int(ura) * 60) - int(minuta) if int(minuta) < int(ura) * 60 else 'Napačen vnos'} minut"


def nal11():
    vnos = input("Vnesi število: ")  # vnos
    vnos = vnos[::-1]  # Obrnite številko kartice
    tmp = 0
    arr = []

    # Pomnožite vsako drugo številko z 2. Če je rezultat večji od 9, odštejte 9.
    for i in range(len(vnos)):
        if i % 2 == 0:
            i = int(vnos[i]) * 2
            if i > 9:
                i = i - 9
        arr.append(i)

    # Seštejte vsa števila.
    for i in arr:
        tmp += i

    # Če je vsota deljiva s 10, je številka veljavna.
    return True if tmp % 10 == 0 else False


def pretvorba(rimsko):
    # Slovar z vrednostmi rimskih števil
    rimske_vrednosti = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # Spremenljivka za shranjevanje rezultata
    rezultat = 0
    dolzina = len(rimsko)

    for i in range(dolzina):
        if i + 1 < dolzina and rimske_vrednosti[rimsko[i]] < rimske_vrednosti[rimsko[i + 1]]:
            rezultat -= rimske_vrednosti[rimsko[i]]
        else:
            rezultat += rimske_vrednosti[rimsko[i]]

    return rezultat




with open("resitve.txt", "w") as f:
    f.write(nal1() + "\n\n")
    f.write(str(nal2()) + "\n\n")
    f.write(str(nal3("geslo")) + "\n\n")
    f.write(str(nal4()) + "\n\n")
    f.write(str(nal5()) + "\n\n")
    f.write(str(nal6()) + "\n\n")
    f.write(str(nal7()) + "\n\n")
    f.write(str(nal8()) + "\n\n")
    f.write(str(nal9()) + "\n\n")
    f.write(str(nal10()) + "\n\n")
    f.write(str(nal11()) + "\n\n")
    f.write(str(pretvorba('XII')) + "\n\n")
