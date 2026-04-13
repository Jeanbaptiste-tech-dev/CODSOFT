import random
import tkinter as tk

def jouer(choix_utilisateur):
    options = ['pierre', 'papier', 'ciseaux']
    choix_ordi = random.choice(options)
    
    lbl_choix_joueur.config(text=choix_utilisateur.capitalize())
    lbl_choix_ordi.config(text=choix_ordi.capitalize())
    
    if choix_utilisateur == choix_ordi:
        resultat = "Égalité !"
        couleur = "#f0ad4e" # Orange
    elif (choix_utilisateur == "pierre" and choix_ordi == "ciseaux") or \
         (choix_utilisateur == "papier" and choix_ordi == "pierre") or \
         (choix_utilisateur == "ciseaux" and choix_ordi == "papier"):
        resultat = "C'est gagné !"
        couleur = "#5cb85c" # Vert
    else:
        resultat = "C'est perdu !"
        couleur = "#d9534f" # Rouge
    
    lbl_resultat.config(text=resultat, fg=couleur)

def reset():
    lbl_choix_joueur.config(text="")
    lbl_choix_ordi.config(text="")
    lbl_resultat.config(text="Faites votre choix", fg="black")

root = tk.Tk()
root.title("CodeSoft - Rock Paper Scissors")
root.geometry("400x500")
root.configure(bg="#f8f9fa")

tk.Label(root, text="Rock Paper Scissor", font=("Arial", 24, "bold"), fg="#337ab7", bg="#f8f9fa").pack(pady=20)

frame_match = tk.Frame(root, bg="#f8f9fa")
frame_match.pack(pady=10)

tk.Label(frame_match, text="Joueur", font=("Arial", 12), bg="#f8f9fa").grid(row=0, column=0, padx=30)
tk.Label(frame_match, text="Ordi", font=("Arial", 12), bg="#f8f9fa").grid(row=0, column=2, padx=30)

lbl_choix_joueur = tk.Label(frame_match, text="", font=("Arial", 14, "bold"), bg="#f8f9fa", fg="#555")
lbl_choix_joueur.grid(row=1, column=0)
tk.Label(frame_match, text="VS", font=("Arial", 12, "italic"), bg="#f8f9fa", fg="gray").grid(row=1, column=1)
lbl_choix_ordi = tk.Label(frame_match, text="", font=("Arial", 14, "bold"), bg="#f8f9fa", fg="#555")
lbl_choix_ordi.grid(row=1, column=2)

frame_res = tk.Frame(root, bg="black", bd=1)
frame_res.pack(pady=30)
lbl_resultat = tk.Label(frame_res, text="Faites votre choix", font=("Arial", 18, "bold"), 
                        width=15, height=2, bg="white")
lbl_resultat.pack(padx=2, pady=2)

frame_boutons = tk.Frame(root, bg="#f8f9fa")
frame_boutons.pack(pady=20)

tk.Button(frame_boutons, text="Pierre", width=10, command=lambda: jouer("pierre")).grid(row=0, column=0, padx=5)
tk.Button(frame_boutons, text="Papier", width=10, command=lambda: jouer("papier")).grid(row=0, column=1, padx=5)
tk.Button(frame_boutons, text="Ciseaux", width=10, command=lambda: jouer("ciseaux")).grid(row=0, column=2, padx=5)

tk.Button(root, text="Reset", width=10, bg="#6c757d", fg="white", command=reset).pack(pady=10)

root.mainloop()