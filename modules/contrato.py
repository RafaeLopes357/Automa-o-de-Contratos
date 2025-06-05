from docx import Document
import os
from os.path import basename, splitext
import gc
from modules.cliente import Cliente
class Contrato:
    def __init__(self, caminho_documento):
        self.caminho_documento = caminho_documento
        self.documento = Document(caminho_documento)
        """
        self.nome_cliente = Cliente.nome
        self.cpf_cliente = Cliente.cpf
        self.endereco_cliente = Cliente.endereco
        self.telefone_cliente = Cliente.telefone
        """
    def inserir_dados_cliente(self, cliente):
        for paragrafo in self.documento.paragraphs:
            placeholder1 = '{nome}'
            placeholder2 = '{cpf}'
            placeholder3 = '{endereço}'
            placeholder4 = '{telefone}'  
            if placeholder1 in paragrafo.text:
                paragrafo.text = paragrafo.text.replace(placeholder1, cliente.nome)
            if placeholder2 in paragrafo.text:
                paragrafo.text = paragrafo.text.replace(placeholder2, cliente.cpf)
            if placeholder3 in paragrafo.text:
                paragrafo.text = paragrafo.text.replace(placeholder3, cliente.endereco)
            if placeholder4 in paragrafo.text:
                paragrafo.text = paragrafo.text.replace(placeholder4, cliente.telefone)
        
        template_dir = os.path.dirname(self.caminho_documento)
        template_name = splitext(basename(self.caminho_documento))[0]
        output_path = os.path.join(template_dir, f"{cliente.nome}_{template_name}.docx")

        # Salvar documento no mesmo diretório do template original
        self.documento.save(output_path)
        gc.collect()