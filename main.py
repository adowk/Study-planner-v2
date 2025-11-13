# main.py
from functions import *

def vis_meny():
    print("\n=== STUDIEPLAN SYSTEM ===")
    print("1. Lag nytt emne")
    print("2. Legg til emne i studieplan")
    print("3. Fjern emne fra studieplan")
    print("4. Vis alle emner")
    print("5. Lag ny studieplan")
    print("6. Vis studieplaner")
    print("7. Sjekk studieplan")
    print("8. Finn hvilke studieplaner som bruker et emne")
    print("9. Lagre alt til fil")
    print("10. Les alt fra fil")
    print("11. Avslutt")
    return input("Velg handling (1–11): ")


def hovedmeny():
    while True:
        valg = vis_meny()

        if valg == "1":
            kode = input("Emnekode: ")
            semester = input("Semester (H/V): ").upper()
            studiepoeng = int(input("Antall studiepoeng: "))
            navn = input("Emnenavn: ")
            lag_nytt_emne(kode, semester, studiepoeng, navn)

        elif valg == "2":
            if not emner or not studieplaner:
                print("Du må ha registrert emner og minst én studieplan først.")
                continue
            for i, sp in enumerate(studieplaner, 1):
                print(f"{i}. {sp.tittel}")
            valg_plan = int(input("Velg studieplan: ")) - 1
            sp = studieplaner[valg_plan]
            skriv_ut_emner()
            kode = input("Skriv inn emnekode for å legge til: ")
            e = finn_emne_med_kode(kode)
            if e:
                sp.legg_til_emne(e)
            else:
                print("Fant ikke emne.")

        elif valg == "3":
            if not studieplaner:
                print("Ingen studieplaner tilgjengelig.")
                continue
            for i, sp in enumerate(studieplaner, 1):
                print(f"{i}. {sp.tittel}")
            valg_plan = int(input("Velg studieplan: ")) - 1
            sp = studieplaner[valg_plan]
            sp.skriv_ut()
            kode = input("Emnekode som skal fjernes: ")
            e = finn_emne_med_kode(kode)
            if e:
                sp.fjern_emne(e)
            else:
                print("Fant ikke emne.")

        elif valg == "4":
            skriv_ut_emner()

        elif valg == "5":
            plan_id = input("Studieplan-ID: ")
            tittel = input("Tittel: ")
            ny_studieplan(plan_id, tittel)

        elif valg == "6":
            if not studieplaner:
                print("Ingen studieplaner.")
            else:
                for sp in studieplaner:
                    sp.skriv_ut()

        elif valg == "7":
            if not studieplaner:
                print("Ingen studieplaner.")
                continue
            for i, sp in enumerate(studieplaner, 1):
                print(f"{i}. {sp.tittel}")
            valg_plan = int(input("Velg studieplan: ")) - 1
            studieplaner[valg_plan].sjekk_plan()

        elif valg == "8":
            kode = input("Skriv inn emnekode: ")
            finn_studieplaner_som_bruker_emne(kode)

        elif valg == "9":
            lagre_til_fil()

        elif valg == "10":
            les_fra_fil()

        elif valg == "11":
            avslutt_program()

        else:
            print("Ugyldig valg.")


if __name__ == "__main__":
    hovedmeny()
