import random

from cassandra.cluster import Cluster, Session
from cassandra.protocol import SyntaxException

CLUSTER_ADDRESS = 'host.docker.internal'
KEY_SPACE = "mykeyspace"
NAMES = ['Kacper', 'Dominik', 'Marcin', 'Krystian', 'Sebastian']
EMAILS = ['test@test.pl', 'wsad@gmail.com', 'essa@mlodziez.eu', 'users@mat.umk.pl']


def print_all_users(session: Session) -> None:
    results = session.execute('SELECT * FROM users')
    for (identifier, name, email) in results:
        print(f'id={identifier} name={name} email={email}')


def main():
    # connecting to cluster
    cluster = Cluster([CLUSTER_ADDRESS])
    session = cluster.connect()

    # tworzenie przestrzeni kluczy z replikacją typu simple strategy i replication_factor = 2
    session.execute(
        "CREATE KEYSPACE IF NOT EXISTS mykeyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '2' }",
    )
    # ustawienie przestrzeni kluczy, w ktorej bedziemy dzialac
    session.set_keyspace(KEY_SPACE)

    # tworzenie tabeli
    session.execute(
        f'CREATE TABLE IF NOT EXISTS users (id int, name text, email text, PRIMARY KEY (id))'
    )

    # dodawanie danych z parametrami
    for i in range(10):
        session.execute('INSERT INTO users(id, name, email) VALUES ( %(id)s, %(name)s, %(email)s )',
                        {'id': i + 1, 'name': random.choice(NAMES), 'email': random.choice(EMAILS)})

    # proste odczytywanie danych w formie wierszy
    print_all_users(session)

    # update
    for index in range(2, 11, 2):
        session.execute("UPDATE users SET name = 'Zmieniony kacper' WHERE id = %(index)s ", {'index': index})

    print('------------------------')
    print_all_users(session)

    # usuwanie wierszy
    for index in range(1, 11, 2):
        session.execute('DELETE FROM users WHERE id = %(index)s', {'index': index})

    print('------------------------')
    print_all_users(session)


if __name__ == '__main__':
    main()
