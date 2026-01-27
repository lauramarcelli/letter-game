#1. El objetivo consiste en desarrollar el juego interactivo “adivina la palabra”.
#2. El funcionamiento esperado es el siguiente:
#3. Al ejecutar el programa se mostrará por pantalla una palabra oculta usando tantos guiones como letras contiene
#la palabra a adivinar(la palabra a adivinar será elegida por el programa usando el módulo de Python random), la
#cantidad de vidas con las que cuenta el jugador y las cantidad de letras incorrectas que va ingresando.
#4. Cuando el jugador ingresa una letra es necesario que se valide el dato (que sea una letra). Luego de validar la
#letra ingresada se corrobora si la letra ingresada pertenece a alguna de las letras de la palabra a adivinar.
#5. Cada vez que el jugador ingrese una letra que NO pertenece a la palabra a adivinar se restará una vida.
#6. El juego finaliza cuando el jugador queda sin vidas, cuando adivina todas las letras de la palabra o cuando
#selecciona no jugar más. Para todos los casos se debe mostrar un mensaje indicando si ganó la partida o si perdió.

import random

words = ["python", "java", "c++", "javascript", "ruby"]
word = random.choice(words)
lives = 6
wrong_letters = []
guess_word = ["_" for _ in word]


while True:
    