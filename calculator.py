from tkinter import *

expression = "" 
def appuyer(touche):
    global expression
    if touche == "=":
        calculer()
        return
    
    expression += str(touche)
    equation.set(expression)

def calculer(): 
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:    
        equation.set("erreur")
        expression = ""

def effacer():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__": 
    gui = Tk()
    for i in range(4):
        gui.grid_columnconfigure(i, weight=1)

    gui.configure(background="#101419") 
    gui.title("Calculatrice")
    gui.geometry("235x385") 

    equation = StringVar()

    resultat = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, 
                 height=2, font=("Arial", 20), anchor="e")
    resultat.grid(row=0, column=0, columnspan=4, sticky="nsew")

    boutons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "/", "="]

    ligne = 1
    colonne = 0

    for bouton in boutons:
        b = Label(gui, text=str(bouton), bg="#476C98", fg="#FFF", height=4, width=6)
        b.bind("<Button-1>", lambda e, b=bouton: appuyer(b))
        b.grid(row=ligne, column=colonne, sticky="nsew", padx=1, pady=1)
        colonne += 1
        if colonne == 4:
            colonne = 0
            ligne += 1

    
    b_clear = Label(gui, text="Effacer", bg="#476C98", fg="#FFF", height=4, width=26)
    b_clear.bind("<Button-1>", lambda e: effacer())
    b_clear.grid(row=ligne, column=0, columnspan=4)
    
    gui.mainloop()