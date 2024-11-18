def nal1():
    x = input("Vnesi eure: ")

    #print("{}EUR je {}USD".format(x, int(x) * 1.11))
    return "{}EUR je {}USD".format(x, int(x) * 1.11)

def nal2():
    kolicinaDenarja = int(input("Koliko denarja imaš: "))
    cenaIzdelka = int(input("Koliko stane izdelek: "))

    #print(f"Imam {kolicinaDenarja} evrov, zato lahko kupim {kolicinaDenarja // cenaIzdelka} po ceni {cenaIzdelka}.") # Imam 1000 evrov, zato lahko kupim 4 izdelke po ceni 350 evrov.
    return f"Imam {kolicinaDenarja} evrov, zato lahko kupim {kolicinaDenarja // cenaIzdelka} po ceni {cenaIzdelka}."

def nal3():
    x = [4, 7, 1, 3]
    y = 0
    list = []
    for i in x:
        y += i
        list.append(i)

    #print("je {}".format(y))
    return "{} je {}".format([i for i in list], y)

def nal4():
    sec = 7354
    m = sec // 60
    h = m // 60
    s = sec - m * 60

    #print(f"{sec} sekund je enako {h} ur, {m//60} minut in {s} sekund.")
    return f"{sec} sekund je enako {h} ur, {m//60} minut in {s} sekund."


def nal5():
    x = int(input("R: "))  # x = 5

    #print(f"obseg kroga s polmerom {x} cm je {round(2 * 3.14 * x, 2)}cm, ploščina pa {3.14 * x ** 2}cm")
    return f"obseg kroga s polmerom {x} cm je {round(2 * 3.14 * x, 2)}cm, ploščina pa {3.14 * x ** 2}cm"

def nal6():
    stevilke = [10, 15, 23, 42, 55]
    deljitelj = 5
    deljiva_st = []

    [deljiva_st.append(i) for i in stevilke if i % deljitelj == 0]
    """
    osnovni for loop če gdo ne razume zgornje vrstice sam vrjetn tega sploh ne boste opazil :D
    
    for i in stevilke:
        if i % deljitelj == 0:
            deljiva_st.append(i)
    """

    #print(deljiva_st)
    return deljiva_st


def nal7():
    """
    import datetime

    # Pridobitev trenutnega datuma in ure
    trenutni_cas = datetime.now()

    # Formatiranje z uporabo f-string
    print(f"Trenutni datum in ura: {trenutni_cas.strftime('%d.%m.%Y %H.%M')}")
    """


    import time

    trenutni_cas = time.localtime()

    #print(f"Trenutni datum in ura: {trenutni_cas.tm_mday:02}.{trenutni_cas.tm_mon:02}.{trenutni_cas.tm_year} {trenutni_cas.tm_hour:02}.{trenutni_cas.tm_min:02}")
    return f"Trenutni datum in ura: {trenutni_cas.tm_mday:02}.{trenutni_cas.tm_mon:02}.{trenutni_cas.tm_year} {trenutni_cas.tm_hour:02}.{trenutni_cas.tm_min:02}"

def nal8():
    import math
    a = 3
    b = 4
    hipotenuza = math.sqrt(a ** 2 + b ** 2)

    #print("V pravokotnem trikotniku s katetama {} in {} cm meri hipotenuza {:.2f} cm.".format(a, b, hipotenuza))
    return "V pravokotnem trikotniku s katetama {} in {} cm meri hipotenuza {:.2f} cm.".format(a, b, hipotenuza)


def nal9():
    import math
    a = 2
    b = 4
    c = 2

    D = b ** 2 - 4 * a * c
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    #print("Za enačbo %dx^2 + %dx + %d = 0, sta korena:\nx1 = %.1f\nx2 = %.1f" % (a, b, c, x1, x2))
    return "Za enačbo %dx^2 + %dx + %d = 0, sta korena:\nx1 = %.1f\nx2 = %.1f" % (a, b, c, x1, x2)


def nal10():
    z1 = complex(2, 3)
    z2 = complex(1, -1)

    vsota = z1 + z2
    razlika = z1 - z2
    produkt = z1 * z2

    print("Za kompleksni števili {} in {}:\nVsota: {}\nRazlika: {}\nProdukt: {}".format(z1, z2, vsota, razlika, produkt))
    """
        print("Vsota: %s" % vsota)
        print("Razlika: %s" % razlika)
        print("Produkt: %s" % produkt)
    """

    return "Za kompleksni števili {} in {}:\nVsota: {}\nRazlika: {}\nProdukt: {}".format(z1, z2, vsota, razlika, produkt)



def nal11():
    a = 2
    k = 3
    n = 5

    vsota = a * (1 - k ** n) / (1 - k)

    #print(f"Vsota prvih {n} členov geometrijskega zaporedja z začetnim členom {a} in količnikom {k} je {vsota}.")
    return f"Vsota prvih {n} členov geometrijskega zaporedja z začetnim členom {a} in količnikom {k} je {vsota}."

def nal12():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C = [[A[0][0] + B[0][0], A[0][1] + B[0][1]],
         [A[1][0] + B[1][0], A[1][1] + B[1][1]]]

    #print(f"Matrika A: \n{A[0]}\n{A[1]}\nMatrika B: \n{B[0]}\n{B[1]}\nVsota matrik A in B:\n{C[0]}\n{C[1]}")
    """
    print(f"Matrika B: \n{B[0]}\n{B[1]}")
    print(f"Vsota matrik A in B:\n{C[0]}\n{C[1]}")
    """
    return f"Matrika A: \n{A[0]}\n{A[1]}\n\nMatrika B: \n{B[0]}\n{B[1]}\nVsota matrik A in B:\n{C[0]}\n{C[1]}"




#izpis rešitve funkcij v datoteko
with open("resitve.txt", "w") as f:
    f.write(nal1() + "\n\n")
    f.write(nal2() + "\n\n")
    f.write(nal3() + "\n\n")
    f.write(nal4() + "\n\n")
    f.write(nal5() + "\n\n")
    f.write(str(nal6()) + "\n\n")
    f.write(nal7() + "\n\n")
    f.write(nal8() + "\n\n")
    f.write(nal9() + "\n\n")
    f.write(nal10() + "\n\n")
    f.write(nal11() + "\n\n")
    f.write(nal12() + "\n\n")





