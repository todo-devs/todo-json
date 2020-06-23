from hashlib import sha1
from json import dump
from requests import get


def main():
    result = {}
    json = get('https://raw.githubusercontent.com/todo-devs/todo/master/config/ussd_codes.json')
    with open('config.json', mode='w', encoding='utf-8') as file:
        file.write(json.text)
    with open('config.json', encoding='utf-8') as file:
        text = file.read()
        cache = sha1(text.encode())
        result['hash'] = cache.hexdigest()
    with open(f'hash.json', mode='w', encoding='utf-8') as file:
        dump(result, file, ensure_ascii=False)


if __name__ == '__main__':
    main()
