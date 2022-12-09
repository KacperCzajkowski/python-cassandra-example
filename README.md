# python-cassandra-example

### Instalacja dockera
## Windows
1. aby zainstalować dockera wymagane jest środowisko linuxowe dla winowsa(wsl 2)
https://learn.microsoft.com/en-us/windows/wsl/install
Istotne jest zainstalowwanie wsl w wersji 2. 
Dystrybucja linuxa nie jest ważna może być domyślna 
2. Instalacja Dockera  
https://docs.docker.com/desktop/install/windows-install/ 
#instrukcja wideo 
https://www.youtube.com/watch?v=2ezNqqaSjq8

## Linux
https://docs.docker.com/engine/install/ubuntu/
Upewnijcie się, że dodaliście użytkownika do grupy docker.
Jeżeli  będą problemy z docker compose należy go doinstalować  
https://docker-docs.netlify.app/compose/install/


## Uwaga
Poniższe  komendy wykonujemy w terminalu Linuxa. 
Osoby z Windowsem odpalają dystrybucje linuxa zainstalowaną wraz z wsl.

### Instalacja narzędzia make
Żeby zainstalować make'a należy wykonać polecenie:
```bash
sudo apt install make 
```

## Uwaga
Przed wykonaniem kolejnych etapów należy posiadać już zainstalowane takie narzędzia jak: docker, docker-compose oraz make.


## Pierwsze uruchomienie
Przed rozpoczęciem pracy należy uruchomić komendę:
```bash
make build
```
To pobierze odpowiednie zależności z internetu i zbuduje obraz.

## Uruchomienie bazy danych Cassandra
W celu uruchomienia bazy danych należy wykonać polecenie:
```bash
make cassandra
```
Ono uruchomi bazę danych jako daemon, który będzie działał w tle.
W celu sprawdzenia, czy się udało można wykonać polecenie:
```bash
make list-containers
```
Ono powinno wylistować wszystkie aktywne kontenery (w naszym przypadku 1)

## Casandra bez docker-compose 
Instrukcja instalacji casandry wraz CQLSH
https://cassandra.apache.org/_/quickstart.html

Dokumentacja casandry 
https://cassandra.apache.org/doc/latest/

## Uruchamianie skryptów
### Zalecane podejście
Należy uruchomić komendę:
```bash
make bash
```
Ona przeniesie nas do kontenera zawierającego pythona oraz zainstalowane potrzebne paczki.
Tam możemy uruchamiać skrypty poprzez `python3 sciezka_do_skrypu`
### Alternatywne podejście
Dla osób posiadających interpreter Pythona w wersji 3.8 w górę oraz menadżera paczek `pip` może po prostu zainstalować paczki z projektu.
