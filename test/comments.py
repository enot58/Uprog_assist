

# Для начала выберем картинки
# screen = pyautogui.screenshot('screenshot.png')
# pag.alert(text='hello', title='Hello', button='OK')
# pag.confirm(text='Вы готовы?', title='Привет', buttons=['OK', 'Cancel'])
# pag.prompt(text='Hello', title='Press message', default='h')
# pag.password(text='hello', title='header', default='none', mask='*')


# if(TypeError):
#     pyautogui.click('blocks/up_down.png')
#Ищем картинку если не выходит пытаемся пролистать
# try:
#     pyautogui.moveTo(greyOne)
#     posOne = pag.position()
#     # Эта функция position() сообщает нам текущее положение мыши на экране:
#     print(posOne)
#
# except TypeError:
#     pyautogui.click('bloks/up_down.png')
#     print(pag.position())






# # Здесь размер приложения
# window.geometry('500x500')
# # Здесь подпись с сеткой
# lbl = Label(window, text="Привет!")
# lbl.grid(column=0, row=0)
#
# # Добавим кнопку
# btn = Button(window, text="Нажми меня", command=clicked)
# btn.grid(column=1, row=1)





# Создаём меню

# menu = Menu(window)
# new_item = Menu(menu, tearoff=0)
#
#
# new_item.add_command(label='Новый')
# menu.add_cascade(label='Файл', menu=new_item, command='lb')
# new_item.add_separator()
# new_item.add_command(label='Редактировать')
#
# window.config(menu=menu)