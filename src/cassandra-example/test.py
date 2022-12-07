from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

KEYSPACE = "testkeyspace"


def main():
    cluster = Cluster(['192.168.128.186'])
    session = cluster.connect()

    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s 
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' } 
        """ % KEYSPACE)

    session.set_keyspace(KEYSPACE)

    session.execute("""
        CREATE TABLE IF NOT EXISTS testkeyspace.mytable (
            thekey text,
            col1 text,
            col2 text,
            PRIMARY KEY (thekey, col1)
        )
        """)

    query = SimpleStatement("""
        INSERT INTO mytable (thekey, col1, col2)
        VALUES (%(key)s, %(a)s, %(b)s)
        """, consistency_level=ConsistencyLevel.ONE)

    prepared = session.prepare("""
        INSERT INTO mytable (thekey, col1, col2)
        VALUES (?, ?, ?)
        """)

    for i in range(10):
        session.execute(query, dict(key="key%d" % i, a='a', b='b'))
        session.execute(prepared.bind(("key%d" % i, 'b', 'b')))

    future = session.execute_async("SELECT * FROM mytable WHERE col1 = 'b'")

    rows = future.result()

    for (thekey, col1, col2) in rows:
        print(f'{thekey} {col1} {col2}')

    # session.execute("DROP KEYSPACE " + KEYSPACE)


#

if __name__ == "__main__":
    main()
