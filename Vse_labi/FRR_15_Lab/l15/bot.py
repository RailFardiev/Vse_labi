import telebot
from telebot import types
from datetime import date
import json
import io
import random
import sqlite3;

API_TOKEN = '7098606093:AAFxHKhVEra5zVTyvuJ1pM30Id_WZHqs380'

bot = telebot.TeleBot(API_TOKEN)
def create_connection():
    conn = sqlite3.connect('schedule.db')
    return conn

def is_day_name(day_name):
    days = ["понедельник", "среда", "четверг", "пятница", "вторник"]
    return day_name.lower() in days

def get_schedule(day_name):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT subject, start_time, room_numb FROM timetable WHERE day = ?", (day_name,))
    schedule = cursor.fetchall()

    conn.close()

    return schedule

def get_format_schedule(day_name):
    schedule = get_schedule(day_name)

    formattedString = f" *{day_name.capitalize()}*\n\n"
    for subject_info in schedule:
        subject, time, classroom = subject_info
        formattedString += f"Предмет: {subject}\nВремя: {time}\nАудитория: {classroom}\n\n"

    return formattedString

def get_curweek_schedule():
    days = ["понедельник","вторник", "среда", "четверг", "пятница"]

    s = "Расписание на эту неделю\n\n"
    for day in days:
        s += get_format_schedule(day) + "\n"

    return s

week_keyboard = (
    types.ReplyKeyboardMarkup(resize_keyboard=True)
    .add(types.KeyboardButton("Понедельник"))
    .add(types.KeyboardButton("Вторник"))
    .add(types.KeyboardButton("Среда"))
    .add(types.KeyboardButton("Четверг"))
    .add(types.KeyboardButton("Пятница"))
    .add(types.KeyboardButton("Расписание"))
)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Используйте /help если у вас возникли вопросы", reply_markup=week_keyboard)

@bot.message_handler(commands=['help'])
def handle_help(message):
    help_message = """
Привет! Я бот для удобного просмотра расписания в институте.

Создан студентом группы 4311-22 Фардиевым Раилем.
Доступные команды:

/start - начать взаимодействие с ботом
/help - доступные команды
/kstu - получить ссылку на официальный сайт КНИТУ
/vk - получить ссылку на официальную группу вконтакте КНИТУ
/location - получить адреса всех учебных корпусов
    """

    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=['location'])
def handle_location(message):
    locations = """
    Местонахождение учебных корпусов:

    Корпус «А» - г. Казань, ул. К. Маркса, 68
    Корпус «Б», «В», «О» - г. Казань, ул. К. Маркса, 72
    Корпус «Д», «Е», «Л», «М» - г. Казань, ул. Сибирский тракт, 12
    Корпус «К» - г. Казань, ул. Толстого, 8/31
    Корпус «Г» - г. Казань, ул. Попова, 10
    Корпус «И» - г. Казань, ул. Сибирский тракт, 41
    Корпус «Т» - г. Казань, ул. Толстого, 6 корпус 1
    """

    bot.send_message(message.chat.id, locations)

@bot.message_handler(commands=['vk'])
def handle_vk_group(message):
    bot.send_message(message.chat.id, "Группа Казанского национального технического университета (КНИТУ) во ВКонтакте: https://vk.com/knitu")

@bot.message_handler(commands=['kstu'])
def kstu_handler(message):
    bot.send_message(message.chat.id, 'https://www.kstu.ru/')

@bot.message_handler(func=lambda message: message.text.lower() == "лучший вуз")
def handle_wheretogo(message):
    bot.send_message(message.chat.id, "КНИТУ")

@bot.message_handler(func=lambda message: message.text.lower() == "когда домой")
def handle_scholarship(message):
    bot.send_message(message.chat.id, "Скоро")

