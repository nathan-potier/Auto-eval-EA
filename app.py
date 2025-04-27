import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import sys
import os
from functools import partial

class ProgramLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Sélection de Programme")
        self.root.geometry("700x500")
        self.root.configure(bg="#e6e6e6")
        
        # Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TFrame', background='#f9f9f9')
        style.configure('TLabel', background='#f9f9f9', font=('Segoe UI', 10))
        style.configure('TButton', font=('Segoe UI', 10), padding=6)
        style.configure('Header.TLabel', font=('Segoe UI', 14, 'bold'))
        style.map("TButton",
                  background=[('active', '#d9d9d9')],
                  relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

        # Header
        header_frame = ttk.Frame(root, padding=10, relief="ridge")
        header_frame.pack(pady=10, padx=10, fill=tk.X)
        ttk.Label(header_frame, text="Sélectionnez un programme à exécuter", style='Header.TLabel').pack()

        # Main content
        main_frame = ttk.Frame(root, padding=10, relief="ridge")
        main_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Program selection
        self.programs = {
            "ABR Chemins": {
                "description": "Vérifie si une suite donnée peut représenter un chemin valide dans un ABR",
                "input_type": "text",
                "default_input": """806 → 249 → 528 → 666 → 555 → 546 → 549 → 541
745 → 108 → 214 → 557 → 479 → 449 → 441 → 453
563 → 940 → 984 → 960 → 970 → 976 → 972 → 971
920 → 368 → 908 → 447 → 383 → 412 → 402 → 405
466 → 286 → 310 → 335 → 334 → 322 → 325 → 319
112 → 136 → 120 → 130 → 135 → 133 → 132 → 131
203 → 265 → 465 → 793 → 780 → 564 → 559 → 572"""
            },
            "Arbre Binaire": {
                "description": "Génère et visualise un arbre binaire à partir d'une liste de valeurs",
                "input_type": "list",
                "default_input": [608, 849, 418, 321, 517, 697, 802, 212, 535, 924, 269, 357, 754, 152]
            },
            "QuickSort Tree": {
                "description": "Construit l'arbre de décision du tri rapide pour un tableau donné",
                "input_type": "list",
                "default_input": [491, 325, 861, 729, 378, 627, 811, 271, 690, 443, 910, 171, 143, 539]
            },
            "Tri Rapide en Place": {
                "description": "Effectue un tri rapide en place avec affichage des swaps",
                "input_type": "list",
                "default_input": [77, 61, 85, 29, 36, 94, 42, 18, 53]
            },
            "Insertions Successives": {
                "description": "Construit un ABR par insertions successives et le visualise",
                "input_type": "list",
                "default_input": [652, 459, 621, 543, 785, 938, 731, 879, 206, 120, 496, 340, 253, 385]
            },
            "Sélection Rapide Stable": {
                "description": "Effectue une sélection rapide stable et affiche la séquence des pivots",
                "input_type": "list",
                "default_input": [986, 371, 773, 508, 393, 922, 522, 647, 498, 423],
                "extra_input": {"k": 2}
            }
        }

        # Program listbox
        listbox_frame = ttk.Frame(main_frame)
        listbox_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        self.program_listbox = tk.Listbox(listbox_frame, height=12, font=('Segoe UI', 10), bd=2, relief="groove", selectbackground="#cce6ff")
        self.program_listbox.pack(side=tk.LEFT, fill=tk.Y)
        
        for program in self.programs.keys():
            self.program_listbox.insert(tk.END, program)

        self.program_listbox.bind('<<ListboxSelect>>', self.on_program_select)
        self.program_listbox.selection_set(0)

        # Program details
        self.details_frame = ttk.Frame(main_frame)
        self.details_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.description_label = ttk.Label(self.details_frame, text="", wraplength=400, anchor=tk.W, justify=tk.LEFT)
        self.description_label.pack(pady=(0, 10), anchor=tk.W)

        self.input_frame = ttk.Frame(self.details_frame)
        self.input_frame.pack(fill=tk.X, pady=5)

        self.extra_input_frame = ttk.Frame(self.details_frame)

        # Buttons
        button_frame = ttk.Frame(root, padding=10, relief="ridge")
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Exécuter", command=self.run_program).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Quitter", command=root.quit).pack(side=tk.LEFT, padx=10)

        # Initialize with first program
        self.current_program = list(self.programs.keys())[0]
        self.update_program_details()

    def on_program_select(self, event):
        selection = event.widget.curselection()
        if selection:
            self.current_program = event.widget.get(selection[0])
            self.update_program_details()

    def update_program_details(self):
        program_info = self.programs[self.current_program]
        self.description_label.config(text=program_info["description"])

        # Clear previous input widgets
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        
        for widget in self.extra_input_frame.winfo_children():
            widget.destroy()

        if program_info["input_type"] == "text":
            ttk.Label(self.input_frame, text="Entrez les suites (une par ligne):").pack(anchor=tk.W)
            self.input_text = tk.Text(self.input_frame, height=10, width=50, bd=2, relief="groove", font=('Segoe UI', 10))
            self.input_text.pack(fill=tk.BOTH, expand=True, pady=5)
            self.input_text.insert(tk.END, program_info["default_input"])
        elif program_info["input_type"] == "list":
            ttk.Label(self.input_frame, text="Entrez les valeurs (séparées par des virgules):").pack(anchor=tk.W)
            self.input_entry = ttk.Entry(self.input_frame, width=50)
            self.input_entry.pack(fill=tk.X, pady=5)
            self.input_entry.insert(0, ", ".join(map(str, program_info["default_input"])))

        if "extra_input" in program_info:
            self.extra_input_frame.pack(fill=tk.X, pady=5)
            for key, value in program_info["extra_input"].items():
                ttk.Label(self.extra_input_frame, text=f"{key}:").pack(side=tk.LEFT, padx=(0, 5))
                setattr(self, f"extra_{key}_entry", ttk.Entry(self.extra_input_frame, width=10))
                getattr(self, f"extra_{key}_entry").pack(side=tk.LEFT)
                getattr(self, f"extra_{key}_entry").insert(0, str(value))

    def get_input_values(self):
        program_info = self.programs[self.current_program]

        if program_info["input_type"] == "text":
            return self.input_text.get("1.0", tk.END).strip()
        elif program_info["input_type"] == "list":
            input_str = self.input_entry.get()
            try:
                return [int(x.strip()) for x in input_str.split(",")]
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer une liste valide de nombres entiers séparés par des virgules")
                return None

    def get_extra_input_values(self):
        program_info = self.programs[self.current_program]
        extra_values = {}

        if "extra_input" in program_info:
            for key in program_info["extra_input"].keys():
                entry = getattr(self, f"extra_{key}_entry")
                try:
                    extra_values[key] = int(entry.get())
                except ValueError:
                    messagebox.showerror("Erreur", f"Veuillez entrer une valeur valide pour {key}")
                    return None

        return extra_values

    def run_program(self):
        input_values = self.get_input_values()
        if input_values is None:
            return
        
        extra_values = self.get_extra_input_values()
        if extra_values is None:
            return

        temp_file = "temp_program.py"

        try:
            if self.current_program == "ABR Chemins":
                with open("abr_chemins.py", "r") as f:
                    code = f.read()

                # Traiter les données d'entrée : chaque ligne devient un élément de la liste
                lines = input_values.split("\n")

                # Créer une liste de chaînes de caractères en conservant chaque ligne comme un élément séparé
                temps = [line for line in lines]

                
                formatted_donnees = []
                
                for ligne in temps:
                    nombres = ligne.split(" → ")
                    formatted_donnees.append([int(nombre) for nombre in nombres])

                # Remplacer 'remplacer' dans le code par les données formatées
                modified_code = code.replace('[[806, 249, 528, 666, 555, 546, 549, 541]]', str(formatted_donnees))

                # Sauvegarder le code modifié dans le fichier temporaire
                with open(temp_file, "w") as f:
                    f.write(modified_code)




            elif self.current_program == "Arbre Binaire":
                with open("DeroulerQuickSort.py", "r") as f:
                    code = f.read()
                modified_code = code.replace('[ 491, 325, 861, 729, 378, 627, 811, 271, 690, 443, 910, 171, 143, 539 ]', str(input_values))
                with open(temp_file, "w") as f:
                    f.write(modified_code)

            elif self.current_program == "QuickSort Tree":
                with open("binary_tree.py", "r") as f:
                    code = f.read()
                modified_code = code.replace('[ 608, 849, 418, 321, 517, 697, 802, 212, 535, 924, 269, 357, 754, 152 ]', str(input_values))
                with open(temp_file, "w") as f:
                    f.write(modified_code)

            elif self.current_program == "Tri Rapide en Place":
                with open("exo2Autoteste.py", "r") as f:
                    code = f.read()
                modified_code = code.replace('[77, 61, 85, 29, 36, 94, 42, 18, 53]', str(input_values))
                with open(temp_file, "w") as f:
                    f.write(modified_code)

            elif self.current_program == "Insertions Successives":
                with open("insertions successives.py", "r") as f:
                    code = f.read()
                modified_code = code.replace('[652, 459, 621, 543, 785, 938, 731, 879, 206, 120, 496, 340, 253, 385]', str(input_values))
                with open(temp_file, "w") as f:
                    f.write(modified_code)

            elif self.current_program == "Sélection Rapide Stable":
                with open("sequence_couples.py", "r") as f:
                    code = f.read()
                modified_code = code.replace('[ 986, 371, 773, 508, 393, 922, 522, 647, 498, 423 ]', str(input_values))
                modified_code = modified_code.replace('k = 2', f'k = {extra_values["k"]}')
                with open(temp_file, "w") as f:
                    f.write(modified_code)

            if sys.platform == "win32":
                subprocess.Popen(["start", "cmd", "/k", "python", temp_file], shell=True)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", "-a", "Terminal", temp_file])
            else:
                subprocess.Popen(["x-terminal-emulator", "-e", "python3", temp_file])

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ProgramLauncher(root)
    root.mainloop()
