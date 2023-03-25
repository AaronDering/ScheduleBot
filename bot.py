import telebot, json;
from telebot.types import ReplyKeyboardMarkup, KeyboardButton;
def good(s):
        if len(s)in [2,3]:
                if (s[0].isdigit and s[1].isalpha) or(s[0].isdigit and s[1].isdigit and s[2].isalpha):
                        return True;
        else:
                return False;
def change_json(diction):
        with open("users.json","w",encoding="utf-8") as file:
                json.dump(diction, file);
token="yourToken";
bot = telebot.TeleBot(token);
with open("schedule.json", encoding="utf-8") as file:
        sche=json.load(file);
with open("users.json", encoding="utf-8") as userrr:
       userr=json.load(userrr);
previous="";
dayyys=["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
keyboard=ReplyKeyboardMarkup(resize_keyboard=True);
keyboardDay=ReplyKeyboardMarkup(resize_keyboard=True);
keyboard.add(KeyboardButton("Класс"));
keyboard.add(KeyboardButton("Получить расписание"));
keyboardDay.add(KeyboardButton("Понедельник"));
keyboardDay.add(KeyboardButton("Вторник"));
keyboardDay.add(KeyboardButton("Среда"));
keyboardDay.add(KeyboardButton("Четверг"));
keyboardDay.add(KeyboardButton("Пятница"));
keyboardDay.add(KeyboardButton("Суббота"));
@bot.message_handler(commands=["help","start"])
def welcome(message):
        bot.send_message(message.chat.id, "Хочешь расписание?", reply_markup=keyboard);
@bot.message_handler(regexp=r"Класс")
def change_class(message):
        bot.send_message(message.chat.id,"Введи название класса");
        @bot.message_handler(regexp=r"(?:\d\d[abv]|\d[abv])")
        def change(message):
                if good(message.text):
                        if str(message.from_user.id) in userr.keys():
                                if userr[str(message.from_user.id)]!=message.text:
                                        userr[str(message.from_user.id)]=message.text;
                                        change_json(userr);
                        else:
                                userr.update({str(message.from_user.id): message.text});
                                change_json(userr);
                else:
                        bot.send_message(message.chat.id, "Попробуй ещё раз");
                bot.send_message(message.chat.id, "Что дальше?", reply_markup=keyboard);
@bot.message_handler(regexp=r"Получить")
def what_day(message):
        bot.send_message(message.chat.id, "На какой день?", reply_markup=keyboardDay);
        @bot.message_handler(regexp=r"(?:Понедельник|Вторник|Среда|Четверг|Пятница|Суббота)")
        def send_schedule(message):
                if message.text in dayyys:
                        todayDict=sche[message.text];
                        claaass=userr[str(message.chat.id)];
                        scheduleUser="";
                k=1;
                for i in todayDict[claaass]:
                        scheduleUser+=str(k)+". "+i+"\n";
                        k+=1;
                bot.send_message(message.chat.id, scheduleUser);
                bot.send_message(message.chat.id, "Что дальше?", reply_markup=keyboard);
bot.infinity_polling();
