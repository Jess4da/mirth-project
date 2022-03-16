import configparser
import re
import json


class sys_lang:
    __sys_lang = configparser.ConfigParser()
    __sys_lang.read('lang/menu.ini', encoding='utf-8')

    @classmethod
    def lang(cls, l):
        return cls.__sys_lang[l]


def TRANSLATE(wrd: str):
    if re.match(r'[a-zA-Z]', wrd):
        data = {}
        with open('lang/words.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get(wrd, '')
    else:
        data = {}
        with open('lang/words.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return list(data.keys())[list(data.values()).index(wrd)]


if __name__ == '__main__':
    print(TRANSLATE('แมว'))
