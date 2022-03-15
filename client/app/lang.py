import configparser


class sys_lang:
    __sys_lang = configparser.ConfigParser()
    __sys_lang.read('lang/menu.ini', encoding='utf-8')

    @classmethod
    def lang(cls, l):
        return cls.__sys_lang[l]
