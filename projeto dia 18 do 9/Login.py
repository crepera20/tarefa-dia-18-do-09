import tkinter as tk
from tkinter import messagebox, PhotoImage
import subprocess
import mysql.connector
import os

# Função para conectar ao banco de dados
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Nome do usuário
        password="",  # senha do root como não tem senha fica em branco
        database="DBescola"  # Nome do banco de dados
    )

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.state("zoomed")  # Aumenta o tamanho da janela para tela cheia

        # Frame para centralizar os widgets
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)  # Expande para ocupar o espaço disponível

        # Carrega e exibi a imagem na parte superior
        self.img = PhotoImage(file="usuario.png")  # caminho da imagem
        self.lblImagem = tk.Label(self.frame, image=self.img)
        self.lblImagem.grid(row=0, column=0, columnspan=2, pady=10)  # Coloca a imagem no topo

        # Label e Entry para usuário
        self.lblUsuario = tk.Label(self.frame, text="Usuário:", font=("Arial", 18))
        self.lblUsuario.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.txtUsuario = tk.Entry(self.frame, font=("Arial", 18))
        self.txtUsuario.grid(row=4, column=1, padx=10, pady=10)

        # Label e Entry para senha
        self.lblSenha = tk.Label(self.frame, text="Senha:", font=("Arial", 18))
        self.lblSenha.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.txtSenha = tk.Entry(self.frame, font=("Arial", 18), show="*")
        self.txtSenha.grid(row=5, column=1, padx=10, pady=10)

        # Botão de Login
        self.btnLogin = tk.Button(self.frame, text="Login", font=("Arial", 18), command=self.realizar_login)
        self.btnLogin.grid(row=6, column=0, columnspan=2, pady=20)

    def realizar_login(self):
        nome_usuario = self.txtUsuario.get()
        senha_usuario = self.txtSenha.get()

        # Conectar ao banco
        db = conectar_banco()
        cursor = db.cursor()

        # Consulta SQL para verificar se o usuário e a senha estão corretos
        query = "SELECT * FROM TBl_usuarios WHERE USU_nome = %s AND USU_senha = %s"
        cursor.execute(query, (nome_usuario, senha_usuario))
        resultado = cursor.fetchone()

        # Verifica se o usuário foi encontrado
        if resultado:
            self.root.destroy()  # Fecha a janela de login
            self.abrir_rotas()   # Abri a página Rotas.py
        else:
            messagebox.showerror("Login", "Usuário não encontrado ou senha incorreta.")

        cursor.close()
        db.close()

    # Função para abrir a página Rotas.py
    def abrir_rotas(self):
        subprocess.Popen(['python', 'Rotas.py'])

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
