import tkinter as tk
from tkinter import messagebox

def calcul_modulo():
    try:
        a = int(entry_a.get())
        k = int(entry_k.get())
        if k == 0:
            messagebox.showerror("Erreur", "k ne peut pas être nul.")
            return
        result_label.config(text=f"{a} mod {k} = {a % k}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer uniquement des entiers.")

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calcul de a mod k")

# Champ a
tk.Label(fenetre, text="Entier a :").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(fenetre)
entry_a.grid(row=0, column=1, padx=5, pady=5)

# Champ k
tk.Label(fenetre, text="Entier k :").grid(row=1, column=0, padx=5, pady=5)
entry_k = tk.Entry(fenetre)
entry_k.grid(row=1, column=1, padx=5, pady=5)

# Bouton calcul
calcul_button = tk.Button(fenetre, text="Calculer a mod k", command=calcul_modulo)
calcul_button.grid(row=2, column=0, columnspan=2, pady=10)

# Résultat
result_label = tk.Label(fenetre, text="", font=("Arial", 12), fg="blue")
result_label.grid(row=3, column=0, columnspan=2)

# Lancement de l'application
fenetre.mainloop()
