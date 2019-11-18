# IS-Projekt
Integracja Systemów Projekt
## Spis treści
- [Laboratorium 1](#Laboratorium-1 "Przejdź do laboratorium 1")
- [Laboratorium 2](#Laboratorium-2 "Przejdź do laboratorium 2")
- [Laboratorium 3](#Laboratorium-3 "Przejdź do laboratorium 3")
- [Laboratorium 4](#Laboratorium-4 "Przejdź do laboratorium 4")
- [Laboratorium 5 i 6](#Laboratorium-5-i-6 "Przejdź do laboratorium 5 i 6")
- [Laboratorium 7 i 8](#Laboratorium-7-i-8 "Przejdź do laboratorium 7 i 8")
- [Technologie](#Technologie "Przejdź do wykorzystanych Technologii")
- [Przygotownaie środowiska](#Przygotownaie-środowiska "Przejdź do konfiguracji środowiska")
---
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
---
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
---
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
---
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
---
## Laboratorium 5 i 6
Budowa dokumentu XML
>Korzystając z przykładu podanego w skrypcie oraz programu z Laboratorium 4 dodaj do programu nową funkcję umożliwiającą konwersję danych z bazy danych/pliku do formatu XML.
>
>Program powinien posiadać:
>- przycisk "Importuj danych z XML" służący do wczytywania danych o katalogu z pliku XML;
>- przycisk "Eksportuj danych do XML" służący do eksportowania danych o katalogu do pliku XML.
>
>Odczytywany i modyfikowany plik XML powinien być zbudowany według schematu podanego w pliku katalog.xml
>
>Przykładowy wygląd aplikacji będącej rezultatem wykonania zadania został pokazy w pliku mockup4.png
>
>Pamiętaj o: 
>- uwzględnieniu poprawnego działania pozostałych przycisków z programu z Laboratorium 4;
>- możliwości wczytywania danych z jednego źródła i zapisu do innego np. wczytanie danych z pliku XML i zapis do bazy danych;
>- uwzględnieniu o przypadku, w którym należy utworzyć plik XML jeśli wcześniej taki nie istniał.  
>
>W repozytorium umieść plik archiwum zawierający:
>- katalog "projekt5_6" z plikami projektu;
>- katalog "rozwiazanie5_6" z uruchamialnymi plikami rozwiązania;
>- szczegóły ustawienia środowiska testowego zapisane w pliku tekstowym.
### Uruchomienie programu
```console
$ ./src/scripts/Lab5_6.py
```
---
## Laboratorium 7 i 8
Budowa serwisu sieciowego z wykorzystaniem SOAP
> Korzystając z przykładu podanego w skrypcie oraz programu z Laboratorium 2-6 rozbuduj program do postaci aplikacji serwerowej, która wystawia usługi SOAP. Dodatkowo stwórz aplikację klienta (osobne okno graficzne), która będzie odpytywać aplikację serwerową o dane.
>
>Aplikacja serwerowa powinna posiadać:
>- (U1) usługę zwracającą liczbę rekordów w bazie danych przefiltrowaną na podstawie podanego przez klienta producenta;
>- (U2) usługę zwracającą dane z bazy danych przefiltrowane na podstawie podanego przez klienta rodzaju matrycy;
>
>Aplikacja klienta powinna posiadać:
>- [dla U1]
>   - przycisk "liczba laptopów producenta", służący do wyświetlania liczby rekordów w bazie danych przefiltrowanych na podstawie podanego przez użytkowika producenta, po naciśnięciu powinna zostać wywołana usługa SOAP aplikacji serwerowej (U1);
>   - listę rozwijaną z producentami do wyboru, jako kryterium działania metody pod przyciskiem "liczba laptopów producenta"
>   - pole do wyświetlania liczby laptopów spełniających podane kryterium
>- [dla U2]
>   - przycisk "lista laptopów z określoną matrycą" służący do wyświetlania informacji z katalogu o urządzeniach z wybranym przez użytkownika rodzajem matrycy (U2).
>   - listę rozwijaną z rodzajami matryc, jako kryterium działania metody pod przyciskiem "lista laptopów z określoną matrycą"
>   - tabelę do wyświetlania danych laptopów spełniających podane kryterium
>
>Przykładowy wygląd aplikacji będącej rezultatem wykonania zadania został pokazy w pliku mockup5.png
>
>Pamiętaj o uwzględnieniu poprawnego działania pozostałych przycisków aplikacji serwerowej z Laboratoriów 2-6.
>
>W repozytorium umieść plik archiwum zawierający:
>- katalog "projekt7_8" z plikami projektu lub projektów;
>- katalog "rozwiazanie7_8" z uruchamialnymi plikami rozwiązania (aplikacji serwerowej i klienta);
>- szczegóły ustawienia środowiska testowego zapisane w pliku tekstowym.
### Uruchomienie programu
- aplikacja z serwerem
    ```console
    $ ./src/scripts/Lab7_8.py
    ```
- aplikacja kliencka
    ```console
    $ ./src/scripts/Lab7_8_client.py
    ```
---
## Technologie
- [Python 3.6](https://docs.python.org/3.6/ "Dokumentacja Python'a")
- [PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/ "Dokumentacja PyQt5")
- [SQLite](https://www.sqlite.org/docs.html "Dokumentacja SQLite")
- [Zeep](https://python-zeep.readthedocs.io/en/master/ "Dokumentacja Zeep")
- [Ladon](https://ladon.readthedocs.io/en/latest/ "Dokumentacja Ladon")
---
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
## importy do exe
```python
from typing import List, Dict, Tuple
import sqlite3
from xml.etree import ElementTree
from PyQt5 import QtWidgets
from ladon.server.wsgi import LadonWSGIApplication
from ladon.tools.log import (
    set_loglevel,
    set_logfile,
    set_log_backup_count,
    set_log_maxsize,
)
import wsgiref.simple_server
import zeep
```
