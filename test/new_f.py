# import posix

import pyautogui as pag
#import pyautogui as PyMasgBox
import pyautogui
#from PIL import Image
import vars

# функция ищет цифру серую
def searchGrey(imgName):
    screen = pyautogui.screenshot('screenshot.png')
    print(screen)
    found = 'false'
    while(found != 'true'):
        try:
            pyautogui.moveTo(imgName)
            print(pag.position())
            found = 'true'
            pag.alert(text='найдено', title='Ура', button='OK')
        except TypeError:
            if (found == 'false'):
                scrollDown()



# Создадим функцию поиска подключений(синих)
def newConnectOne():
    try:
        pag.moveTo(vars.green_47)
        if(vars.green_47):
            scrollDown()
            newConnect(3)
        else:
            return 'false'
    except:
        pag.moveTo(vars.yellow_47)
        if (vars.yellow_47):
            scrollDown()
            newConnect(3)
        else:
            return 'false'


def neConnectionTwo():
    try:
        pag.moveTo(vars.green_83)
        if(vars.green_83):
            scrollDown()
            newConnect(3)
        else:
            return 'false'
    except:
        pag.moveTo(vars.yellow_83)
        if (vars.yellow_83):
            scrollDown()
            newConnect(3)
        else:
            return 'false'
def newConnect(attempt):
    screen = pyautogui.screenshot('screenshot.png')
    print(screen)
    blueClick = 0
    #found = 'false'
    noneFound = 0
    while (blueClick != 2):
            try:
                pyautogui.moveTo(vars.blue_part)
                posBlue = pag.position()
                if (vars.blue_part):
                    pag.doubleClick(posBlue.x, posBlue.y)
                    #found = 'true'
                    blueClick = blueClick + 1
                    print('Найдено')
                    #print(found)
                    print(blueClick)
                    #pag.alert(text='найдено', title='Ура', button='OK')
            except:
                uploadConnect(1)
                print('Не найдено')
                noneFound = noneFound + 1
                if(noneFound == attempt):
                    answer = pag.confirm(text='Не найдено более 2 раз', title='Продолжить?', buttons=['OK', 'Cancel'])
                    if(answer == 'Cancel'):
                        break
                    elif(answer == 'OK'):
                        scrollDown()
    if(blueClick == 2):
        return 'true'
    else:
        return 'false'

# def newConnect():
#     screen = pyautogui.screenshot('screenshot2.png')
#     print(screen)
#     found = 'false'
#     z = 0
#     while (found != 'true'):
#         try:
#             uploadConnect(0.5)
#             pyautogui.moveTo(vars.blue_part)
#             print(pag.position())
#             found = 'true'
#             z = z + 1
#             # pag.alert(text='найдено', title='Ура', button='OK')
#
#             return 'true'
#
#         except TypeError:
#             if (found == 'false'):
#                 i = 0
#                 while(i < 2):
#                     uploadConnect(3)
#                     i = i + 1
#                     if(found == 'true'):
#                         break
#                     if(i == 2):
#                         scrollDown()



# Поиск серых


# Функция пролистывания вверх
def scrollUp():
    screen = pyautogui.screenshot('screenshot.png')
    #print(screen)
    try:
        pyautogui.moveTo(vars.up_scroll)
        print(pag.position())
        pos_Up = pag.position()
        i = 0
        pag.click(pos_Up.x, pos_Up.y, 12, 2, 'left')


    except TypeError:
        pag.alert(text='Не найдено', title='Увы', button='OK')

# Функция пролистывания вниз
def scrollDown():
    screen = pyautogui.screenshot('screenshot.png')
    # print(screen)
    try:
        pyautogui.moveTo(vars.down_scroll)
        print(pag.position())
        pos_Down = pag.position()
        i = 0
        pag.click(pos_Down.x, pos_Down.y, 20*5, 0.1, 'left')
        pag.moveTo(pos_Down.x - 20, pos_Down.y)
    except TypeError:
        pag.alert(text='Не найдено', title='Увы', button='OK')


# Функция обновления подключений
def uploadConnect(t_sleep):
    pyautogui.moveTo(vars.upload)
    posUpload = pag.position()
    pag.click(posUpload.x, posUpload.y)
    pag.sleep(t_sleep)


def clkTwo():
    newPos = pag.position()
    pag.doubleClick(newPos.x, newPos.y)



# Простая функция НАЙТИ
def findBlock(img):
    screen = pyautogui.screenshot('screenshot.png')
    print(screen)
    pyautogui.moveTo(img)


# переход во входы

def entrancesF():
    screen = pyautogui.screenshot('screenshot.png')
    print(screen)
    pyautogui.moveTo(vars.entrances)
    posEntry = pag.position()
    pag.click(posEntry.x, posEntry.y)


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

#findBlock(vars.entry_up_down)
#  Ползём вниз
def entryDown():

    screen = pyautogui.screenshot('screenshot.png')
    pyautogui.moveTo(vars.down_scroll)

    posDown = pag.position()

    pag.moveTo(posDown.x - 20, posDown.y + 20)
    # screen = pyautogui.screenshot('screenshot.png')
    try:
        pyautogui.moveTo(vars.entry_up_down)
    except:
        pyautogui.moveTo(vars.entry_up_downMin)

    pag.sleep(0.3)

    pag.mouseDown(button='left', x=posDown.x, y=posDown.y)
    pag.sleep(1)
    pag.mouseUp()
    # pag.mouseUp(button='left', x = posDown.x, y = posDown.y)

#  Вводим 1
def entryDown1000():
    thousand = 0
    while (thousand != 2):
        try:
            screen = pyautogui.screenshot('screenshot.png')
            pag.sleep(0.2)
            pag.moveTo(vars.text_1000)
            posThousand = pag.position()
            if (vars.text_1000):
                pag.sleep(0.2)
                pag.doubleClick(posThousand.x, posThousand.y)
                # pag.sleep(0.2)
                pag.typewrite('1')
                # pag.sleep(0.1)
                pag.click(posThousand.x, posThousand.y + 20)
                thousand = thousand + 1
        except:
            print('No')

#  Переходим к тиу устройств и сохраняем
def typeAndSave():
    screen = pyautogui.screenshot('screenshot.png')
    pag.moveTo(vars.text_type)
    posType = pag.position()
    pag.click(posType.x, posType.y)
    screen = pyautogui.screenshot('screenshot.png')
    pag.sleep(0.1)
    pag.moveTo(vars.recording)
    pag.click(pag.position())

#entancesF_Two()
# entryDown()
def eD():
    screen = pyautogui.screenshot('screenshot.png')
    pyautogui.moveTo(vars.down_scroll)
    posDown = pag.position()
    pag.moveTo(posDown.x -20, posDown.y + 20)
    screen = pyautogui.screenshot('screenshot.png')
    pyautogui.moveTo(vars.entry_up_down)
    pag.sleep(0.3)
    #
    # pag.mouseDown(button='left', x = posDown.x, y = posDown.y)
    # pag.sleep(1)
    # pag.mouseUp()
    #pag.mouseUp(button='left', x = posDown.x, y = posDown.y)
