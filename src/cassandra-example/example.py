from cassandra.cluster import Cluster

if __name__ == '__main__':
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    print(session.execute("SELECT release_version FROM system.local").one())
