class Cadastra_Carro:
    __slots__ = ['_lista_carros']

    def __init__(self):
        self._lista_carros = [] 

    def cadastracarro(self, carro):
        existe = self.busca(carro._cpf)
        if existe is None:
            self._lista_cnh.append(carro)
            return True
        else:
            return False
    
    def busca(self, id):
        for lc in self._lista_pessoas:
            if lc._id == id:
                return lc
        return None
