import tkinter as tk
from tkinter import messagebox
import os
from usuarios_model import Usuario  # Certifique-se de que você tenha esse modelo

class UsuariosApp:
    def __init__(self, root):
        self.usuario = Usuario()

        self.root = root
        self.root.title("Cadastro de Usuários")
        self.root.state("zoomed")

        # Frame para centralizar os widgets
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Widgets
        self.lblIdUsuario = tk.Label(self.frame, text="ID do Usuário:", font=("Arial", 18))
        self.lblIdUsuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txtIdUsuario = tk.Entry(self.frame, font=("Arial", 18))
        self.txtIdUsuario.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscar = tk.Button(self.frame, text="Buscar", command=self.buscar_usuario, font=("Arial", 18))
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=10)

        self.lblNome = tk.Label(self.frame, text="Nome:", font=("Arial", 18))
        self.lblNome.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txtNome = tk.Entry(self.frame, font=("Arial", 18))
        self.txtNome.grid(row=1, column=1, padx=10, pady=10)

        # Adicione mais campos conforme necessário...

        # Botões
        self.btnInserir = tk.Button(self.frame, text="Inserir", command=self.inserir_usuario, font=("Arial", 18))
        self.btnInserir.grid(row=6, column=0, padx=10, pady=10)

        self.btnAlterar = tk.Button(self.frame, text="Alterar", command=self.alterar_usuario, font=("Arial", 18))
        self.btnAlterar.grid(row=6, column=1, padx=10, pady=10)

        self.btnExcluir = tk.Button(self.frame, text="Excluir", command=self.excluir_usuario, font=("Arial", 18))
        self.btnExcluir.grid(row=6, column=2, padx=10, pady=10)

        # Botão de Sair
        self.btnSair = tk.Button(self.frame, text="Sair", command=self.sair, font=("Arial", 18))
        self.btnSair.grid(row=7, column=0, columnspan=3, pady=20)

    def buscar_usuario(self):
        # Implemente a lógica de busca para o usuário
        pass

    def inserir_usuario(self):
        # Implemente a lógica para inserir um usuário
        pass

    def alterar_usuario(self):
        # Implemente a lógica para alterar um usuário
        pass

    def excluir_usuario(self):
        # Implemente a lógica para excluir um usuário
        pass

    def sair(self):
        self.root.destroy()
        os.system('python Rotas.py')  # Retorna para Rotas.py

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = UsuariosApp(root)
    root.mainloop()
