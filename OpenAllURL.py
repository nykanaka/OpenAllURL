from tkinter import *
import time
import webbrowser
import pyperclip

webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))

def getText():
    s = text.get(1.0, END)
    #label['text'] = s
    with open("input.txt", "w") as somefile:
        somefile.write(text.get(1.0, END))
    k = 0
    element = ['com', 'net', 'www', 'ru', 'https', 'http']
    with open("input.txt", "r") as somefile:
        addres = somefile.read()
    for l_url in addres.splitlines():
        for elmnt in element:
            if elmnt in l_url:
                webbrowser.get('Chrome').open(l_url)
                k += 1
                if k == 25:
                    time.sleep(10)
                    k = 0
                break

def pasteText():
    text.insert(END, str(pyperclip.paste()))

def deleteText():
    text.delete(1.0, END)

root = Tk()
root.title("Открытие ссылок")

text = Text(width=70, height=20)
text.pack()

frame = Frame()
frame.pack()

b_get = Button(frame, text="Открыть", command=getText)
b_get.pack(side=LEFT)

b_paste = Button(frame, text="Вставить из буфера обмена", command=pasteText)
b_paste.pack(side=LEFT)

b_delete = Button(frame, text="Удалить", command=deleteText)
b_delete.pack(side=LEFT)

label = Label()
label.pack()

root.mainloop()