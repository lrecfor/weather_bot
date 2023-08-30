from bs4 import BeautifulSoup
import requests
import nest_asyncio
nest_asyncio.apply()


class Parser:

    def __init__(self, city_name):
        self.city = city_name
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 "
                          "Safari/537.36"
        }
        self.temp = ''
        self.time = ''
        self.wind = ''
        self.vl = ''

    def parse_weather(self):
        session = requests.Session()
        response = session.get(f"https://yandex.ru/pogoda/"+self.city.lower(), headers=self.headers)

        bs = BeautifulSoup(response.text, "html.parser")
        self.temp = bs.find_all('span', 'temp__value temp__value_with-unit')[1].text
        self.time = bs.find('time', 'time fact__time').text[7:-2]
        self.wind = bs.find('span', 'wind-speed').text + " " + bs.find('span', 'fact__unit').text
        self.vl = bs.find('div', 'term term_orient_v fact__humidity').text.split("%")[1]

    def get_weather(self):
        self.parse_weather()
        return str('Город: ' + self.city + '\n' + 'Время: ' + self.time + '\n'
                   + 'Температура: ' + self.temp + '\n' + 'Ветер: ' + self.wind + '\n' + self.vl + "%")