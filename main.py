import sys
import socket
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from telacadastro import Telacadastro
from telalogin import Telalogin
from pessoa import Pessoa

# from servidorlocadrive import ServidorCadastro
# from cadastro import Cadastra_CNH
from PyQt5.QtCore import QDate
from teladeloginefetuado import LoginEfetuado
from telabotaodadospessoais import OP_DadosPessoais
from telaalterardadospessoais import AlterarDP
from telaAluguel import OP_MeuAluguel
from telabotaominhasreservas import OP_MinhasReservas
from telaCNH import OP_CNH
from cnh import CNH
# from cadastracnh import Cadastra_CNH
from cadastrarcarro import Cadastra_Carro
from tela_CarrosDispo import OP_CarDispo
from carros_telaPICAPE import Carros_B
from carros_telaSEDAN import Carros_C
from carros_telaSUV import Carros_A
from telasobrenos import Sobre_Nos
import json


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(700, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QDialog()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()
        self.stack10 = QtWidgets.QMainWindow()
        self.stack11 = QtWidgets.QMainWindow()
        self.stack12 = QtWidgets.QMainWindow()

        self.tela_inicial = Telalogin()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Telacadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_loginefetuado = LoginEfetuado()
        self.tela_loginefetuado.setupUi(self.stack2)

        self.tela_dadospessoais = OP_DadosPessoais()
        self.tela_dadospessoais.setupUi(self.stack3)

        self.tela_alterarDP = AlterarDP()
        self.tela_alterarDP.setupUi(self.stack4)

        self.tela_meualuguel = OP_MeuAluguel()
        self.tela_meualuguel.setupUi(self.stack5)

        self.tela_minhasreservas = OP_MinhasReservas()
        self.tela_minhasreservas.setupUi(self.stack6)

        self.tela_CNH = OP_CNH()
        self.tela_CNH.setupUi(self.stack7)

        self.tela_CarrosDispo = OP_CarDispo()
        self.tela_CarrosDispo.setupUi(self.stack8)

        self.tela_CategoriaA = Carros_A()
        self.tela_CategoriaA.setupUi(self.stack9)

        self.tela_CategoriaB = Carros_B()
        self.tela_CategoriaB.setupUi(self.stack10)

        self.tela_CategoriaC = Carros_C()
        self.tela_CategoriaC.setupUi(self.stack11)

        self.tela_Sobrenos = Sobre_Nos()
        self.tela_Sobrenos.setupUi(self.stack12)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)
        self.QtStack.addWidget(self.stack10)
        self.QtStack.addWidget(self.stack11)
        self.QtStack.addWidget(self.stack12)


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

        self.cad_carros = Cadastra_Carro()


        self.ip = 'localhost'
        self.port = 1600
        self.addr = (self.ip, self.port)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.addr)

        # BOTOES DA TELA INICIAL
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.pushButton_4.clicked.connect(self.verificarLogin)
        self.tela_inicial.pushButton.clicked.connect(self.fecharPrograma)

        # BOTOES DA TELA DE CADASTRO
        self.tela_cadastro.pushButton_2.clicked.connect(self.botaoCadastra)
        self.tela_cadastro.pushButton.clicked.connect(self.abrirTelalogin)

        # BOTOES DA TELA DE LOGIN EFETUADO
        self.tela_loginefetuado.botao_sair.clicked.connect(self.SairSistema)
        # self.tela_loginefetuado.pushButton_2.clicked.connect(self.AbrirTelaCNH)
        self.tela_loginefetuado.pushButton_3.clicked.connect(
            self.abrirTelaCarrosDispo)
        self.tela_loginefetuado.pushButton_4.clicked.connect(
            self.abrirTelaDadosPessoais)
        self.tela_loginefetuado.pushButton_5.clicked.connect(
            self.AbrirTelaMinhasReservas)
        self.tela_loginefetuado.pushButton_6.clicked.connect(
            self.abrirTelaAlugarCarro)
        self.tela_loginefetuado.pushButton.clicked.connect(
            self.AbrirTelaSobrenos)

        # BOTOES DA TELA DE DADOS PESSOAIS
        self.tela_dadospessoais.pushButton.clicked.connect(
            self.abrirTelaloginEfetuado)
        self.tela_dadospessoais.pushButton_2.clicked.connect(
            self.abrirTelaAlterarDP)

        # BOTOES DA TELA DE ALTERAR DADOS PESSOAIS
        # self.tela_alterarDP.pushButton.clicked.connect(self.abrirTelaDadosPessoais)

        # BOTOES DA TELA MEU ALUGUEL
        self.tela_meualuguel.pushButton.clicked.connect(
            self.abrirTelaloginEfetuado)

        # BOTOES DA TELA DE MINHAS RESERVAS
        self.tela_minhasreservas.pushButton_2.clicked.connect(
            self.abrirTelaloginEfetuado)

        # BOTOES DA TELA MINHA CNH
        # self.tela_CNH.pushButton_2.clicked.connect(self.botaoCadastraCNH)
        self.tela_CNH.pushButton.clicked.connect(self.abrirTelaloginEfetuado)

        # BOTOES DA TELA DE CARROS DISPONIVEIS
        self.tela_CarrosDispo.pushButton.clicked.connect(
            self.AbrirTelaCategoriaA)
        self.tela_CarrosDispo.pushButton_2.clicked.connect(
            self.AbrirTelaCategoriaB)
        self.tela_CarrosDispo.pushButton_3.clicked.connect(
            self.AbrirTelaCategoriaC)
        self.tela_CarrosDispo.pushButton_4.clicked.connect(
            self.abrirTelaloginEfetuado)

        # BOTOES DA TELA DE CATEGORIA A
        self.tela_CategoriaA.pushButton.clicked.connect(
            self.abrirTelaCarrosDispo)

        # BOTOES DA TELA DE CATEGORIA B
        self.tela_CategoriaB.pushButton.clicked.connect(
            self.abrirTelaCarrosDispo)

        # BOTOES DA TELA DE CATEGORIA C
        self.tela_CategoriaC.pushButton.clicked.connect(
            self.abrirTelaCarrosDispo)

        # BOTOES TELA SOBRE NOS
        self.tela_Sobrenos.pushButton.clicked.connect(
            self.abrirTelaloginEfetuado)

        self.cpf = ''

    
    def SairSistema(self):
        print('1 sair sistema')
        msg = f'sair;'
        self.client_socket.send(msg.encode())
        print('2 sair sistema')
        

        self.addr = (self.ip, self.port)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.addr)
    
        self.abrirTelalogin()
      
    def botaoCadastra(self):

        nome = self.tela_cadastro.lineEdit.text()
        datanasci = self.tela_cadastro.dateEdit.text()
        cpf = self.tela_cadastro.lineEdit_2.text()
        telefone = self.tela_cadastro.lineEdit_3.text()
        email = self.tela_cadastro.lineEdit_4.text()
        cep = self.tela_cadastro.lineEdit_5.text()
        estado = self.tela_cadastro.lineEdit_6.text()
        cidade = self.tela_cadastro.lineEdit_7.text()
        senha = self.tela_cadastro.lineEdit_9.text()

        preencheu = 0
        if (nome != '' and datanasci != '' and cpf != '' and telefone != '' and email != '' and cep != '' and estado != '' and cidade != '' and senha != ''):
            try:
                msg = f'cadastro;{nome};{cpf};{email};{estado};{telefone};{cep};{cidade};{datanasci};{senha}'
                self.client_socket.send(msg.encode())
                resp = self.client_socket.recv(1024).decode()
                print(resp)

                if resp.lower() == 'conta criada com sucesso!':

                    QMessageBox.information(
                        None, 'LocaDrive', 'Pessoa cadastrada com sucesso!')
                    self.tela_cadastro.lineEdit.setText('')
                    self.tela_cadastro.dateEdit.setDate(QDate.currentDate())
                    self.tela_cadastro.lineEdit_2.setText('')
                    self.tela_cadastro.lineEdit_3.setText('')
                    self.tela_cadastro.lineEdit_4.setText('')
                    self.tela_cadastro.lineEdit_5.setText('')
                    self.tela_cadastro.lineEdit_6.setText('')
                    self.tela_cadastro.lineEdit_7.setText('')
                    self.tela_cadastro.lineEdit_9.setText('')
                    preencheu = 1
                    self.addr = (self.ip, self.port)
                    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.client_socket.connect(self.addr)
                else:
                    QMessageBox.warning(
                        None, 'LocaDrive', 'Erro ao cadastrar pessoa no servidor.')
            except Exception as e:
                print(f"erro: {e}")

            '''else           QMessageBox.warning(None, 'LocaDrive', 'O CPF informado já está cadastrado na base de dados!')'''

        else:
            QMessageBox.warning(None, 'LocaDrive','Todos os valores devem ser preenchidos!')

        if preencheu == 1:
            self.abrirTelalogin()
        else:
            self.abrirTelaCadastro()

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelalogin(self):
        self.tela_inicial.lineEdit.setText('')
        self.tela_inicial.lineEdit_2.setText('')
        
        self.cpf = ''
        self.QtStack.setCurrentIndex(0)
        

    def abrirTelaloginEfetuado(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTelaDadosPessoais(self):
        try:
            print('1')
            mensagem = f'busca;{self.cpf}'
            print('2')
            self.client_socket.send(mensagem.encode())
            print('3')
            resposta = self.client_socket.recv(1024).decode()
            print('4')
            if ';' in resposta:
                nome, cpf_encotrado, email, estado, telefone, cep, cidade, data_nascimento = resposta.split(
                    ';')
                print(f'Nome: {nome}, CPF: {cpf_encotrado}, EMAIL: {email}, Estado: {estado}, Telefone: {telefone}, CEP: {cep}, Cidade: {cidade}, Data de Nascimento: {data_nascimento}')
                self.tela_dadospessoais.lineEdit_2.setText(nome)
                self.tela_dadospessoais.lineEdit_3.setText(cpf_encotrado)
                self.tela_dadospessoais.lineEdit_4.setText(email)
                self.tela_dadospessoais.lineEdit_6.setText(estado)
                self.tela_dadospessoais.lineEdit_5.setText(telefone)
                self.tela_dadospessoais.lineEdit_8.setText(cidade)
                self.tela_dadospessoais.lineEdit.setText(data_nascimento)
                self.tela_dadospessoais.lineEdit_7.setText(cep)
            
    
            else:
                print("Resposta do servidor em formato inesperado.")

        except Exception as e:
            print(f"Erro ao abrir a tela de perfil: {e}")

        self.QtStack.setCurrentIndex(3)

    def mostrar_mensagem_erro(self, mensagem):
        QMessageBox.critical(self, "...", mensagem)

    def abrirTelaAlterarDP(self):
        self.QtStack.setCurrentIndex(4)

    def abrirTelaAlugarCarro(self):
        self.QtStack.setCurrentIndex(5)

    def AbrirTelaMinhasReservas(self):
        self.QtStack.setCurrentIndex(6)

    '''def AbrirTelaCNH(self):
    
        sabe, cpf_pessoa, data_nascimento, nome_pessoa = self.cad.busca_dados(self.cpf)
        if sabe == True:
            self.tela_CNH.lineEdit_2.setText(nome_pessoa)
            self.tela_CNH.lineEdit_3.setText(cpf_pessoa)
            self.tela_CNH.lineEdit.setText(data_nascimento)
            try:
                sabe1, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci = self.cad_cnh.buscaDadosCNH(cpf_pessoa)
                if sabe1 == True:
                    self.tela_CNH.lineEdit_6.setText(rg)
                    self.tela_CNH.comboBox.setCurrentText(tipo_carteira)
                    data_CNH = QDate.fromString(data_emissao_CNH, "yyyy-MM-dd")
                    self.tela_CNH.dateEdit_2.setDate(data_CNH)
                    self.tela_CNH.lineEdit_5.setText(estado)
                    self.tela_CNH.lineEdit_7.setText(cidade)
                    data_VENCI = QDate.fromString(data_venci, "yyyy-MM-dd")
                    self.tela_CNH.dateEdit_3.setDate(data_VENCI)

                    self.tela_CNH.lineEdit_2.setReadOnly(True)
                    self.tela_CNH.lineEdit.setReadOnly(True)
                    self.tela_CNH.dateEdit_2.setReadOnly(True)
                    self.tela_CNH.lineEdit_5.setReadOnly(True)
                    self.tela_CNH.lineEdit_3.setReadOnly(True)
                    self.tela_CNH.lineEdit_6.setReadOnly(True)
                    self.tela_CNH.dateEdit_3.setReadOnly(True)
                    self.tela_CNH.lineEdit_7.setReadOnly(True)
            except:
                pass

                
        self.QtStack.setCurrentIndex(7)'''

    def abrirTelaCarrosDispo(self):
        self.QtStack.setCurrentIndex(8)

    def AbrirTelaCategoriaA(self):
        self.QtStack.setCurrentIndex(9)

    def AbrirTelaCategoriaB(self):
        self.QtStack.setCurrentIndex(10)

    def AbrirTelaCategoriaC(self):
        self.QtStack.setCurrentIndex(11)

    def AbrirTelaSobrenos(self):
        self.QtStack.setCurrentIndex(12)

    def verificarLogin(self):

        self.cpf = self.tela_inicial.lineEdit.text()
        senha = self.tela_inicial.lineEdit_2.text()
        naoamostra = 0
        if ((self.cpf != '' and senha != '') or (self.cpf != '') or (senha != '')):
            try:
                mensagem = f"login;{self.cpf};{senha}"
                self.client_socket.send(mensagem.encode())

                print('1 - mensagem enviada: ', mensagem)

                resposta = self.client_socket.recv(1024).decode()
                print('2 - resposta recebida: ', resposta)

                if resposta.lower() == 'login bem-sucedido!':
                    # Lógica para quando o login é bem-sucedido
                    print("Login bem-sucedido!")
                    self.abrirTelaloginEfetuado()
                else:
                    # Lógica para lidar com outros casos
                    self.mostrar_mensagem_erro('Usuário ou senha incorretos.')
            except Exception as e:
                print(f"erro ao conectar com o servidor: {e}")
                self.mostrar_mensagem_erro(
                    "erro ao conectar com o servidor. Verifique sua conexao")
        else:
            self.mostrar_mensagem_erro("preencha todos os campos")

        # pessoa = self.cad.busca(cpf)
        '''if (pessoa!=None):
            self.tela_dadospessoais.lineEdit_2.setText(pessoa._nome)
            self.tela_dadospessoais.lineEdit_3.setText(pessoa._cpf)
            self.tela_dadospessoais.lineEdit_4.setText(pessoa._email)
            self.tela_dadospessoais.lineEdit_6.setText(pessoa._estado)
        
            self.tela_dadospessoais.lineEdit.setText(pessoa._data_nascimento)
            self.tela_dadospessoais.lineEdit_5.setText(pessoa._telefone)
            self.tela_dadospessoais.lineEdit_7.setText(pessoa._cep)
            self.tela_dadospessoais.lineEdit_8.setText(pessoa._cidade)

            self.tela_alterarDP.nome_completo.setText(pessoa._email)
            self.tela_alterarDP.cpf_pessoa.setText(pessoa._cpf)
            self.tela_alterarDP.data_nascimentopessoa.setText(pessoa._data_nascimento)
            self.tela_alterarDP.estado_pessoa.setText(pessoa._estado)
            self.tela_alterarDP.cep_pessoa.setText(pessoa._cep)
            self.tela_alterarDP.cidade_pessoa.setText(pessoa._cidade)
            self.tela_alterarDP.email_pessoa.setText(pessoa._email)
            self.tela_alterarDP.telefone_pessoa.setText(pessoa._telefone)'''

    '''def AlterarDadosPessoais(self):
        nome = self.tela_alterarDP.nome_completo.text()
        datanasci = self.tela_alterarDP.data_nascimentopessoa.text()  
        cpf = self.tela_alterarDP.cpf_pessoa.text()
        telefone = self.tela_alterarDP.telefone_pessoa.text()
        email = self.tela_alterarDP.email_pessoa.text()
        cep = self.tela_alterarDP.cep_pessoa.text()
        estado = self.tela_alterarDP.estado_pessoa.text()
        cidade = self.tela_cadastro.lineEdit_7.text()
        senha = self.tela_cadastro.lineEdit_9.text()
        if(nome != '' and datanasci != '' and cpf != '' and telefone != '' and email != '' and cep != '' and estado != '' and cidade != '' and senha !=''):
                p = Pessoa(nome, datanasci, cpf, telefone, email, cep, estado, cidade, senha)
                
                if self.cad.cadastra(p):
                    
                    QMessageBox.information(None, 'LocaDrive', 'Cadastro realizado com sucesso!')
                    self.tela_cadastro.lineEdit.setText('') 
                    self.tela_cadastro.dateEdit.setDate(QDate.currentDate()) 
                    self.tela_cadastro.lineEdit_2.setText('')
                    self.tela_cadastro.lineEdit_3.setText('')
                    self.tela_cadastro.lineEdit_4.setText('')
                    self.tela_cadastro.lineEdit_5.setText('')
                    self.tela_cadastro.lineEdit_6.setText('')  
                    self.tela_cadastro.lineEdit_7.setText('')
                    self.tela_cadastro.lineEdit_9.setText('')
                    preencheu = 1
    
                else:
                    QMessageBox.warning(None, 'LocaDrive', 'O CPF informado já está cadastrado na base de dados!')
                               
        else:
            QMessageBox.warning(None, 'LocaDrive', 'Todos os valores devem ser preenchidos!')
            
               
        if preencheu == 1:
            self.abrirTelalogin()
        else:
            self.abrirTelaCadastro()'''

    '''def botaoCadastraCNH(self):
        preencheu = 0
        nome = self.tela_CNH.lineEdit_2.text()
        data_nasci = self.tela_CNH.lineEdit.text()
        data_emissao_CNH = self.tela_CNH.dateEdit_2.text()
        estado = self.tela_CNH.lineEdit_5.text()
        cpf = self.tela_CNH.lineEdit_3.text()

        rg = self.tela_CNH.lineEdit_6.text()
        data_venci = self.tela_CNH.dateEdit_3.text()
        cidade = self.tela_CNH.lineEdit_7.text()
        tipo_carteira = self.tela_CNH.comboBox.currentText()

        if(nome != '' and data_nasci != '' and cpf != '' and data_venci != '' and rg != '' and tipo_carteira != '' and estado != '' and cidade != '' and data_emissao_CNH !=''):
                c = CNH(nome, data_nasci, data_emissao_CNH, estado, cpf, rg, data_venci, cidade, tipo_carteira)
                
                if self.cad_cnh.cadastracnh(c):
                    QMessageBox.information(None, 'LocaDrive', 'Cadastro realizado com sucesso!')
                    self.tela_CNH.lineEdit_2.setReadOnly(True)
                    self.tela_CNH.lineEdit.setReadOnly(True)
                    self.tela_CNH.dateEdit_2.setReadOnly(True)
                    self.tela_CNH.lineEdit_5.setReadOnly(True)
                    self.tela_CNH.lineEdit_3.setReadOnly(True)
                    self.tela_CNH.lineEdit_6.setReadOnly(True)
                    self.tela_CNH.dateEdit_3.setReadOnly(True)
                    self.tela_CNH.lineEdit_7.setReadOnly(True)
        
                    preencheu = 1
    
                else:
                    QMessageBox.warning(None, 'LocaDrive', 'O CPF informado já está cadastrado na base de dados!')
                               
        else:
            QMessageBox.warning(None, 'LocaDrive', 'Todos os valores devem ser preenchidos!')
            
               
        if preencheu == 1:
            self.abrirTelaloginEfetuado()
        else:
            self.AbrirTelaCNH()'''

    def fecharPrograma(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
