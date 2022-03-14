import configparser

config = configparser.ConfigParser()
config.read('config.ini')

if __name__ == '__main__':
    # print(type(config['SERVER']['ไอพี']))
    import json
    data = {
    }
    with open('th.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    print(data['แอปเปิ้ล'])
