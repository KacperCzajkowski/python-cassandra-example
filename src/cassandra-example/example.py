from cassandra.cluster import Cluster

if __name__ == '__main__':
    cluster = Cluster(['host.docker.internal'])
    session = cluster.connect()

    print(session.execute("SELECT release_version FROM system.local").one())
    # ja tworze tabele

    # ja dodaje dane do tabeli

    # dominik kontrolnie może napisać sqlkę listującą te tabele

    # odpalam selecta na bazunie