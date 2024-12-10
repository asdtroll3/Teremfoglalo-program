
class Foglalas:
    def __init__(self, key, tanar_neve, tantargy, terem_szam, nap, kezd_ido, veg_ido):
        self.key = key
        self.tanar_neve = tanar_neve
        self.tantargy = tantargy
        self.terem_szam = terem_szam
        self.nap = nap
        self.kezd_ido = kezd_ido
        self.veg_ido = veg_ido


def utkozik(uj_foglalas, foglalasok):
    """Ellenőrzi, hogy van-e ütközés a foglalások között."""
    for foglalas in foglalasok:
        if foglalas.terem_szam == uj_foglalas.terem_szam and foglalas.nap == uj_foglalas.nap:
            if uj_foglalas.kezd_ido < foglalas.veg_ido and uj_foglalas.veg_ido > foglalas.kezd_ido:
                return True
    return False


def uj_foglalas(foglalasok):
    """Új teremfoglalás hozzáadása."""
    global keys
    print("Tanar neve: ", end="")
    tanar_neve = input()
    print("Tantárgy: ", end="")
    tantargy = input()
    print("Terem szám: ", end="")
    terem_szam = int(input())
    print("Nap (1-Hétfő, ..., 7-Vasárnap): ", end="")
    nap = int(input())
    print("Kezdési időpont (óra): ", end="")
    kezd_ido = int(input())
    print("Befejezési időpont (óra): ", end="")
    veg_ido = int(input())

    uj_foglalas = Foglalas(keys, tanar_neve, tantargy, terem_szam, nap, kezd_ido, veg_ido)

    if utkozik(uj_foglalas, foglalasok):
        print("Ütközés! A foglalás nem adható hozzá.")
    else:
        foglalasok.append(uj_foglalas)
        keys += 1
        print("Foglalás sikeresen hozzáadva.")


def listaz_foglalasok(foglalasok):
    """Listázza az összes foglalást."""
    if not foglalasok:
        print("Nincsenek foglalások.")
        return

    for foglalas in foglalasok:
        print(f"Foglalas száma: {foglalas.key}, Tanar neve: {foglalas.tanar_neve}, Tantárgy: {foglalas.tantargy}, "
              f"Terem szám: {foglalas.terem_szam}, Nap: {foglalas.nap}, "
              f"Kezdés: {foglalas.kezd_ido}, Befejezés: {foglalas.veg_ido}")


def torol_foglalas(foglalasok):
    """Foglalás törlése foglalás szám alapján."""
    print("Adja meg a törlendő foglalás számát: ", end="")
    key = int(input())

    for foglalas in foglalasok:
        if foglalas.key == key:
            foglalasok.remove(foglalas)
            print("Foglalás törölve.")
            return

    print("Nem található foglalás ezzel a számmal")

def szerkeszt_foglalas(foglalasok):
    try:
        editkey = int(input("Adja meg a szerkesztendo foglalas számát:\n"))

        # Find the booking by key
        foglalas = next((f for f in foglalasok if f.key == editkey), None)

        if foglalas:
            # Collect new data from user
            foglalas.tanar_neve = input("Uj tanar neve: ")
            foglalas.tantargy = input("Uj tantargy neve: ")
            foglalas.terem_szam = input("Uj terem szama: ")
            foglalas.nap = input("Uj nap szama: ")
            foglalas.kezd_ido = int(input("Uj kezdesi ido (0-23): "))
            foglalas.veg_ido = int(input("Uj befejezesi ido (0-23): "))

            if foglalas.kezd_ido >= foglalas.veg_ido:
                print("Hiba: A kezdesi idopont nem lehet nagyobb vagy egyenlo a befejezesi idopontnal.")
                return

            if utkozik(foglalas, foglalasok):
                print("Hiba: Az uj adatok utkoznek egy masik foglalassal.")
            else:
                print("Foglalas sikeresen szerkesztve.")
        else:
            print("Nincs ilyen foglalas.")

    except ValueError:
        print("Hiba: Nem ervenyes kulcsot adott meg.")

