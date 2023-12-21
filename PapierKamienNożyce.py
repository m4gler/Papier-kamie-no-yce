import random

def papier_kamien_nozyce():
    print("Witaj w papier kamień nożyce")

while True:
    wybor_gracza = input("Wybierz: 1 - Papier, 2 - Kamień, 3 - Nożyce, 4 - Koniec gry: ")

    if wybor_gracza == '4':
        print("Dziękujemy za grę")
        break

    if wybor_gracza not in ['1', '2', '3']:
        print("Nie ma takiej opcji!")
        continue

    wybor_komputera = str(random.randint(1, 3))

    print(f"Wybór gracza: {wybor_gracza}")
    print(f"Wybór komputera {wybor_komputera}")

    if wybor_gracza == wybor_komputera:
        print("Remis")

    elif (wybor_gracza == '1' and wybor_komputera == '2') or \
         (wybor_gracza == '2' and wybor_komputera == '3') or \
         (wybor_gracza == '3' and wybor_komputera == '1'):
        print("wygrałeś")

    else:
        print("przgrałeś")














