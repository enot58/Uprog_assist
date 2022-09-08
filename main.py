import pyautogui as pag
import pyautogui as PyMasgBox
import pyautogui
from PIL import Image
import tkinter as tk
from tkinter import *
# import gui
import vars
import pickle
import json
import new_f_Two


# поиск 5 и перевод в 13

def entancesF_Two():
    screen = pyautogui.screenshot('screenshot.png')
    print(screen)
    foundThirteen = 0
    while(foundThirteen != 2):
        try:
            screen = pyautogui.screenshot('screenshot.png')
            pyautogui.moveTo(vars.text_5)
            posFive = pag.position()
            #pag.click(posFive.x, posFive.y)
            if (vars.text_5):
                pag.doubleClick(posFive.x, posFive.y)
                screen = pyautogui.screenshot('screenshot.png')
                pag.sleep(0.3)
                pag.moveTo(vars.text_13)
                posThirteen = pag.position()
                pag.click(posThirteen.x, posThirteen.y)
                foundThirteen = foundThirteen + 1
                #pag.alert(text='Найдено', title='Hello', button='OK')
                print('Yes')
        except:
            print('No')

            try:
                screen = pyautogui.screenshot('screenshot.png')
                pag.moveTo(vars.text_top17)
                print('17 ok')
                if(vars.text_top17):
                    pag.moveTo(vars.right_scroll)
                    right_scrollOne = pag.position()
                    pag.click(right_scrollOne.x - 20, right_scrollOne.y, 7, 0.2, 'left')
            except:
                # pag.alert(text='Не найдено', title='Hello', button='OK')
                screen = pyautogui.screenshot('screenshot.png')
                pag.moveTo(vars.right_scroll)
                posRight = pag.position()
                pag.moveTo(posRight.x - 20, posRight.y)

                pag.click(posRight.x, posRight.y, 3, 0.1, 'left')
                pag.moveTo(posRight.x - 20, posRight.y)

    # if(foundThirteen == 2):
    #     return 'true'
    # else:
    #     return 'false'





























# # f = open(r'file.txt', 'wb')
# # obj = ['строка', (2, 4)]
# # pickle.dump(obj, f)
# # f.close()
#
#
# # f = open(r'file.txt', 'rb')
# # obj = pickle.load(f)
# # print(obj)
#
#
# # print(FG.newdf(vars.all_1)['p_y'])
#
#
# # i = 0
# # while(i < len(all_number)):
# #     FG.newdf(all_number[i])
# #     i = i + 1
#
#
# def posScroll():
#     screen = pag.screenshot('screenshot.png')
#     pag.moveTo(vars.entry_up_downV2)
#     up_pos = pag.position()
#     # """
#     #             Запись в файл
#     #         """
#     # filePos = open(r'data/pos.txt', 'wb')
#     # up_posD = up_pos
#     #
#     # pickle.dump(up_posD, filePos)
#     # filePos.close()
#     # """
#     #     Конец
#     # """
#     with open('data/pos.json', 'wb') as write_file:
#         json.dump(up_pos, write_file)
#
#     print(up_pos.y)
#     pag.moveTo(vars.down_scroll)
#     down_pos = pag.position()
#
#     # """
#     #         Запись в файл
#     # """
#     # filePos = open(r'data/pos.txt', 'wb')
#     # down_posD = down_pos
#     # pickle.dump(down_posD, filePos)
#     # filePos.close()
#     # """
#     #     Конец
#     # """
#     # print(down_pos.y)
#
# # posScroll()
#
# # f = open(r'data/pos.txt', 'rb')
# # up_posL = pickle.load(f)
# # down_posL = pickle.load(f)
# #
# # print(up_posL)
# # print(down_posL)
#
#
#
# # pag.mouseDown(button='left', x = up_pos.x, y = up_pos.y)
# # pag.moveTo(up_pos.x, up_pos.y + 180)
# # pag.mouseUp()
# #
# # pag.sleep(3)
# # pag.mouseDown(button='left', x = up_pos.x, y = up_pos.y)
# # pag.moveTo(up_pos.x, up_pos.y + 180)
# # pag.mouseUp()
#
#
#
#
#
# # screen = pag.screenshot('screenshot.png')
# # pag.moveTo(vars.entry_up_downV2)
# # up_pos = {
# #     'up_pos': {
# #         'x': pag.position().x,
# #         'y': pag.position().y
# #     }
# # }
# # with open('data/pos.json', 'w') as write_file:
# #     json.dump(up_pos, write_file, sort_keys=True, indent=4)
# #
# #
# # pag.moveTo(vars.down_scroll)
# # down_pos = {
# #     'down_pos': {
# #         'x': pag.position().x,
# #         'y': pag.position().y
# #     }
# # }
# #
# # with open('data/pos.json', 'a') as write_file:
# #     json.dump(down_pos, write_file, sort_keys=True, indent=4)
#
#
# # with open('data/pos.json') as f:
# #     data = json.load(f)
# # print(data['down_pos'])
#
#
#
#
# # data = {
# #     "country": "Russia",
# #     "vehicle": {
# #         "name": "Volkswagen",
# #         "model": "T-Roc"
# #     }
# # }
# #
# # with open("data/file.json", "w") as file:
# #     json.dump(data, file)
#
#
# # numbers = [1, 2, 3, 4]
# #
# # filename = 'data/file.json'
# # with open(filename, 'w') as f:
# #     json.dump(numbers, f)
# #
# #
# #
# #
# # with open(filename) as f:
# #     numbers = json.load(f)
# #
# # print(numbers)
#
# # username = input("What is your name?")
#
# filename = 'data/file.json'
# # with open(filename, 'w') as f:
# #     json.dump(username, f)
# #     print(f"We'll remember you when you come back? {username}!")
#
#
# # try:
# #     with open(filename) as f:
# #         username = json.load(f)
# # except:
# #     username = input("What is your name?")
# #     with open(filename, 'w') as f:
# #         json.dump(username, f)
# #         print(f"We'll remember you when you come back? {username}!")
# # else:
# #     print(f"Welcome back, {username}")
#
# ii = {
#     'x': 123,
#     'y': 125
# }
#
# with open(filename, 'w') as posX_Y:
#     json.dump(ii, posX_Y)
#
#
#
#
# # ii.age = {
# #     'anna': 33,
# #     'lena': 22
# # }
# with open(filename, 'w') as posX_Y:
#     json.dump(ii, posX_Y)
#
#
#









