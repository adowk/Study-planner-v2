# Oppgave 1
class Emne:
    def __init__(self, kode, semester, studiepoeng, navn):
        self.kode = kode.upper()
        self.semester = semester.upper()  # 'H' = høst, 'V' = vår
        self.studiepoeng = int(studiepoeng)
        self.navn = navn

    def __str__(self):
        semnavn = "Høst" if self.semester == "H" else "Vår"
        return f"{self.kode}: {self.navn} ({self.studiepoeng} studiepoeng, {semnavn})"

emner = []


def lag_nytt_emne(kode, semester, studiepoeng, navn):
    nytt_emne = Emne(kode, semester, studiepoeng, navn)
    emner.append(nytt_emne)


# Oppgave 2
studieplan = [] 

def legg_til_i_studieplan(emne):
    e = lag_nytt_emne(emne.kode, emne.semester, emne.studiepoeng, emne.navn)

    if e is None: 
        print("Emnet ble ikke funnet og ikke lagt til å studieplanen.")
        return False
    if ann(x.kode == emne.kode for x in studieplan):
        print("Emnet er allerede i studieplanen.")
        return False
    studieplan.append(e)
    print(f"Emnet {emne.kode} ble lagt til i studieplanen.")
    return True


# Oppgave 3
def fjern_fra_studieplan(emne):
    if emne in studieplan:
        studieplan.remove(emne)
        print(f"Emnet {emne.kode} ble fjernet fra studieplanen.")
        return True
    else:
        print(f"Emnet {emne.kode} finnes ikke i studieplanen.")
        return False

# Oppgave 4 
def skriv_ut_emner():
    if not emner:
        print("Ingen emner registrert ennå.")
    else:
        for e in emner:
            print(e)


# Oppgave 5
def ny_studieplan():
    global studieplan
    studieplan = []
    print("En ny studieplan er opprettet.")

# Oppgave 6
def skriv_ut_studieplan():
    if not studieplan:
        print("Studieplanen er tom.")
        return False

hostemner = [e for e in studieplan if e.semester == "H" or e.semester == "Høst"]
varemner = [e for e in studieplan if e.semester == "V" or e.semester == "Vår"]

if hostemner:
    for e in hostemner:
        print(" -", e)
    else:
        print("ingen emner i dette semesteret.")


if varemner:
    for e in varemner:
        print(" -", e)
    else: 
        print("ingen emner i dette semesteret.")

# Oppgave 7
def sjekk_studieplan():
    if not self.kode:
        print("Studieplanen er tom.")
        return False
    if self.semester not in ["H", "V"]:
        print("Ugyldig semesterkode funnet i studieplanen.")
        return False
    if self.studiepoeng <= 0:
        print("Ugyldig studiepoeng funnet i studieplanen.")
        return False
    if not self.navn.strip():
        print("Ugyldig emnenavn funnet i studieplanen.")
        return False
    return True

# Oppgave 9
def lagre_til_fil(filnavn="emner.txt"):
    with open(filnavn, "w", encoding="utf-8") as fil:
        for e in emner:
            fil.write(f"{e.kode};{e.semester};{e.studiepoeng};{e.navn}\n")
    print("Emnene ble lagret til fil.")


# Oppgave 10
def les_fra_fil(filnavn="emner.txt"):
    emner.clear()
    try:
        with open(filnavn, "r", encoding="utf-8") as fil:
            for linje in fil:
                kode, semester, studiepoeng, navn = linje.strip().split(";")
                emner.append(Emne(kode, semester, studiepoeng, navn))
        print("Emnene ble lest inn fra fil.")
    except FileNotFoundError:
        print("Filen finnes ikke. Lagre først før du leser.")


# Oppgave 11
def avslutt_program():
    print("Programmet avsluttes...")
    quit()
