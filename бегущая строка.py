import os
import time

d1 = 1/6 # задержка 1

print("Чё написать?:",end=' ')
text = input()
if len(text) == 0:
    print('>> ты меня тролишь?')
    text = ('УЧИСЬ ПИСАТЬ, ЧМОШНИК')

print("Ширина поля?:", end=' ')
w = input ()
if len(w) > 0:
    w = int(w)
    if w > 80:
        w = 80
    if w < 1:
        print('>> Пожалуй поставлю 80')
        w = 80
else:
    print('>> установлено на 80')
    w = 80

text = text + ' '*4
if len(text) < w:
    text = text + ' '*(w - len(text))
l = len(text)+1

print ("Задержка в конце? (секунд):", end=' ')
d2 = input()
if len(d2) == 0:
    d2 = 0
else:
    if d2.find(',') != -1:
        d2=d2[:d2.find(',')]+'.'+d2[d2.find(',')+1:]
    d2 = float(d2)
if d2 <= 0:
    d2 = 0

while True:
    for x in range(0,l):
        os.system('cls')
        print ((text[x:]+text[:x])[:w])
        time.sleep(d1)
    time.sleep(d2)