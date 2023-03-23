# Билеотеки
from tkinter import *
from tkinter import ttk
import json

# Функция сохранения

settings = {
    'clicks': '0',
    'upd_co': '1',
    'price': '25',
}

with open('settings.json', 'r') as file:
    settings1 = json.load(file)

#Переменные (Не рекомендуется изменять!)

clicks = int(settings1['clicks'])
upd_co = int(settings1['upd_co'])
price = int(settings1['price'])

# Функция закрытия окна

def finish():
    global clicks
    global upd_co
    global price
    root.destroy() # Закрытие онка ручками
    settings = {
        'clicks': str(clicks),
        'upd_co': str(upd_co),
        'price': str(price),
    }
    with open('settings.json', 'w') as file:
        json.dump(settings, file)
    print('Сохранение успешно!')
    print('Код выхода: 0')

# Функция клика

def click_farm():
    global clicks
    global upd_co
    clicks += upd_co
    # Изменение текста
    lb_cl['text'] = f'Золота: {clicks}'

# Функция улучшения кликов

def upd_clicks():
    global clicks
    global price
    global upd_co
    if clicks >= price:
        clicks -= price
        upd_co += 1
        price = 25 * upd_co
        lb_pr['text'] = f'Цена улучшения: {price} золотых'

# Очистка данных

def clrall():
    settings = {
        'clicks': '0',
        'upd_co': '1',
        'price': '25',
    }
    with open('settings.json', 'w') as file:
        json.dump(settings, file)
    root.destroy()
    print('Очистка завершена! Игра закрывается')
    print('Код выхода 0')

# Создание и настройка окна
root = Tk()
root.geometry('250x200+800+400')

# Создание набора вкладок

tab_control = ttk.Notebook(root)
tab_control.pack(expand=True, fill=BOTH)

# Создание вкладок

game = ttk.Frame(tab_control)
magaz = ttk.Frame(tab_control)
options = ttk.Frame(tab_control)

# Основное окно
root.title('Игра"Кликер"')
root.iconbitmap(default='logo.ico')
root.resizable(False,False)
root.protocol('WM_DELETE_WINDOW', finish)

# Создание взаимодействия с игрой

btnf = ttk.Button(game, text='Кликай!', command=click_farm)
btn_upd_plus = ttk.Button(magaz, text='Улучшение кирки', command=upd_clicks)
lb_cl = ttk.Label(game, text= f'Золота {clicks}')
lb_pr = ttk.Label(magaz, text=f'Цена улучшения {price} золотых')
clear_btn = ttk.Button(options, text=f'Очистка всех данных (Откат невозможен!)', command=clrall)

# Отоброжение элементов
lb_pr.pack(anchor='s', padx=45, ipady=20, fill=X)
lb_cl.pack(anchor=S)

btnf.pack(anchor='s',fill = X, ipady=5, pady = 1)
btn_upd_plus.pack(anchor='sw', fill=X, expand=True, ipady=5)
clear_btn.pack(expand=True, fill=X)

tab_control.add(game, text='Игра')
tab_control.add(magaz, text='Магазин')
tab_control.add(options, text='Настройки')

# Взаимодействие с окном (Нетрогай это!!!)
root.mainloop()