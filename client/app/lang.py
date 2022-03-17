import configparser
import json


class sys_lang:
    __sys_lang = configparser.ConfigParser()
    __sys_lang.read('lang/menu.ini', encoding='utf-8')

    @classmethod
    def lang(cls, l):
        return cls.__sys_lang[l]


def TRANSLATE(wrd: str, to='th'):
    if to == 'th':
        data = {}
        with open('lang/words.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get(wrd, None)
    elif to == 'en':
        data = {}
        with open('lang/words.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        if wrd not in list(data.values()):
            return "Wrong"
        return list(data.keys())[list(data.values()).index(wrd)]
    return wrd


if __name__ == '__main__':
    print(TRANSLATE('แมว'))
