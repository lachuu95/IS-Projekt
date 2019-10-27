# IS-Projekt
Integracja Systemów Projekt
- Laboratorium 1 - Pliki tekstowe, odczyt danych
    >Korzystając z przykładu podanego w skrypcie napisz program, który po uruchomieniu wczytuje dane z pliku tekstowego "katalog.txt" (plik umieszczony w materiałach dodatkowych) i wyświetla dane na konsoli z etykietami poszczególnych pól (widok pseudo-tabelaryczny).
    >
    >Dodaj plik "katalog.txt" do katalogu głównego projektu.
- Laboratorium 2 - Praca w trybie graficznym
    >Korzystając z przykładu podanego w skrypcie oraz programu z Laboratorium 1 napisz program okienkowy, który po uruchomieniu  wczytuje dane z pliku tekstowego "katalog.txt" (plik umieszczony w materiałach dodatkowych) i wyświetla wszystkie dane z etykietami poszczególnych pól w oknie.
    >
    >Program powinien posiadać:
    >- przycisk "Importuj z pliku" służący do wczytywania danych z pliku TXT - po naciśnięciu powinien wyświetlić wczytane dane w formie graficznej tabeli;
    >- możliwość edycji danych z poziomu komórki tabeli;
    >- przycisk "Eksportuj do pliku" służący do zapisu zmodyfikowanej zawartości pliku TXT.
- Laboratorium 3 - baza danych do celów integracyjnych
    >Korzystając z przykładu podanego w skrypcie oraz programu z Laboratorium 2 dodaj do programu funkcję obsługi bazy danych:
    >1. Zaprojektuj schemat bazy danych odpowiadający rekordom w pliku "katalog.txt".
    >2. Wypełnij stworzoną bazę danych rekordami z pliku "katalog.txt".
    >3. Dodaj do programu nową funkcję umożliwiającą wczytywanie danych o katalogu z bazy danych.
    >
    >Program powinien posiadać:
    >- przycisk "Importuj z bazy danych" służący do wczytywania danych z bazy danych - po naciśnięciu powinien wyświetlić wczytane dane w formie graficznej tabeli (tak jak na Laboratorium 2.);
## Spis treści
- [Laboratorium 1 użycie](#Laboratorium-1-użycie)
- [Laboratorium 2 użycie](#Laboratorium-2-użycie)
- [Laboratorium 3 użycie](#Laboratorium-3-użycie)
- [Technologie](#Technologie)
- [Przygotownaie środowiska](#Przygotownaie-środowiska)
- [Uruchomienie serwera mySQL](#Uruchomienie-serwera-mySQL)
## Laboratorium 1 użycie
- wersja wczytująca lina po lini:
    ```console
    $ ./src/scripts/Lab1.py
    ```
- wersja wczytująca do data frame:
    ```console
    $ ./src/scripts/Lab1v1.py
    ```
## Laboratorium 2 użycie
```console
$ ./src/scripts/Lab2.py
```
## Laboratorium 3 użycie
```console
$ ./src/scripts/Lab2.py
```
## Technologie
- [Python 3.6](https://docs.python.org/3.6/ "Dokumentacja Pythona")
## Przygotownaie środowiska
```console
$ python3 -m venv .env
```
```console
$ . .env/bin/activate
```
```console
$ pip install -U -r requirements.txt
```