# TODO: Lag en meny som bruker funksjonene fra functions.py
from functions import *

def vis_meny():
    """Viser hovedmenyen"""
    print("\n=== STUDIEPLAN MENY ===")
    print("1. Registrer nytt emne")
    print("2. Vis alle emner")
    print("3. Legg til emne i studieplan")
    print("4. Fjern emne fra studieplan")
    print("5. Vis studieplan")
    print("6. Opprett ny studieplan")
    print("7. Sjekk studieplan")
    print("8. Lagre emner til fil")
    print("9. Last inn emner fra fil")
    print("10. Avslutt")
    return input("Velg handling (1-10): ")

def hovedmeny():
    """Hovedmeny-løkke"""
    while True:
        valg = vis_meny()
        
        if valg == "1":
            kode = input("Skriv inn emnekode: ")
            semester = input("Skriv inn semester (H/V): ").upper()
            while semester not in ["H", "V"]:
                print("Ugyldig semester! Skriv H for høst eller V for vår.")
                semester = input("Skriv inn semester (H/V): ").upper()
            try:
                studiepoeng = int(input("Skriv inn antall studiepoeng: "))
                while studiepoeng <= 0:
                    print("Ugyldig antall studiepoeng!")
                    studiepoeng = int(input("Skriv inn antall studiepoeng: "))
            except ValueError:
                print("Ugyldig input! Vennligst skriv inn et helt tall.")
                continue
            navn = input("Skriv inn emnenavn: ")
            while not navn.strip():
                print("Emnenavn kan ikke være tomt!")
                navn = input("Skriv inn emnenavn: ")
            lag_nytt_emne(kode, semester, studiepoeng, navn)
            
        elif valg == "2":
            skriv_ut_emner()
            
        elif valg == "3":
            if not emner:
                print("Ingen emner å velge fra!")
                continue
            print("\nTilgjengelige emner:")
            for i, e in enumerate(emner, 1):
                print(f"{i}. {e}")
            try:
                emne_idx = int(input("Velg emne nummer: ")) - 1
                if 0 <= emne_idx < len(emner):
                    legg_til_i_studieplan(emner[emne_idx])
                else:
                    print("Ugyldig valg!")
            except ValueError:
                print("Ugyldig input!")
                
        elif valg == "4":
            if not studieplan:
                print("Studieplanen er tom!")
                continue
            print("\nEmner i studieplanen:")
            for i, e in enumerate(studieplan, 1):
                print(f"{i}. {e}")
            try:
                emne_idx = int(input("Velg emne nummer: ")) - 1
                if 0 <= emne_idx < len(studieplan):
                    fjern_fra_studieplan(studieplan[emne_idx])
                else:
                    print("Ugyldig valg!")
            except ValueError:
                print("Ugyldig input!")
                
        elif valg == "5":
            skriv_ut_studieplan()
            
        elif valg == "6":
            ny_studieplan()
            
        elif valg == "7":
            if not studieplan:
                print("Studieplanen er tom!")
                continue
            if sjekk_studieplan():
                print("Studieplanen er gyldig!")
            else:
                print("Studieplanen er ikke gyldig!")
                
        elif valg == "8":
            lagre_til_fil()
            
        elif valg == "9":
            les_fra_fil()
            
        elif valg == "10":
            avslutt_program()
            
        else:
            print("Ugyldig valg!")

if __name__ == "__main__":
    hovedmeny(
