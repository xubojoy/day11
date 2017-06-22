#Author:xubojoy
# from urllib import request, parse
# from xml.parsers.expat import ParserCreate
#
# def fetch_xml(url):
#     with request.urlopen(url) as f:
#         data = f.read()
#         return data.decode('utf-8')
#
#
#
#
# class WeatherSaxHandler():
#     def __init__ (self):
#         self.weather_data={}
#         self.date_index=0
#
#     def start_element(self,name,attrs):
#         if name=='yweather:location':
#             self.weather_data['city']=attrs['city']
#             self.weather_data['country']=attrs['country']
#         if name=='yweather:forecast' and self.date_index<2:
#             if self.date_index==0:
#                 self.weather_data['today'] = {}
#                 self.weather_data['today']['text'] = attrs['text']
#                 self.weather_data['today']['low'] = int(attrs['low'])
#                 self.weather_data['today']['high'] = int(attrs['high'])
#                 self.date_index += 1
#             elif self.date_index==1:
#                 self.weather_data['tomorrow'] = {}
#                 self.weather_data['tomorrow']['text'] = attrs['text']
#                 self.weather_data['tomorrow']['low'] = int(attrs['low'])
#                 self.weather_data['tomorrow']['high'] = int(attrs['high'])
#                 self.date_index += 1
#     def end_element(self,name):
#         pass
#
#     def char_data(self,text):
#         pass
#
# def parse_weather(xml):
#     handler=WeatherSaxHandler()
#     parse=ParserCreate()
#     parse.StartElementHandler=handler.start_element
#     parse.EndElementHandler=handler.end_element
#     parse.CharacterDataHandler=handler.char_data
#     parse.Parse(xml)
#     return handler.weather_data
#
# d='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22beijing%2C%20china%22)%20and%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeysw%2C%20scotland%22)%20and%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
#
# weather = parse_weather(fetch_xml(d))
#
# print('Weather:', str(weather))


import os
from urllib import request
from bs4 import BeautifulSoup

'html_code.txt contains the source code of url'

def fetch_xml():
    # req = request.Request(url)
    # page = request.urlopen(req)
    # f = page.read()
    file_path = os.path.join(os.path.dirname(__file__), 'html_code.txt')
    f = open(file_path, 'rb').read()
    soup = BeautifulSoup(f, 'html.parser')

    for j in soup.findAll('div', {'class': 'BdB Bds(d) Bdbc(#fff.12) Fz(1.2em) Py(2px) O(0) Pos(r) forecast-item'}):
        print('星期:', j.find('div', class_="D(ib) Va(m) W(1/4)").text)
        print('天气:', j.select('span[class="D(ib) Va(m) W(1/4) Ta(c)"] > img')[0]['title'].strip())
        a = j.select('span[class="D(ib) Va(m) W(1/4) Ta(end)"]')[0].get_text()
        print('温度:', 'high:%sF, low:%sF' % (a[0:3], a[3:6]))
        print('-' * 30)

if __name__ == "__main__":
    # d = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22beijing%2C%20china%22)%20and%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeysw%2C%20scotland%22)%20and%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
    fetch_xml()