# functions.py

import os

class Emne:
    def __init__(self, kode, semester, studiepoeng, navn):
        self._kode = kode.upper()
        self.semester = semester.upper()  # 'H' = høst, 'V' = vår
        self.studiepoeng = int(studiepoeng)
        self.navn = navn

    # Frivillig: gjør emnekode skrivebeskyttet
    @property
    def kode(self):
        return self._kode

    def __str__(self):
        semnavn = "Høst" if self.semester == "H" else "Vår"
        return f"{self.kode}: {self.navn} ({self.studiepoeng} sp, {semnavn})"


# Lister over objekter
emner = []
studieplaner = []

class Studieplan:
    def __init__(self, plan_id, tittel):
        self.plan_id = plan_id
        self.tittel = tittel
        self.hostemner = []
        self.varemner = []

    def legg_til_emne(self, emne):
        if emne.semester == "H":
            if emne not in self.hostemner:
                self.hostemner.append(emne)
                print(f"{emne.kode} lagt til i høstsemesteret.")
            else:
                print("Emnet finnes allerede i høstsemesteret.")
        elif emne.semester == "V":
            if emne not in self.varemner:
                self.varemner.append(emne)
                print(f"{emne.kode} lagt til i vårsemesteret.")
            else:
                print("Emnet finnes allerede i vårsemesteret.")
        else:
            print("Ugyldig semesterkode.")

    def fjern_emne(self, emne):
        if emne in self.hostemner:
            self.hostemner.remove(emne)
            print(f"{emne.kode} fjernet fra høstsemesteret.")
        elif emne in self.varemner:
            self.varemner.remove(emne)
            print(f"{emne.kode} fjernet fra vårsemesteret.")
        else:
            print("Emnet finnes ikke i denne studieplanen.")

    def skriv_ut(self):
        print(f"\nStudieplan: {self.tittel} (ID: {self.plan_id})")
        print("Høstsemester:")
        if self.hostemner:
            for e in self.hostemner:
                print(" -", e)
        else:
            print("Ingen emner i høstsemesteret.")
        print("Vårsemester:")
        if self.varemner:
            for e in self.varemner:
                print(" -", e)
        else:
            print("Ingen emner i vårsemesteret.")

    def sjekk_plan(self):
        alle_emner = self.hostemner + self.varemner
        if not alle_emner:
            print("Studieplanen er tom.")
            return False
        for e in alle_emner:
            if e.semester not in ["H", "V"]:
                print(f"Ugyldig semester i {e.kode}")
                return False
            if e.studiepoeng <= 0:
                print(f"Ugyldige studiepoeng i {e.kode}")
                return False
            if not e.navn.strip():
                print(f"Ugyldig emnenavn i {e.kode}")
                return False
        print("Studieplanen er gyldig.")
        return True


def lag_nytt_emne(kode, semester, studiepoeng, navn):
    nytt_emne = Emne(kode, semester, studiepoeng, navn)
    emner.append(nytt_emne)
    print(f"Emnet {kode} ble opprettet.")

def ny_studieplan(plan_id, tittel):
    ny = Studieplan(plan_id, tittel)
    studieplaner.append(ny)
    print(f"Ny studieplan '{tittel}' ble opprettet.")

def skriv_ut_emner():
    if not emner:
        print("Ingen emner registrert.")
    else:
        print("\nRegistrerte emner:")
        for e in emner:
            print(" -", e)

def finn_emne_med_kode(kode):
    for e in emner:
        if e.kode == kode.upper():
            return e
    return None

def finn_studieplaner_som_bruker_emne(kode):
    funnet = False
    for sp in studieplaner:
        for e in sp.hostemner + sp.varemner:
            if e.kode == kode.upper():
                print(f"- {sp.tittel}")
                funnet = True
                break
    if not funnet:
        print("Ingen studieplaner bruker dette emnet.")


def lagre_til_fil(filnavn="data.txt"):
    with open(filnavn, "w", encoding="utf-8") as fil:
        # Lagre emner
        fil.write("[EMNER]\n")
        for e in emner:
            fil.write(f"{e.kode};{e.semester};{e.studiepoeng};{e.navn}\n")

        # Lagre studieplaner
        fil.write("[STUDIEPLANER]\n")
        for sp in studieplaner:
            host_koder = ",".join([e.kode for e in sp.hostemner])
            var_koder = ",".join([e.kode for e in sp.varemner])
            fil.write(f"{sp.plan_id};{sp.tittel};{host_koder};{var_koder}\n")

    print("Data (emner og studieplaner) ble lagret til fil.")


def les_fra_fil(filnavn="data.txt"):
    if not os.path.exists(filnavn):
        print("Filen finnes ikke. Lagre først før du leser.")
        return

    emner.clear()
    studieplaner.clear()

    with open(filnavn, "r", encoding="utf-8") as fil:
        seksjon = None
        for linje in fil:
            linje = linje.strip()
            if not linje:
                continue
            if linje == "[EMNER]":
                seksjon = "emner"
                continue
            elif linje == "[STUDIEPLANER]":
                seksjon = "studieplaner"
                continue

            if seksjon == "emner":
                kode, semester, studiepoeng, navn = linje.split(";")
                emner.append(Emne(kode, semester, studiepoeng, navn))
            elif seksjon == "studieplaner":
                plan_id, tittel, host_str, var_str = linje.split(";")
                sp = Studieplan(plan_id, tittel)
                if host_str:
                    for kode in host_str.split(","):
                        e = finn_emne_med_kode(kode)
                        if e:
                            sp.hostemner.append(e)
                if var_str:
                    for kode in var_str.split(","):
                        e = finn_emne_med_kode(kode)
                        if e:
                            sp.varemner.append(e)
                studieplaner.append(sp)
    print("Data (emner og studieplaner) ble lest fra fil.")


def avslutt_program():
    print("Programmet avsluttes...")
    quit()
