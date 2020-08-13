from pyignite import Client

def main():
    client = Client()
    client.connect('127.0.0.1', 10800)

    query = ''

    result = client.sql(query)

    for row in result:
        print(row)


if __name__ == '__main__':
    main()