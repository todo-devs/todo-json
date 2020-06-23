from hashlib import sha1
from json import dump


def main():
    result = {}
    with open('config.json', encoding='utf-8') as file:
        text = file.read()
        cache = sha1(text.encode())
        result['hash'] = cache.hexdigest()
    with open(f'hash.json', mode='w', encoding='utf-8') as file:
        dump(result, file, ensure_ascii=False)


if __name__ == '__main__':
    main()
