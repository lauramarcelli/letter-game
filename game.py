import tkinter as tk
import random

words = ["sol", "luna", "estrella", "cometa", "planeta", "agua", "aire", "tierra", "fuego", "nieve", "arbol", "flor", "fruto"
"arbusto", "hoja", "piedras", "montañas", "rios", "mar"]
word = random.choice(words)
wrong_letters = []
guess_word = ["_" for _ in word]
lives = 6

def play():
    global lives
    
    if lives > 0 and "_" in guess_word:

        
        guess = entry_guess.get().lower()
        entry_guess.delete(0, tk.END)

        if len(guess) !=1 or not guess.isalpha():
            label_wrong.config(text="Error: Ingrese una sola letra ")
            return

        if guess in guess_word or guess in wrong_letters:
            label_wrong.config(text="Ya ingresaste esa letra")
            return
        
        if guess in word:
            for l in range(len(word)):
                if word[l] == guess:
                    guess_word[l] = guess
            label_wrong.config(text="Bien hecho!")
        else:
            lives -= 1
            wrong_letters.append(guess)
            label_wrong.config(text="Letra incorrecta")

        label_word.config(text=f"Palabra: {' '.join(guess_word)}")
        label_lives.config(text=f"Vidas restantes: {lives}")
        label_wrong.config(text=f"Letras incorectas: {', '.join(wrong_letters)}"
        if wrong_letters else "Incorrectas: ")

        if "_" not in guess_word:
            label_wrong.config(text="🥳Felicidades, adivinaste la palabra🎊")

        if lives == 0:
            label_wrong.config(text="🥲Lo siento, perdiste")
            label_word.config(text=f"La palabra era: {word}")
         

#ventana
root = tk.Tk()

root.title("Adivina la palabra - Versión: Naturaleza")
root.geometry("500x400")

main_frame = tk.Frame(root)
main_frame.pack(expand=True)

#labels
label_word = tk.Label(main_frame, text="Palabra: _ _ _ _ _")
label_word.pack()
label_word.config(font=("Arial", 16))
label_word.config(fg="blue")
label_word.pack(padx=10, pady=10)

label_lives = tk.Label(main_frame, text="Vidas: 6")
label_lives.pack()
label_lives.config(font=("Arial", 16))
label_lives.config(fg="blue")
label_lives.pack(padx=10, pady=10)

label_wrong = tk.Label(main_frame, text="Incorrectas: ")
label_wrong.pack()
label_wrong.config(font=("Arial", 16))
label_wrong.config(fg="blue")
label_wrong.pack(padx=10, pady=10)

#entrada
entry_guess = tk.Entry(main_frame)
entry_guess.pack()
entry_guess.config(font=("Arial", 16))
entry_guess.config(fg="blue")
entry_guess.pack(padx=10, pady=10)

#boton
button_play = tk.Button(main_frame, text="jugar", command=play)
button_play.pack()
button_play.config(font=("Arial", 16))
button_play.config(fg="blue")
button_play.pack(padx=10, pady=10)        

root.mainloop()