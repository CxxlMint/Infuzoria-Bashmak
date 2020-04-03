# 2453f743a9720b082acd93fbecb88e9fde7a4d737fbd4968fb89d00f54d305ad651ecfafc7f90b0d9f3ae

import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from commander.commander import Commander
from vk_bot import VkBot


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# API-ключ
token = "2453f743a9720b082acd93fbecb88e9fde7a4d737fbd4968fb89d00f54d305ad651ecfafc7f90b0d9f3ae"
# Авторизация
vk = vk_api.VkApi(token=token)
# Работа с сообщениями
longpoll = VkLongPoll(vk)
commander = Commander()
print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print(f'New message from {event.user_id}', end='')
            bot = VkBot(event.user_id)
            if event.text[0] == "/":
                write_msg(event.user_id, commander.do(event.text[1::]))
            else:
                write_msg(event.user_id, bot.new_message(event.text))
            print('Text: ', event.text)
            print("-------------------")
