import pyautogui as pag
import pyautogui as PyMasgBox
import pyautogui
from PIL import Image
import tkinter as tk
from tkinter import *
import gui
import vars

"""
 Данная функция определяет состояние каналов
 возвращает серый, синий, зелёный, жёлтый
"""

def newdf(x):
    screen = pag.screenshot('screenshot.png')
    i = 0
    name_i = ''
    active = 'false'
    while (len(x) > i or active == 'true'):
        try:
            pag.moveTo(x[i])
            print('yes')
            active = 'true'
            print(x[i] + ' найдено')
            name_i = x[i]
            break
        except:
            print('none')
        i = i + 1
        print(name_i)
    return {
        'name': name_i,
        'p_x': pag.position().x,
        'p_y': pag.position().y
    }


"""
 --- Функция передвижения ползунка вверх---
"""











































# class NumberColor:
#     def __init__(self, name):
#         self.name = newdf(name)['name'],
#         self.color = newdf(name)['name'],
#         self.pos_x = newdf(name)['p_x'],
#         self.pos_y = newdf(name)['p_y']
#
#     def newdf(name):
#         i = 0
#         name_i = ''
#         active = 'false'
#         while (len(name) > i or active == 'true'):
#             try:
#                 pag.moveTo(name[i])
#                 print('yes')
#                 active = 'true'
#                 print(name[i] + ' найдено')
#                 name_i = name[i]
#                 break
#             except:
#                 print('none')
#             i = i + 1
#             print(name_i)
#         return {
#             'name': name_i,
#             'p_x': pag.position().x,
#             'p_y': pag.position().y
#         }
#
# one = NumberColor(vars.all_1)

