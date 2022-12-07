import random

from cassandra.cluster import Cluster
from cassandra.protocol import SyntaxException

CLUSTER_ADDRESS = 'localhost'
KEY_SPACE = "mykeyspace"
NAMES = ['Kacper', 'Dominik', 'Marcin', 'Krystian', 'Sebastian']
EMAILS = ['test@test.pl', 'wsad@gmail.com', 'essa@mlodziez.eu', 'users@mat.umk.pl']


def main():
    # connecting to cluster
    cluster = Cluster([CLUSTER_ADDRESS])
    session = cluster.connect()

    print(session.execute("SELECT release_version FROM system.local").one())

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

    # odczytywanie danych
    results = session.execute('SELECT * FROM users')
    for result in results:
        print(result)



if __name__ == '__main__':
    main()