@bot.message_handler(func=lambda message: message.text.lower() == "напиши фамилию писателя")
def handle_scholarship(message):
    l = [
        "Пушкин",
        "Лермонтов",
        "Достоевский",
        "Толстой",
        "Тургенев"
    ]

    bot.send_message(message.chat.id, "Фамилия известного писателя: " + random.choice(l))

@bot.message_handler(func=lambda message: True)
def handle_day(message):
    text = message.text.lower()

    if is_day_name(text):
        schedule = get_format_schedule(text)
        bot.send_message(message.chat.id, schedule)

    elif text == "расписание":
        schedule = get_curweek_schedule()
        bot.send_message(message.chat.id, schedule)

    else:
        bot.send_message(message.chat.id, "Извините, я вас не понял")

bot.infinity_polling()
# Создание таблиц
# cursor.execute('''CREATE TABLE IF NOT EXISTS subject (name TEXT PRIMARY KEY)''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS teacher (id INTEGER PRIMARY KEY AUTOINCREMENT, full_name TEXT, subject TEXT, FOREIGN KEY (subject) REFERENCES subject(name))''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS timetable (id INTEGER PRIMARY KEY AUTOINCREMENT, subject_name TEXT, day TEXT, room_numb TEXT, start_time TEXT, FOREIGN KEY (subject_name) REFERENCES subject(name))''')

# # Загрузка данных из JSON файла



# cursor.execute('INSERT OR IGNORE INTO subject (name) VALUES (?)', ('СИИ',))
# cursor.execute('INSERT OR IGNORE INTO subject (name) VALUES (?)', ('ЗИ',))
# cursor.execute('INSERT OR IGNORE INTO subject (name) VALUES (?)', ('ФИЗ-РА',))
# cursor.execute('INSERT OR IGNORE INTO subject (name) VALUES (?)', ('ЭП',))
# cursor.execute('INSERT OR IGNORE INTO subject (name) VALUES (?)', ('АИС',))
# cursor.execute('INSERT INTO teacher (full_name, subject) VALUES (?, ?)', ('Курбангалеев', 'СИИ'))
# cursor.execute('INSERT INTO teacher (full_name, subject) VALUES (?, ?)', ('Курбангалеев', 'ЗИ'))
# cursor.execute('INSERT INTO teacher (full_name, subject) VALUES (?, ?)', ('Вотякова', 'РПИ'))
# cursor.execute('INSERT INTO teacher (full_name, subject) VALUES (?, ?)', ('Екатерина Феликсовна', 'ЭП'))
# cursor.execute('INSERT INTO teacher (full_name, subject) VALUES (?, ?)', ('Яна Сергеевна', 'ФИЗ-РА'))
# cursor.execute('INSERT INTO teacher (full_name, subject) VALUES (?, ?)', ('Панченко', 'ПИС'))
# cursor.execute('INSERT INTO teacher (full_name, subject) VALUES (?, ?)', ('Титовцев', 'АИС'))

# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('СИИ', 'понедельник', '9:40', 'О105'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('ЗИ', 'понедельник', '11:20', 'В302'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('ЗИ', 'понедельник', '13:00', 'В302'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('РПИ', 'понедельник', '14:40', 'В101'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('ФИЗ-РА', 'вторник', '8:00', 'Мирас'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('ПИС', 'среда', '9:40', 'В101'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('ПИС', 'среда', '11:20', 'В101'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('ЭП', 'среда', '13:00', 'В318'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('ЭП', 'среда', '14:40', 'В318'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('АИС', 'четверг', '11:20', 'В101'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('АИС', 'четверг', '13:00', 'В302'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('АИС', 'четверг', '14:40', 'В302'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('РПИ', 'пятница', '8:00', 'В302'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('РПИ', 'пятница', '9:40', 'В302'))
# cursor.execute('INSERT INTO timetable (subject, day, start_time, room_numb) VALUES (?, ?, ?, ?)', ('ФИЗ-РА', 'пятница', '13:00', 'Мирас'))