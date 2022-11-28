from cassandra.cluster import Cluster

if __name__ == '__main__':
    cluster = Cluster(['host.docker.internal'])
    session = cluster.connect()

    rows = session.execute("SELECT keyspace_name FROM system")
    print(rows)