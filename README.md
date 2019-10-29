# IS-Projekt
Integracja Systemów Projekt
## Spis treści
- [Laboratorium 1](#Laboratorium-1 "Przejdz do laboratorium 1")
- [Laboratorium 2](#Laboratorium-2 "Przejdz do laboratorium 2")
- [Laboratorium 3](#Laboratorium-3 "Przejdz do laboratorium 3")
- [Laboratorium 4](#Laboratorium-4 "Przejdz do laboratorium 4")
- [Technologie](#Technologie "Przejdz do wykorzystanych Technologii")
- [Przygotownaie środowiska](#Przygotownaie-środowiska "Przejdz do konfiguracji środowiska")
## Laboratorium 1
Pliki tekstowe, odczyt danych
>Korzystając z przykładu podanego w skrypcie napisz program, który po uruchomieniu wczytuje dane z pliku tekstowego "katalog.txt" (plik umieszczony w materiałach dodatkowych) i wyświetla dane na konsoli z etykietami poszczególnych pól (widok pseudo-tabelaryczny).
>
>Dodaj plik "katalog.txt" do katalogu głównego projektu.
### Uruchomienie programu
- wersja wczytująca lina po lini:
    ```console
    $ ./src/scripts/Lab1.py
    ```
- wersja wczytująca do data frame:
    ```console
    $ ./src/scripts/Lab1v1.py
    ```
## Laboratorium 2
Praca w trybie graficznym
>Korzystając z przykładu podanego w skrypcie oraz programu z Laboratorium 1 napisz program okienkowy, który po uruchomieniu  wczytuje dane z pliku tekstowego "katalog.txt" (plik umieszczony w materiałach dodatkowych) i wyświetla wszystkie dane z etykietami poszczególnych pól w oknie.
>
>Program powinien posiadać:
>- przycisk "Importuj z pliku" służący do wczytywania danych z pliku TXT - po naciśnięciu powinien wyświetlić wczytane dane w formie graficznej tabeli;
>- możliwość edycji danych z poziomu komórki tabeli;
>- przycisk "Eksportuj do pliku" służący do zapisu zmodyfikowanej zawartości pliku TXT.
### Uruchomienie programu
```console
$ ./src/scripts/Lab2.py
```
## Laboratorium 3
Baza danych do celów integracyjnych
>Korzystając z przykładu podanego w skrypcie oraz programu z Laboratorium 2 dodaj do programu funkcję obsługi bazy danych:
>1. Zaprojektuj schemat bazy danych odpowiadający rekordom w pliku "katalog.txt".
>2. Wypełnij stworzoną bazę danych rekordami z pliku "katalog.txt".
>3. Dodaj do programu nową funkcję umożliwiającą wczytywanie danych o katalogu z bazy danych.
>
>Program powinien posiadać:
>- przycisk "Importuj z bazy danych" służący do wczytywania danych z bazy danych - po naciśnięciu powinien wyświetlić wczytane dane w formie graficznej tabeli (tak jak na Laboratorium 2.);
### Uruchomienie programu
```console
$ ./src/scripts/Lab3.py
```
## Laboratorium 4
Import i eksport danych z bazy danych do plików tekstowych
>Korzystając z przykładu podanego w skrypcie oraz programu z Laboratorium 3 dodaj do programu nową funkcję umożliwiającą modyfikowanie danych wczytanych z tabeli oraz eksport danych do bazy danych. Zadbaj o wyświetlanie użytkownikowi informacji o różnicach między danymi, które widzi, a tymi które są zapisane w bazie danych.
>
>Program powinien posiadać:
>- możliwość edycji danych pobranych z bazy danych;
>- przycisk "Eksportuj do bazy danych", który po naciśnięciu zaktualizuje stan bazy danych;
>- Pamiętaj o uwzględnieniu poprawnego działania pozostałych przycisków z programu z Laboratorium 3. i 2. oraz możliwości wczytywania danych z jednego źródła i zapisu do innego np. wczytanie danych z pliku i zapis do bazy danych.
>
>W repozytorium umieść plik archiwum zawierający:
>- katalog "projekt4" z plikami projektu;
>- katalog "rozwiazanie4" z uruchamialnymi plikami rozwiązania;
>- szczegóły ustawienia środowiska testowego zapisane w pliku tekstowym.
### Uruchomienie programu
```console
$ ./src/scripts/Lab4.py
```
## Technologie
- [Python 3.6](https://docs.python.org/3.6/ "Dokumentacja Python'a")
- [PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/ "Dokumentacja PyQt5")
- [SQLite](https://www.sqlite.org/docs.html "Dokumentacja SQLite")
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
