from pyignite import Client

# https://apache-ignite-binary-protocol-client.readthedocs.io/en/latest/examples.html

def main():
    client = Client()
    client.connect('127.0.0.1', 10800)

    my_cache = client.get_or_create_cache('my cache')
    my_cache.put('my key', 42)

    result = my_cache.get('my key')
    print('my key: {}'.format(result))


if __name__ == '__main__':
    main()