import winsound as ws

octava = [261, 277, 293, 311, 329, 349, 369, 391, 415, 440, 466, 493]
escala = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in octava:
    if escala[octava.index(i)] == 1:
        print(i)
       # ws.Beep(i, 400)
'''
for i in octava[: : -1]:
    if escala[octava.index(i)] == 1:
        ws.Beep(i, 400)'''