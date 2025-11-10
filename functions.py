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


# Oppgave 4 
def skriv_ut_emner():
    if not emner:
        print("Ingen emner registrert ennå.")
    else:
        for e in emner:
            print(e)


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
