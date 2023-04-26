"""Rozbuduj program do zarządzania firmą. Wszystkie funkcjonalności
(komendy, zapisywanie i czytanie przy użyciu pliku itp.) pozostają bez zmian.

Stwórz clasę Manager, która będzie implementowała dwie kluczowe metody - execute i assign.
 Przy ich użyciu wywołuj poszczególne fragmenty aplikacji.
 Metody execute i assign powinny zostać zaimplementowane zgodnie z
  przykładami z materiałów do zajęć.

Niedozwolone są żadne zmienne globalne,
wszystkie dane powinny być przechowywane wewnątrz obiektu Manager."""
"""
Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.

Program po uruchomieniu wyświetla informację o dostępnych komendach:

saldo
sprzedaż
zakup
konto
lista
magazyn
przegląd
koniec

Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla
każdej z nich:

saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi
znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu
(np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu
"rower" oraz dodanie do konta kwoty 100).
zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk.
Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do
 komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
konto - Program wyświetla stan konta.
lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego
nazwę.
przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla
wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”.
eżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od
początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o
 tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi
 wybrać odpowiedni zakres).
koniec - Aplikacja kończy działanie.

Dodatkowe wymagania:

Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc
użyć komendy "przeglad".
Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację
o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji
(np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę,
 aplikacja powinna wyświetlić informację o niemożności wykonania operacji i
 jej nie wykonać). Zadbaj też o prawidłowe typy danych.

 ----------------------------------------------------------
 Zadanie 7
 Na podstawie zadania z lekcji 5 (operacje na koncie, sprzedaż/zakup itp.) należy
 zaimplementować poniższą część:

Saldo konta oraz magazyn mają zostać zapisane do pliku tekstowego, a przy kolejnym
uruchomieniu programu ma zostać odczytany. Zapisać należy również historię operacji
(przegląd), która powinna być rozszerzana przy każdym kolejnym uruchomieniu programu.

"""

DOSTEPNE_KOMENDY = (
    'saldo',
    'sprzedaz',
    'zakup',
    'konto',
    'lista',
    'magazyn',
    'przeglad',
    'koniec',
)

magazyn = {}
historia = []

with open('saldo.txt') as plik1:
    konto = int(plik1.readline())

with open('magazyn.txt') as plik2:
    for linia in plik2:
        nazwa_produktu = linia.strip().split(";")[0]
        ilosc_sztuk = int(linia.strip().split(";")[1])
        cena = int(linia.strip().split(";")[2])
        magazyn[nazwa_produktu] = [ilosc_sztuk, cena]


