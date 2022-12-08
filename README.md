# python-cassandra-example


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
