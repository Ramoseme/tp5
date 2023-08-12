#ejercicio 2
"""from tp5 import redondear"""
#ejercicio 3
"""import datetime

def mostrar_fecha_y_hora():

    fecha_hora_actual = datetime.datetime.now()
    fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

    print("Fecha y hora actuales:", fecha_hora_formateada)

mostrar_fecha_y_hora()"""

#ejercicio 4
"""import random

def numero_par_azar():
    numeros_pares = list(range(2, 11, 2))
    numero_azar = random.choice(numeros_pares)
    return numero_azar

while True:
    numero_par = numero_par_azar()
    print("Número par al azar entre 2 y 10:", numero_par)

    import time
    time.sleep(1)"""
#ejercicio 5

import random

import time
inicio=time.time()

def bola_magica():
    respuestas = ["Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"]

    while True:
        pregunta = input("Haz tu pregunta a la Bola Mágica (o escribe 'salir' para terminar): ")

        if pregunta.lower() == 'salir':
            print("¡Hasta luego!")
            break

        respuesta_seleccionada = random.choice(respuestas)
        print("Respuesta de la Bola Mágica:", respuesta_seleccionada)

bola_magica()

final=time.time()
delta= final - inicio
print("los segundos de ejecucuion son de: {:.3f}".format(delta))

#ejercicio 6 aplicado en el ejercicio 5