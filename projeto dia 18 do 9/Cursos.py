import tkinter as tk
from tkinter import messagebox
import os
from cursos_model import Curso  # Certifique-se de que você tenha esse modelo

class CursosApp:
    def __init__(self, root):
        self.curso = Curso()

        self.root = root
        self.root.title("Cadastro de Cursos")
        self.root.state("zoomed")

        # Frame para centralizar os widgets
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Widgets
        self.lblIdCurso = tk.Label(self.frame, text="ID do Curso:", font=("Arial", 18))
        self.lblIdCurso.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txtIdCurso = tk.Entry(self.frame, font=("Arial", 18))
        self.txtIdCurso.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscar = tk.Button(self.frame, text="Buscar", command=self.buscar_curso, font=("Arial", 18))
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=10)

        self.lblNome = tk.Label(self.frame, text="Nome:", font=("Arial", 18))
        self.lblNome.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txtNome = tk.Entry(self.frame, font=("Arial", 18))
        self.txtNome.grid(row=1, column=1, padx=10, pady=10)

        # Adicione mais campos conforme necessário...

        # Botões
        self.btnInserir = tk.Button(self.frame, text="Inserir", command=self.inserir_curso, font=("Arial", 18))
        self.btnInserir.grid(row=6, column=0, padx=10, pady=10)

        self.btnAlterar = tk.Button(self.frame, text="Alterar", command=self.alterar_curso, font=("Arial", 18))
        self.btnAlterar.grid(row=6, column=1, padx=10, pady=10)

        self.btnExcluir = tk.Button(self.frame, text="Excluir", command=self.excluir_curso, font=("Arial", 18))
        self.btnExcluir.grid(row=6, column=2, padx=10, pady=10)

        # Botão de Sair
        self.btnSair = tk.Button(self.frame, text="Sair", command=self.sair, font=("Arial", 18))
        self.btnSair.grid(row=7, column=0, columnspan=3, pady=20)

    def buscar_curso(self):
        # Implemente a lógica de busca para o curso
        pass

    def inserir_curso(self):
        # Implemente a lógica para inserir um curso
        pass

    def alterar_curso(self):
        # Implemente a lógica para alterar um curso
        pass

    def excluir_curso(self):
        # Implemente a lógica para excluir um curso
        pass

    def sair(self):
        self.root.destroy()
        os.system('python Rotas.py')  # Retorna para Rotas.py

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = CursosApp(root)
    root.mainloop()
