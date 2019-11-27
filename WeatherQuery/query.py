import json
import requests
from json import JSONDecodeError

FILENAME = 'city_code.txt'


def read_code(filename=FILENAME):
    with open(filename, 'r') as f:
        city_code = json.load(f)
    return city_code


def query_code(table, city):
    '''
    table:字典
    city:字符串
    '''
    try:
        code = table[city]
    except KeyError:
        raise
    return code


def query_weather(code):
    html = f'http://wthrcdn.etouch.cn/weather_mini?citykey={code}'

    try:
        info = requests.get(html)
        info.encoding = 'utf-8'
    except requests.ConnectionError:
        raise

    try:
        info_json = info.json()
    except JSONDecodeError:
        return '无法查询'
    # 天气情况
    data = info_json['data']
    city = f"城市：{data['city']}\n"
    today = data['forecast'][0]
    date = f"日期：{today['date']}\n"
    now = f"实时温度：{data['wendu']}度\n"
    temperature = f"温度：{today['high']} {today['low']}\n"
    fengxiang = f"风向：{today['fengxiang']}\n"
    type = f"天气：{today['type']}\n"
    tips = f"贴士：{data['ganmao']}\n"

    return city + date + now + temperature + fengxiang + type + tips
