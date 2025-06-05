class Cliente:
    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def to_dict(self):
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'endereco': self.endereco,
            'telefone': self.telefone
        }
    