import telebot
from config import Config
from schedule import Schedule
from week_type import weekType

schedule = Schedule()
bot = telebot.TeleBot(Config.TOKEN)


class Commands:
    def __init__(self):
        self.text = None
        self.chat = None

    @bot.message_handler(commands=['help'])
    def help(self):
        text = f"Тут всього дві команди якщо не рахувати цю.\n /week_type Повертає значення чисельник знаменник \n " \
               f"/schedule <date> Повертає розклад, якщо <date> не вказана повертає розклад на сьогодні, в значення " \
               f"date вписується день тижня наприклад\n''/schedule <пн>'',''/schedule <вт>'' "
        bot.send_message(self.chat.id, text)

    @bot.message_handler(commands=['schedule'])
    def schedule(self):
        text = self.text
        schedule.week_correct()
        try:
            start = text.index('<')
            stop = text.index('>')
            date = text[start + 1:stop]
            days_dict = {'пн': schedule.mon, 'вт': schedule.tue, 'ср': schedule.wed, 'чт': schedule.thu,
                         'пт': schedule.fri}
            if days_dict.get(date, False):
                text = days_dict.get(date)
            else:
                text = 'Невірний формат <date>'
        except ValueError:
            if len(text) == 9:
                text = schedule.schedule_today()
            else:
                text = 'Команда вказана невірно'
        bot.send_message(self.chat.id, text)

    @bot.message_handler(commands=['week_type'])
    def week_type(self):
        text = weekType()
        bot.send_message(self.chat.id, text)


bot.polling(none_stop=True)
