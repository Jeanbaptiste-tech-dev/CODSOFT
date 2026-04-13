import json
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

#Fonctions
data_file = "tache.json"
def sauvegarder_tache():
    taches = List_Box.get(0, tk.END)
    with open(data_file, "w") as f:
        json.dump(taches,f, indent=4)
def charger_tache():
    with open(data_file, 'r') as f:
        try:
            taches= json.load(f)
            for tache in taches:
                List_Box.insert(tk.END, tache)
        except:
            print(None)

def ajouter_tache():
    tache = entrer.get()
    if tache !="":
        List_Box.insert(tk.END, tache)
        sauvegarder_tache()
    else:
        messagebox.showwarning("Warning", "Please Enter a Task")

def supprimer_tache():
    try:
        index=List_Box.curselection()
        List_Box.delete(index)
        sauvegarder_tache()
    except:
        messagebox.showwarning("Warning", "Please select a task")

#Entré de l'utilisateur
entrer=tk.Entry(root, width=30)
entrer.pack(pady=5)

#Buttons

ajouter_task= tk.Button(root, text="ajouter une tache", width=15, command=ajouter_tache)
ajouter_task.pack(pady=5)

supprimer_task=tk.Button(root, text="Supprimer une tache", width=15, command=supprimer_tache)
supprimer_task.pack(pady=5)

List_Box=tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
List_Box.pack(pady=10)

charger_tache()

root.mainloop()