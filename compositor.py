import winsound as ws

octavas = [[130, 138, 146, 155, 164, 174, 184, 195, 207, 220, 233, 246], [261, 277, 293, 311, 329, 349, 369, 391, 415, 440, 466, 493], [523, 554, 587, 622, 659, 698, 739, 783, 830, 880, 932, 987], [1046, 1108, 1174, 1244, 1318, 1396, 1479, 1567, 1661, 1760, 1864, 1975]]

tiempos = {"f": 125, "s": 250, "c": 500, "n": 1000, "b": 2000, "r": 4000}

cancion = map(lambda n: n.strip(), input("Escribe la canción: ").split(",")) 

nota = 0
escala = 0
duracion = ""

for tono in cancion: #122n
    if len(tono) == 3:
        nota = int(tono[0]) - 1
        escala = int(tono[1]) - 1
        duracion = tono[2]
    elif len(tono) == 4:
        nota = int(tono[0:2]) - 1
        escala = int(tono[2]) - 1
        duracion = tono[3]
    frecuencia = octavas[escala][nota]
    tiempo = tiempos[duracion]
    ws.Beep(frecuencia, tiempo)