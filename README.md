# IS-Projekt
Integracja Systemów Projekt
- Laboratorium 1 - Pliki tekstowe, odczyt danych
- Laboratorium 2 - Praca w trybie graficznym
- Laboratorium 3 - baza danych do celów integracyjnych
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
$ ./src/scripts/read_flat_file_line.py resource/katalog.txt
```
- wersja wczytująca do data frame:
```console
$ ./src/scripts/read_flat_file_df.py resource/katalog.txt
```
## Laboratorium 2 użycie
```console
$ ./src/scripts/read_n_save_file_gui.py
```
## Laboratorium 3 użycie
```console
$ ??
```
## Technologie
- [Python 3.6](https://docs.python.org/3.6/ "Dokumentacja Pythona")
- [Docker 18.09.7](https://docs.docker.com/ "Dokumentacja Dokera")
- [Docker Compose 1.24.1](https://docs.docker.com/compose/ "Dokumentacja Docker Compose")
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
## Uruchomienie serwera mySQL
```console
$ cd resource/
```
```console
$ docker-compose up
```