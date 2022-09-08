import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import ttk
from tkinter.ttk import Progressbar
import main
import vars
import FG


window = Tk()
window.geometry('500x500')

"""
 Создание табов
"""
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
"""
    Таб №1
"""
tab_control.add(tab1, text='По очереди')
tab_control.pack(expand=1, fill='both')
"""
    Таб №2
"""

tab_control.add(tab2, text='Функции раздельно')
tab_control.pack(expand=1, fill='both')
"""
    Таб №3
"""

tab_control.add(tab3, text='Данные')
tab_control.pack(expand=1, fill='both')
"""
 Конец табов
"""

"""
      Начало первой функции 
-- Определение положения элементов --
"""
definePos = Label(
    tab1,
    text='Определить положение',
)
definePos.grid(column=0, row = 0)
definePosButtom = Button(
    tab1,
    text = 'Определить'
)
definePosButtom.grid(column=1, row=0)

searchBar = Progressbar(tab1, length = 200)
searchBar.grid(column = 2, row = 0)
searchBar['value'] = 1


window.mainloop()























# def click():
#     lbl = Label(window, text="Привет!")
#     lbl.grid(column=0, row=0)
#
# window = Tk()
# # Здесь заголовок
# window.title("Добро пожаловать!")
# window.geometry('500x500')
#
# tab_control = ttk.Notebook(window)
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)
#
# tab_control.add(tab1, text='Общие функции')
# tab_control.pack(expand=1, fill='both')
#
# tab_control.add(tab2, text='Функции раздельно')
# tab_control.pack(expand=1, fill='both')
#
# # Функция поиска синей
# # Здесь подпись
# lbl_search = Label(
#     tab2,
#     text= 'Поиск синей',
#     font = (
#         40
#     )
# )
# # Здесь расположение подписи
# lbl_search.grid(column=0, row=0)
# # Здесь кнопка
# searchBlue = Button(tab2, text="Поиск", command = new_f_Two.newConnect)
# # Расположение кнопки
# searchBlue.grid(column=1, row=0)
# # прогресс
# searchBar = Progressbar(tab2, length = 200)
# searchBar.grid(column = 2, row = 0)
# searchBar['value'] = 1
#
# # Функция  перехода во входы
# # Здесь переход подпись
# lbl_Next = Label(
#     tab2,
#     text= 'Перейти?',
#     font = (
#         40
#     )
# )
# # Здесь расположение подписи
# lbl_Next.grid(column=0, row=1)
# # Здесь кнопка
# nextBtn = Button(tab2, text="Да", command = new_f_Two.entrancesF)
# # Расположение кнопки
# nextBtn.grid(column=1, row=1)
# # прогресс
# # searchBar = Progressbar(tab2, length = 200)
# # searchBar.grid(column = 2, row = 0)
# # searchBar['value'] = 1
#
#
#
# lbl_Down = Label(
#     tab2,
#     text = 'Пролистать вниз?',
#     font = (
#         40
#     )
# )
# lbl_Down.grid(column = 0, row = 3)
# btn_Down = Button(tab2, text = 'Вниз', command = new_f_Two.entryDown)
# btn_Down.grid(column = 1, row = 3)
#
#
#
#
#
#
# ############################################
# # Общая функция старта
# #############################################
# mainStart = Button(tab1, text = 'Start', command = main.startSearch).pack()
#
# window.mainloop()
#
#
#
#
#
