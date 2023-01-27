import requests
import json
from pprint import pprint
import PySimpleGUI as sg

sg.theme('Dark')
layout= [[sg.Input(size=(43, 1), key='in')],
        [sg.Button('Найти')]]


window = sg.Window("Поиск пользователя 3000", layout)

while True:
    event, values = window.read()

    # Событие выхода:
    if event in (None, 'Exit'):
        break

    # Событие нажатия кнопки Search
    if event == 'Найти':
        #Получаем инфу
        username = values['in']
        #добавляем в ссылку юзернейм
        url = f"https://api.github.com/users/{username}"
        #Данные json
        user_data = requests.get(url).json()

        try:
            required_data = f"Company: {user_data['company']},\nCreated at: {user_data['created_at']},\nEmail: {user_data['email']},\nID: {user_data['id']},\nName: {user_data['name']},\nURL: {user_data['url']}"
            f = open('user_info.txt','w')
            f.write(required_data)
            sg.Popup('Информация о пользователе сохранена в файл')
            f.close()
        except:
            sg.Popup('Пользователь не найден')