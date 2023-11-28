#classe carros: id, modelo, ano, marca, cor, qtdporta
class Carro:
    def __init__(self, id, modelo, ano, marca, cor, qtdporta):
        self._id = id
        self._modelo = modelo
        self._ano = ano
        self._marca = marca
        self._cor = cor
        self._qtdporta = qtdporta