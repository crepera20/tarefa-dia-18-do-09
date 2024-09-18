import tkinter as tk
from tkinter import messagebox
import os
import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Nome do usuário
        password="",         # Senha do root como não tem senha fica em branco
        database="DBescola"  # Nome do banco de dados
    )

class Aluno:
    def __init__(self):
        self.conexao = conectar_banco()  # Usando a função de conexão

    def inserir(self, nome, telefone, email, endereco, idade):
        try:
            cursor = self.conexao.cursor()
            cursor.execute('''
                INSERT INTO TBL_alunos (ALU_nome, ALU_endereco, ALU_email, ALU_telefone, ALU_idade)
                VALUES (%s, %s, %s, %s, %s)  # Use %s para placeholders
            ''', (nome, endereco, email, telefone, idade))
            self.conexao.commit()
            print("Aluno inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir no banco de dados: {e}")

    def alterar(self, ALU_codigo, ALU_nome, ALU_endereco, ALU_email, ALU_telefone, ALU_idade):
        cursor = self.conexao.cursor()
        cursor.execute('''
            UPDATE TBL_alunos SET ALU_nome=%s, ALU_endereco=%s, ALU_email=%s, ALU_telefone=%s, ALU_idade=%s
            WHERE ALU_codigo=%s
        ''', (ALU_nome, ALU_endereco, ALU_email, ALU_telefone, ALU_idade, ALU_codigo))
        self.conexao.commit()

    def excluir(self, ALU_codigo):
        cursor = self.conexao.cursor()
        cursor.execute('DELETE FROM TBL_alunos WHERE ALU_codigo=%s', (ALU_codigo,))
        self.conexao.commit()

    def buscar(self, ALU_codigo):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM TBL_alunos WHERE ALU_codigo=%s', (ALU_codigo,))
        resultado = cursor.fetchone()
        return resultado