while True:
    print(f'Komendy: {DOSTEPNE_KOMENDY}')
    komenda = input('Wprowadz Komende:').strip()
    print(f'Wprowadzona Komenda: {komenda}')
    if komenda not in DOSTEPNE_KOMENDY:
        print('Podano Zla Komende')

    if komenda == 'koniec':
        print('Koniec Programu, Milego Dnia')
        # zapis do pliku
        break
    elif komenda == 'saldo':
        print(f'wykonuje akcje {komenda.upper()}...')
        kwota = int(input('Podaj Kwote, o ktora zmieni sie stan konta:'))
        if konto + kwota < 0:
            print('Ta Operacja jest niemozliwa')
        else:
            konto += kwota
            print(f'Zmieniam stan konta o {kwota}')
            historia.append([komenda, kwota])
    elif komenda == 'sprzedaz':
        print(f'wykonuje akcje {komenda.upper()}...')
        nazwa_produktu = input('Podaj Nazwe Produktu: ')
        cena = float(input('Podaj Cene Jednego Produktu: '))
        ilosc_produktow = int(input('Podaj Ilosc Produktow: '))
        koszt = cena * ilosc_produktow
        magazyn[nazwa_produktu][0] -= ilosc_produktow
        if nazwa_produktu not in magazyn:
            print("nie ma takiego produktu")
        else:
            konto += koszt
            print(f'Sprzedaje {ilosc_produktow} sztuk {nazwa_produktu} za {koszt}')
            historia.append([komenda, nazwa_produktu, ilosc_produktow, koszt])
    elif komenda == 'zakup':
        print(f'wykonuje akcje {komenda.upper()}...')
        nazwa_produktu = input('Podaj Nazwe Produktu: ')
        cena = float(input('Podaj Cene Jednego Produktu: '))
        ilosc_produktow = int(input('Podaj Ilosc Produktow: '))
        koszt = cena * ilosc_produktow
        magazyn[nazwa_produktu][0] += ilosc_produktow
        if koszt > konto:
            print('Nie masz tylu srodkow na koncie')
        else:
            if nazwa_produktu not in magazyn:
                magazyn[nazwa_produktu] = 0
                magazyn[nazwa_produktu] += ilosc_produktow
                konto -= koszt
            print(f'zakupiono {ilosc_produktow} sztuk {nazwa_produktu} za {koszt}')
            historia.append([komenda, nazwa_produktu, ilosc_produktow, koszt])
    elif komenda == 'konto':
        print(f'wykonuje akcje {komenda.upper()}...')
        print(f'Aktualny Stan Konta to: {konto}')
    elif komenda == 'lista':
        print(f'wykonuje akcje {komenda.upper()}...')
        print(f'Aktualny Stan Magazynu to: {magazyn}')
    elif komenda == 'magazyn':
        print(">>>> ", magazyn)
        print(f'wykonuje akcje {komenda.upper()}...')
        produkt_w_magazynie = input('podaj nazwe produktu:')
        if produkt_w_magazynie not in magazyn:
            print('Brak towaru w magazynie')
            continue
        print(f'Wmagazynie znjaduje sie {produkt_w_magazynie.upper()}(ilosc/cena za sztuke)')
        print(magazyn[produkt_w_magazynie])
    elif komenda == 'przeglad':
        with open('historia.txt', 'r') as plik3:
            zawartosc = plik3.readlines()
            zawartosc.extend(historia)
        print(f'wykonuje akcje {komenda.upper()}...')
        print('Prosze Wybrac Zakres od 0 do 4')
        od = int(input("podaj zakres od: "))
        do = int(input("podaj zakres do: "))
        if od < 0:
            print('poza zakresem, prosze wprowadzic poprawny zakres')
            od = int(input("podaj zakres od: "))
        if do > 4:
            print('poza zakresem, prosze wprowadzic poprawny zakres')
            do = int(input("podaj zakres do: "))
        for idx, wpis in enumerate(zawartosc[od:do]):
            print(idx, wpis)
        print(zawartosc)
        with open('historia.txt', 'a') as plik3:
            for polecenie in historia:
                if polecenie[0] in ['zakup']:
                    polecenie_do_zapisu = \
                        f'{polecenie[0]} {polecenie[1]} {polecenie[2]} {polecenie[3]}\n'
                elif polecenie[0] in ['sprzedaz']:
                    polecenie_do_zapisu = \
                        f'{polecenie[0]} {polecenie[1]} {polecenie[2]} {polecenie[3]}\n'
                elif polecenie[0] in ['saldo']:
                    polecenie_do_zapisu =\
                        f'{polecenie[0]} {polecenie[1]}\n'
                else:
                    continue
                plik3.write(polecenie_do_zapisu)
import json

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name} ({self.position}) - ${self.salary}/month"

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        for employee in self.employees:
            print(employee)

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return None

    def write_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

class Manager:
    def __init__(self, company, file_manager):
        self.company = company
        self.file_manager = file_manager

    def execute(self, command):
        if command == "list":
            self.company.list_employees()
        elif command.startswith("add "):
            _, name, position, salary = command.split(" ")
            employee = Employee(name, position, int(salary))
            self.company.add_employee(employee)
            self.file_manager.write_data([employee.__dict__ for employee in self.company.employees])
        else:
            print("Invalid command")

    def assign(self, data):
        employees = [Employee(employee['name'], employee['position'], employee['salary']) for employee in data]
        self.company.employees = employees

if __name__ == "__main__":
    company = Company()
    file_manager = FileManager("data.json")
    manager = Manager(company, file_manager)

    data = file_manager.read_data()
    if data:
        manager.assign(data)

    while True:
        command = input("Enter command: ")
        if command == "exit":
            break
        manager.execute(command)
