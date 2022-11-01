
import telebot
import GeoData
from requests import get
from json import loads
import dateutil.parser
import datetime

#ЭТИ ДАННЫЕ НУЖНО БУДЕТ СПРЯТАТЬ в env(для демонстрации оставим так)!!!
'''SETTINGS'''
CITI_FOUND = 'Antalya'
ACCUWEATHER_TOKEN = ''
TELEGRAM_TOKEN = ''
'''SETTINGS'''


def weather(cod_loc: str, token_accu: str):

    url_weather = f'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{cod_loc}?apikey={token_accu}&language=ru&metric=True'
    response = get(url_weather, headers={"APIKey": token_accu})
    json_data = loads(response.text)
    #print(json_data)
    dict_weather = dict()
    dict_weather['DateTime'] = json_data[0]['DateTime']
    dict_weather['mlink'] = json_data[0]['MobileLink']
    dict_weather['dlink'] = json_data[0]['Link']
    dict_weather['temp'] = json_data[0]['Temperature']
    dict_weather['sky'] = json_data[0]['IconPhrase']
    return dict_weather


def main():

    # Создаем экземпляр бота
    bot = telebot.TeleBot(TELEGRAM_TOKEN)

    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'Привет, я бот погоды в Анталии.\n Введи /commands чтобы узнать список команд')

    @bot.message_handler(commands=["commands"])
    def commands(m, res=False):
        bot.send_message(m.chat.id, "Список команд :\n /start - приветстиве;\n /today - погода сегодня;\n /commands - список команд;")

    @bot.message_handler(commands=["today"])
    def today(m, res=False):
        bot.send_message(m.chat.id, "Прогноз погоды сегодня в Анталии")
        #Получаем данные широты и долготы и узнём код местности
        lat, lon = GeoData.posittion(CITI_FOUND)
        CityKey = GeoData.code_location(lat, lon, ACCUWEATHER_TOKEN)
        dweather= weather(CityKey, ACCUWEATHER_TOKEN);
        date = dateutil.parser.parse(dweather['DateTime'], ignoretz=True)
        out_str1 = 'Дата:'+ str(date.day) + '-' + str(date.month) + '-' + str(date.year) 
        out_str2 = 'Температура :' + str(dweather['temp']['Value']) + 'C ' + str(dweather['sky'])
        bot.send_message(m.chat.id, out_str1)
        bot.send_message(m.chat.id, out_str2)

    # Получение сообщений от юзера
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        bot.send_message(message.chat.id, 'Я не знаю такой команды :(')

    # Запускаем бота
    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    main()