class Application:
    def __init__(self, root):
        self.aluno = Aluno()
        self.root = root
        self.root.title("Cadastro de Alunos")
        self.root.state("zoomed")

        # Frame para centralizar os widgets
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Widgets
        self.lblIdAluno = tk.Label(self.frame, text="Código do Aluno:", font=("Arial", 18))
        self.lblIdAluno.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txtIdAluno = tk.Entry(self.frame, font=("Arial", 18))
        self.txtIdAluno.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscar = tk.Button(self.frame, text="Buscar", command=self.buscar_aluno, font=("Arial", 18))
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=10)

        self.lblNome = tk.Label(self.frame, text="Nome:", font=("Arial", 18))
        self.lblNome.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txtNome = tk.Entry(self.frame, font=("Arial", 18))
        self.txtNome.grid(row=1, column=1, padx=10, pady=10)

        self.lblEndereco = tk.Label(self.frame, text="Endereço:", font=("Arial", 18))
        self.lblEndereco.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.txtEndereco = tk.Entry(self.frame, font=("Arial", 18))
        self.txtEndereco.grid(row=2, column=1, padx=10, pady=10)

        self.lblTelefone = tk.Label(self.frame, text="Telefone:", font=("Arial", 18))
        self.lblTelefone.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.txtTelefone = tk.Entry(self.frame, font=("Arial", 18))
        self.txtTelefone.grid(row=3, column=1, padx=10, pady=10)

        self.lblEmail = tk.Label(self.frame, text="E-mail:", font=("Arial", 18))
        self.lblEmail.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.txtEmail = tk.Entry(self.frame, font=("Arial", 18))
        self.txtEmail.grid(row=4, column=1, padx=10, pady=10)

        self.lblIdade = tk.Label(self.frame, text="Idade:", font=("Arial", 18))
        self.lblIdade.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.txtIdade = tk.Entry(self.frame, font=("Arial", 18))
        self.txtIdade.grid(row=5, column=1, padx=10, pady=10)

        # Botões
        self.btnInserir = tk.Button(self.frame, text="Inserir", command=self.inserir_aluno, font=("Arial", 18))
        self.btnInserir.grid(row=6, column=0, padx=10, pady=10)

        self.btnAlterar = tk.Button(self.frame, text="Alterar", command=self.alterar_aluno, font=("Arial", 18))
        self.btnAlterar.grid(row=6, column=1, padx=10, pady=10)

        self.btnExcluir = tk.Button(self.frame, text="Excluir", command=self.excluir_aluno, font=("Arial", 18))
        self.btnExcluir.grid(row=6, column=2, padx=10, pady=10)

        # Botão de sair
        self.btnSair = tk.Button(self.frame, text="Sair", command=self.sair, font=("Arial", 18))
        self.btnSair.grid(row=7, column=0, columnspan=3, pady=20)

        # Bind para detectar o fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def buscar_aluno(self):
        idAluno = self.txtIdAluno.get()
        try:
            idAluno = int(idAluno)
            resultado = self.aluno.buscar(idAluno)
            if resultado:
                self.txtNome.delete(0, tk.END)
                self.txtNome.insert(tk.END, resultado[1])
                self.txtEndereco.delete(0, tk.END)
                self.txtEndereco.insert(tk.END, resultado[2])
                self.txtEmail.delete(0, tk.END)
                self.txtEmail.insert(tk.END, resultado[3])
                self.txtTelefone.delete(0, tk.END)
                self.txtTelefone.insert(tk.END, resultado[4])
                self.txtIdade.delete(0, tk.END)
                self.txtIdade.insert(tk.END, resultado[5])
                messagebox.showinfo("Sucesso", "Busca realizada com sucesso!")
            else:
                messagebox.showerror("Erro", "Aluno não encontrado!")
        except ValueError:
            messagebox.showerror("Erro", "ID do aluno deve ser um número.")

    def inserir_aluno(self):
        ALU_nome = self.txtNome.get()
        ALU_endereco = self.txtEndereco.get()
        ALU_email = self.txtEmail.get()
        ALU_telefone = self.txtTelefone.get()
        ALU_idade = self.txtIdade.get()

        if ALU_nome and ALU_endereco and ALU_email and ALU_telefone and ALU_idade:
            try:
                self.aluno.inserir(ALU_nome, ALU_telefone, ALU_email, ALU_endereco, ALU_idade)
                messagebox.showinfo("Sucesso", "Aluno inserido com sucesso!")
                self.limpar_campos()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao inserir aluno: {e}")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def alterar_aluno(self):
        ALU_codigo = self.txtIdAluno.get()
        ALU_nome = self.txtNome.get()
        ALU_endereco = self.txtEndereco.get()
        ALU_email = self.txtEmail.get()
        ALU_telefone = self.txtTelefone.get()
        ALU_idade = self.txtIdade.get()

        if ALU_codigo and ALU_nome and ALU_endereco and ALU_email and ALU_telefone and ALU_idade:
            try:
                self.aluno.alterar(ALU_codigo, ALU_nome, ALU_endereco, ALU_email, ALU_telefone, ALU_idade)
                messagebox.showinfo("Sucesso", "Aluno alterado com sucesso!")
                self.limpar_campos()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao alterar aluno: {e}")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def excluir_aluno(self):
        idAluno = self.txtIdAluno.get()
        if idAluno:
            try:
                self.aluno.excluir(idAluno)
                messagebox.showinfo("Sucesso", "Aluno excluído com sucesso!")
                self.limpar_campos()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir aluno: {e}")
        else:
            messagebox.showerror("Erro", "Por favor, informe o ID do aluno a ser excluído!")

    def limpar_campos(self):
        self.txtIdAluno.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtEndereco.delete(0, tk.END)
        self.txtEmail.delete(0, tk.END)
        self.txtTelefone.delete(0, tk.END)
        self.txtIdade.delete(0, tk.END)

    def sair(self):
        self.root.quit()

    def on_closing(self):
        if messagebox.askokcancel("Sair", "Deseja sair?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
