from datetime import datetime
from tkinter import messagebox
import tkinter as tk

class ValorNegativoError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass

class ContaCorrente:
    def __init__(self, nome:str, limite:float):
        self.__nome = nome
        self.__data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__limite = limite
        self.__saldo = 0.0
        
    def depositar(self, valor:float):
        if valor < 0:
            raise ValorNegativoError("Depósito não pode ser negativo.")
        self.__saldo += valor

    def sacar(self, valor:float):
        if valor < 0:
            raise ValorNegativoError("Saque não pode ser negativo.")
        if valor > self.__saldo + self.__limite:
            raise SaldoInsuficienteError("Saldo insuficiente para saque.")
        self.__saldo -= valor

    def __str__(self):
        return (f"Nome: {self.__nome}\n"
                f"Data de Criação: {self.__data_criacao}\n"
                f"Saldo: R$ {self.__saldo:.2f}\n"
                f"Limite: R$ {self.__limite:.2f}\n")
    

# Interface gráfica
class InterfaceContaCorrente:
    def __init__(self, master):
        self.master = master
        master.title("Conta Corrente")
        master.geometry("400x250")
        master.resizable(False, False)

        self.conta = None

        # a) Entradas
        tk.Label(master, text="Nome:").grid(row=0, column=0, sticky="w")
        self.entry_nome = tk.Entry(master)
        self.entry_nome.grid(row=0, column=1, sticky="we")

        tk.Label(master, text="Limite:").grid(row=1, column=0, sticky="w")
        self.entry_limite = tk.Entry(master)
        self.entry_limite.grid(row=1, column=1, sticky="we")

        # b) Botão Criar
        self.btn_criar = tk.Button(master, text="Criar", command=self.criar_conta)
        self.btn_criar.grid(row=2, column=0, columnspan=2, pady=5)

        # c) Label para informações da conta
        self.lbl_info_conta = tk.Label(master, text="", justify="left")
        self.lbl_info_conta.grid(row=3, column=0, columnspan=2, sticky="w")

        # d) Entrada para depósito/saque
        tk.Label(master, text="Valor:").grid(row=4, column=0, sticky="w")
        self.entry_valor = tk.Entry(master)
        self.entry_valor.grid(row=4, column=1, sticky="we")

        # e) Botões de depósito e saque
        self.btn_depositar = tk.Button(master, text="Depositar", command=self.depositar)
        self.btn_depositar.grid(row=5, column=0, pady=5)

        self.btn_sacar = tk.Button(master, text="Sacar", command=self.sacar)
        self.btn_sacar.grid(row=5, column=1, pady=5)

    def criar_conta(self):
        nome = self.entry_nome.get()
        try:
            limite = float(self.entry_limite.get())
            if not nome:
                raise ValueError("O nome não pode estar vazio.")
            self.conta = ContaCorrente(nome, limite)
            self.lbl_info_conta.config(text=str(self.conta))
        except ValueError as e:
            messagebox.showerror("Erro", f"Entrada inválida: {e}")

    def depositar(self):
        if self.conta is None:
            messagebox.showerror("Erro", "Crie uma conta primeiro.")
            return
        try:
            valor = float(self.entry_valor.get())
            self.conta.depositar(valor)
            self.lbl_info_conta.config(text=str(self.conta))
        except (ValueError, ValorNegativoError) as e:
            messagebox.showerror("Erro", str(e))

    def sacar(self):
        if self.conta is None:
            messagebox.showerror("Erro", "Crie uma conta primeiro.")
            return
        try:
            valor = float(self.entry_valor.get())
            self.conta.sacar(valor)
            self.lbl_info_conta.config(text=str(self.conta))
        except (ValueError, ValorNegativoError, SaldoInsuficienteError) as e:
            messagebox.showerror("Erro", str(e))


# Execução da interface
root = tk.Tk()
app = InterfaceContaCorrente(root)
root.mainloop()