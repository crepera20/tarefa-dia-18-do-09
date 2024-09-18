import tkinter as tk
from tkinter import ttk
import subprocess

class RotasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rotas")
        self.root.state("zoomed")  # Abre a janela em tela cheia

        # Título centralizado
        self.lblTitulo = tk.Label(self.root, text="Rotas", font=("Arial", 24), pady=20)
        self.lblTitulo.pack()

        # Frame para centralizar a janela de seleção
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True)

        # Janela de variáveis (ComboBox) para selecionar uma tabela do banco de dados
        self.lblSelecione = tk.Label(self.frame, text="Selecione uma rota:", font=("Arial", 18))
        self.lblSelecione.grid(row=0, column=0, padx=10, pady=10)

        self.opcoes = ["Professores", "Alunos", "Cidades", "Cursos", "Usuários"]
        self.comboRotas = ttk.Combobox(self.frame, values=self.opcoes, font=("Arial", 18), state="readonly")
        self.comboRotas.grid(row=0, column=1, padx=10, pady=10)
        self.comboRotas.bind("<<ComboboxSelected>>", self.selecionar_rota)

        # Botão de Sair
        self.btnSair = tk.Button(self.frame, text="Sair", font=("Arial", 18), command=self.sair)
        self.btnSair.grid(row=1, column=0, columnspan=2, pady=20)

    def selecionar_rota(self, event):
        rota = self.comboRotas.get()
        if rota == "Professores":
            self.abrir_pagina('Professores.py')
        elif rota == "Alunos":
            self.abrir_pagina('Alunos.py')
        elif rota == "Cidades":
            self.abrir_pagina('Cidades.py')
        elif rota == "Cursos":
            self.abrir_pagina('Cursos.py')
        elif rota == "Usuários":
            self.abrir_pagina('Usuarios.py')

    def abrir_pagina(self, pagina):
        subprocess.Popen(['python', pagina])  # Abre a página correspondente
        self.root.destroy()  # Fecha a janela de rotas

    def sair(self):
        self.root.quit()  # Fecha a aplicação

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = RotasApp(root)
    root.mainloop()