def szures_foglalasok(foglalasok):
    try:
        print("Szuro opcio:")
        print("1. Tanar szerint")
        print("2. Tantargy szerint")
        print("3. Terem szerint")
        print("4. Nap szerint")
        print("5. Kezdesi ido szerint")
        print("6. Befejezesi ido szerint")
        szuro_opcio = int(input("Valasztas: "))

        if szuro_opcio == 1:
            tanar = input("Adja meg a tanar nevet: ")
            for foglalas in foglalasok:
                if foglalas.tanar_neve == tanar:
                    print(f"Foglalas száma: {foglalas.key}, Tanar: {foglalas.tanar_neve}, Tantargy: {foglalas.tantargy}, "
                          f"Terem: {foglalas.terem_szam}, Nap: {foglalas.nap}, Kezdes: {foglalas.kezd_ido}, "
                          f"Befejezes: {foglalas.veg_ido}")
        elif szuro_opcio == 2:
            tantargy = input("Adja meg a tantargy nevet: ")
            for foglalas in foglalasok:
                if foglalas.tantargy == tantargy:
                    print(f"Foglalas száma: {foglalas.key}, Tanar: {foglalas.tanar_neve}, Tantargy: {foglalas.tantargy}, "
                          f"Terem: {foglalas.terem_szam}, Nap: {foglalas.nap}, Kezdes: {foglalas.kezd_ido}, "
                          f"Befejezes: {foglalas.veg_ido}")
        elif szuro_opcio == 3:
            terem = int(input("Adja meg a terem szamat: "))
            for foglalas in foglalasok:
                if foglalas.terem_szam == terem:
                    print(f"Foglalas száma: {foglalas.key}, Tanar: {foglalas.tanar_neve}, Tantargy: {foglalas.tantargy}, "
                          f"Terem: {foglalas.terem_szam}, Nap: {foglalas.nap}, Kezdes: {foglalas.kezd_ido}, "
                          f"Befejezes: {foglalas.veg_ido}")
        elif szuro_opcio == 4:
            nap = int(input("Adja meg a napot (1-Hetfo, ..., 7-Vasarnap): "))
            for foglalas in foglalasok:
                if foglalas.nap == nap:
                    print(f"Foglalas száma: {foglalas.key}, Tanar: {foglalas.tanar_neve}, Tantargy: {foglalas.tantargy}, "
                          f"Terem: {foglalas.terem_szam}, Nap: {foglalas.nap}, Kezdes: {foglalas.kezd_ido}, "
                          f"Befejezes: {foglalas.veg_ido}")
        elif szuro_opcio == 5:
            kezd_ido = int(input("Adja meg a kezdesi idot: "))
            for foglalas in foglalasok:
                if foglalas.kezd_ido == kezd_ido:
                    print(f"Foglalas száma: {foglalas.key}, Tanar: {foglalas.tanar_neve}, Tantargy: {foglalas.tantargy}, "
                          f"Terem: {foglalas.terem_szam}, Nap: {foglalas.nap}, Kezdes: {foglalas.kezd_ido}, "
                          f"Befejezes: {foglalas.veg_ido}")
        elif szuro_opcio == 6:
            veg_ido = int(input("Adja meg a vegzesi idot: "))
            for foglalas in foglalasok:
                if foglalas.veg_ido == veg_ido:
                    print(f"Foglalas száma: {foglalas.key}, Tanar: {foglalas.tanar_neve}, Tantargy: {foglalas.tantargy}, "
                          f"Terem: {foglalas.terem_szam}, Nap: {foglalas.nap}, Kezdes: {foglalas.kezd_ido}, "
                          f"Befejezes: {foglalas.veg_ido}")
        else:
            print("Hibas valasztas.")
    except ValueError:
        print("Hiba: Nem ervenyes bemenet.")

def naptari_nezet(foglalasok):
    napok = ["Hetfo", "Kedd", "Szerda", "Csutortok", "Pentek", "Szombat", "Vasarnap"]

    print("\n*** Heti naptari nezet ***\n")

    for nap in range(1, 8):
        print(f"\n{napok[nap - 1]}:\n")

        for ora in range(24):
            foglalt = False
            for foglalas in foglalasok:
                if foglalas.nap == nap and foglalas.kezd_ido <= ora < foglalas.veg_ido:
                    print(f"{ora}:00 - {ora + 1}:00: {foglalas.tantargy} "
                          f"({foglalas.tanar_neve}, Terem: {foglalas.terem_szam})")
                    foglalt = True
                    break
            if not foglalt:
                print(f"{ora}:00 - {ora + 1}:00: SZABAD")
def menu():
    """Főmenü."""
    foglalasok = []
    global keys
    keys = 0

    while True:
        print("\n1. Új foglalás hozzáadása")
        print("2. Foglalások listázása")
        print("3. Foglalás törlése")
        print("4. Foglalás szerkesztése")
        print("5. Foglalások szűrése")
        print("6. Naptári nézet")
        print("7. Kilépés")
        print("Választás: ", end="")

        valasztas = int(input())

        if valasztas == 1:
            uj_foglalas(foglalasok)
        elif valasztas == 2:
            listaz_foglalasok(foglalasok)
        elif valasztas == 3:
            torol_foglalas(foglalasok)
        elif valasztas == 4:
            szerkeszt_foglalas(foglalasok)
        elif valasztas == 5:
            szures_foglalasok(foglalasok)
        elif valasztas == 6:
            naptari_nezet(foglalasok)
        elif valasztas == 7:
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")


# Futtatja a programot megnyitasnal
if __name__ == "__main__":
    menu()
