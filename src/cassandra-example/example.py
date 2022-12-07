from cassandra.cluster import Cluster

CLUSTER_ADDRESS = 'host.docker.internal'

def main():
    # connecting to cluster
    cluster = Cluster([CLUSTER_ADDRESS])
    session = cluster.connect()

    print(session.execute("SELECT release_version FROM system.local").one())

    # create a new key space
    session.execute
    # ja tworze tabele

    # ja dodaje dane do tabeli

    # dominik kontrolnie może napisać sqlkę listującą te tabele

    # odpalam selecta na bazunie


if __name__ == '__main__':
    main()
