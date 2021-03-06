import bs4 as bs4
import requests, random


class VkBot:
    def __init__(self, user_id):
        print("\nСоздан объект бота!")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._COMMANDS = ["ПРИВЕТ", "!ПОГОДА", "!ВРЕМЯ", "ПОКА", "!КОМАНДЫ", "!ЧИСЛО", '!МОНЕТКА', 'ИГРА КИЛЛЕР',
                          '!ЦИТАТА', "ИГРА ПРИКЛЮЧЕНИЕ", "АУФ", '!ШАР', '!ВЫБЕРИ', "ПОМОЩЬ"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

    def new_message(self, message):
        # Привет
        if message.upper() == self._COMMANDS[0]:
            return f"Привет-привет, {self._USERNAME}! " + str(
                random.choice(['&#128521;', '&#128524;', '&#9995; &#128519;']))
        # Погода
        elif message.upper().split(' ')[0] == self._COMMANDS[1]:
            pass
            #return self._get_weather()
        # Время
        elif message.upper() == self._COMMANDS[2]:
            return self._get_time()
        # Пока
        elif message.upper() == self._COMMANDS[3]:
            return f"Пока-пока, {self._USERNAME}!"
        elif message.upper() == self._COMMANDS[4] or message.upper() == self._COMMANDS[13]:
            return f"Список команд:\n" \
                   f"\n" \
                   f"Развлечения &#127918;:\n" \
                   f"Игра киллер - регистрация на игру. &#128299;\n" \
                   f"Игра приключение - начать приключение в фентезийном мире. &#128481;&#128737;\n" \
                   f"Анонимный чат - анонимный чат с другими пользователями &#9993;\n" \
                   f"!Монетка - подбросить монетку (орел/решка). &#127922;\n" \
                   f"!Цитата - мудрая цитата. ☝\n" \
                   f"!Шар [текст] - шар предсказаний. &#128302;\n" \
                   f"!Выбери [фраза 1] или [фраза 2] - шар предсказаний. &#9878;\n" \
                   f"написать шутку: [ваша шутка] - записать шутку в список шуток\n" \
                   f"шутка - рандомная шутка других пользователей\n" \
                   f"\n" \
                   f"Полезное &#127891;:\n" \
                   f"!Погода - для просмотра погоды в Москве. &#9728;\n" \
                   f"!Время - для просмотра времени в Москве. &#127763;\n" \
                   f"!Число [от]   [до] - генерация рандомного числа. &#128290;\n" \
                   f"переводчик - переводчик &#128292;\n" \
                   f"почтовый индекс [адрес] - почтовый индекс по заданному адресу &#128234;"
        elif message.upper()[0:6] == self._COMMANDS[5]:
            if len(message.split(' ')) != 3:
                return f"Неверный синтаксис, надо вводить так:\n" \
                       f"!Число [от] [до]"
            else:
                if int(message.split(' ')[1]) > int(message.split(' ')[2]):
                    return f"Первое число больше второго &#128530;"
                else:
                    return f"Ваше число: " + str(random.randint(int(message.split(' ')[1]), int(message.split(' ')[2])))
        elif message.upper() == self._COMMANDS[6]:
            return f"Иии выпадает! " + random.choice(['Орёл', 'Решка']) + ' ' + str(
                random.choice(['&#127773;', '&#128516;', '&#128527;', '&#128517;']))
        elif message.upper() == self._COMMANDS[7]:
            return "Отлично, для регитрации на игру отправьте свою фотографию &#128100;, чтобы другие игроки смогли вас" \
                   " найти &#8986;"
        elif message.upper() == self._COMMANDS[8]:
            with open('citata.txt', 'r') as file:
                line = file.readlines()
                return line[random.randint(0, 12)].encode("utf-8")
        elif message.upper() == self._COMMANDS[9]:
            return "Вы начали игру {название еще не придкмал}.\n для выхода из игры напишите: выход игра приключение." \
                   "\n для сохранения игры напишите: сохранить игра приключение.\n для загрузки сохранения напишите:" \
                   " загрузить игра приключение.\n чтобы начать напишите: начать приключение."
        elif message.upper() == self._COMMANDS[10]:
            return "Выкатывает со дворов!"
        elif message.upper().split(' ')[0] == self._COMMANDS[11]:
            if len(message.split(' ')) < 2:
                return "Неправильный синтаксис:\n" \
                       "!Шар [текст] - верный синтаксис."
            else:
                return random.choice(
                    ['Хорошие перспективы.', 'Даже не думай.', 'Скорее да, чем нет.', 'Скорее нет, чем да.',
                     'Никаких сомнений.', 'Спроси позже.', 'Бесспорно.', 'Определённо да.',
                     'Сконцентрируйся и спроси опять.', 'Лучше не рассказывать.'])
        elif message.upper().split(' ')[0] == self._COMMANDS[12]:
            if 'или' not in message:
                return "Неправильный синтаксис:\n" \
                       "!Выбери [фраза 1] или [фраза 2] - верный синтаксис."
            elif message[-3:] == 'или':
                return "Неправильный синтаксис:\n" \
                       "!Выбери [фраза 1] или [фраза 2] - верный синтаксис."
            else:
                message = message[8:]
                message = message.split(' или ')
                if len(message) > 2:
                    return 'Слишком много "или".'
                else:
                    return 'Мой выбор: ' + str(random.choice(message))
        else:
            return "Не понимаю о чем вы... &#128530;\n Для списка команд напишите:\n" \
                   "!команды"

    def _get_time(self):
        request = requests.get("https://my-calend.ru/date-and-time-today")
        b = bs4.BeautifulSoup(request.text, "html.parser")
        return self._clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]

    @staticmethod
    def _clean_all_tag_from_str(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True
        return result

    ''''@staticmethod
    def _get_weather(city=str("Москва")) -> list:
        owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language='ru')
        place = city
        observation = owm.weather_at_place(place)
        w = observation.get_weather()
        return 'В городе ' + city + ' сейчас ' + w.get_detailed_status() + ' и ' + str(
            w.get_temperature('celsius')['temp']) + ' градусов по Цельсию.'''
