import requests
import re
from datetime import datetime

city_code = "260010" # 京都のcityコード
url = "https://weather.tsukumijima.net/api/forecast/city/" + city_code

try:
    response = requests.get(url)
    response.raise_for_status()     # ステータスコード200番台以外は例外とする
except requests.exceptions.RequestException as e:
    print("Error:{}".format(e))

else:
    weather_json = response.json()
    p = "今日の天気は" + weather_json['forecasts'][0]['telop'] + "です" # 0:今日 1:明日 2:明後日
    print(p)
    f = open('tenki.txt', 'w', encoding='UTF-8')
    f.write(p)
    f.close()
