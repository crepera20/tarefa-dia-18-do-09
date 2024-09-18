import tkinter as tk
from tkinter import messagebox
import os
from cidades_model import Cidade  # Certifique-se de que você tenha esse modelo

class CidadesApp:
    def __init__(self, root):
        self.cidade = Cidade()

        self.root = root
        self.root.title("Cadastro de Cidades")
        self.root.state("zoomed")

        # Frame para centralizar os widgets
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Widgets
        self.lblIdCidade = tk.Label(self.frame, text="ID da Cidade:", font=("Arial", 18))
        self.lblIdCidade.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txtIdCidade = tk.Entry(self.frame, font=("Arial", 18))
        self.txtIdCidade.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscar = tk.Button(self.frame, text="Buscar", command=self.buscar_cidade, font=("Arial", 18))
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=10)

        self.lblNome = tk.Label(self.frame, text="Nome:", font=("Arial", 18))
        self.lblNome.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txtNome = tk.Entry(self.frame, font=("Arial", 18))
        self.txtNome.grid(row=1, column=1, padx=10, pady=10)

        # Adicione mais campos conforme necessário...

        # Botões
        self.btnInserir = tk.Button(self.frame, text="Inserir", command=self.inserir_cidade, font=("Arial", 18))
        self.btnInserir.grid(row=6, column=0, padx=10, pady=10)

        self.btnAlterar = tk.Button(self.frame, text="Alterar", command=self.alterar_cidade, font=("Arial", 18))
        self.btnAlterar.grid(row=6, column=1, padx=10, pady=10)

        self.btnExcluir = tk.Button(self.frame, text="Excluir", command=self.excluir_cidade, font=("Arial", 18))
        self.btnExcluir.grid(row=6, column=2, padx=10, pady=10)

        # Botão de Sair
        self.btnSair = tk.Button(self.frame, text="Sair", command=self.sair, font=("Arial", 18))
        self.btnSair.grid(row=7, column=0, columnspan=3, pady=20)

    def buscar_cidade(self):
        # Implemente a lógica de busca para a cidade
        pass

    def inserir_cidade(self):
        # Implemente a lógica para inserir uma cidade
        pass

    def alterar_cidade(self):
        # Implemente a lógica para alterar uma cidade
        pass

    def excluir_cidade(self):
        # Implemente a lógica para excluir uma cidade
        pass

    def sair(self):
        self.root.destroy()
        os.system('python Rotas.py')  # Retorna para Rotas.py

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = CidadesApp(root)
    root.mainloop()
