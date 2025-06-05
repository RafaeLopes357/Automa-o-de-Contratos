import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from modules.cliente import Cliente
from modules.contrato import Contrato
class FormularioContrato:
    def __init__(self, master):
        self.master = master
        self.master.title("Automação de Contratos")

        # Layout da interface
        self.criar_widgets()

    def criar_widgets(self):
        # Campos de entrada
        tk.Label(self.master, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nome = tk.Entry(self.master)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.master, text="CPF:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_cpf = tk.Entry(self.master)
        self.entry_cpf.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Endereço:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_endereco = tk.Entry(self.master)
        self.entry_endereco.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Telefone:").grid(row=3, column=0, padx=10, pady=10)
        self.entry_telefone = tk.Entry(self.master)
        self.entry_telefone.grid(row=3, column=1, padx=10, pady=10)

        # Botão para gerar os contratos
        self.btn_selecionar = tk.Button(self.master, text='Selecionar Contratos', command=self.selecionar_contratos)
        self.btn_selecionar.grid(row=4, column=0, columnspan=2, pady=5)

        self.btn_gerar = tk.Button(self.master, text="Gerar Contrato", command=self.gerar_contrato)
        self.btn_gerar.grid(row=5, column=0, columnspan=2, pady=10)

    def selecionar_contratos(self):
        arquivos = filedialog.askopenfilenames(title='Selecione os contratos', filetypes=[('Documentos Word', 'docx')])
            
        if arquivos:
            self.caminhos_contratos = list(arquivos)
            messagebox.showinfo('Arquivos selecionados',f'{len(self.caminhos_contratos)}arquivos selecionados')
        else:
            self.caminhos_contratos = []
            messagebox.showwarning('Nenhum arquivo', 'Nenhum contrato foi selecionado')
    def gerar_contrato(self):
        # Pegar os dados do cliente
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        endereco = self.entry_endereco.get()
        telefone = self.entry_telefone.get()

        # Verificar se todos os campos foram preenchidos
        if not nome or not cpf or not endereco or not telefone:
            messagebox.showwarning("Campos faltando", "Preencha todos os campos!")
            return
        if not self.caminhos_contratos:
            messagebox.showwarning('Nenhum contrato', 'Selecione pelo menos um contrato')

        cliente = Cliente(nome, cpf, endereco, telefone)
        try:
            for caminho in self.caminhos_contratos:
                contrato = Contrato(caminho)
                contrato.inserir_dados_cliente(cliente)
                messagebox.showinfo("Sucesso", f"Contrato gerado com sucesso para {nome}!")
        except Exception as e:
            messagebox.showwarning('Erro',f'Erro ao gerar comtratos: {str(e)}')
    
    
# Iniciar a interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioContrato(root)
    root.mainloop()