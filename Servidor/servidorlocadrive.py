# módulo banco_de_dados.py

import socket
import threading
import json
import mysql.connector as mysql

conexao = mysql.connect(host='localhost', database='bdlocadrive', user='root', passwd='123456')
cursor = conexao.cursor()


sql1 = """
CREATE TABLE IF NOT EXISTS cadastrapessoa(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    email VARCHAR(30) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    telefone VARCHAR(12) NOT NULL,
    cep VARCHAR(15) NOT NULL,
    cidade VARCHAR(20) NOT NULL,
    data_nascimento VARCHAR(12) NOT NULL,
    senha VARCHAR(20) NOT NULL
)"""


sql2 = '''
    CREATE TABLE IF NOT EXISTS cadastracnh(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    data_nascimento VARCHAR(12) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    rg VARCHAR(20) NOT NULL,
    tipo_carteira VARCHAR(3) NOT NULL, 
    data_emissao_CNH VARCHAR(12) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    cidade VARCHAR(20) NOT NULL,
    data_venci VARCHAR(12) NOT NULL
)'''


cursor.execute(sql1)
cursor.execute(sql2)


class ServidorCadastro(threading.Thread):
    """
    Esta é a classe Servidor Cadastro 
    
    ...
    
    Attributes:
    -----------
    csocket : socket
        Socket do cliente conectado.
    addr: tuple
        Endereço do cliente conectado.
    
    Methods:
    _init_(self, clientAddress, clientesocket): 
        Inicializa a classe, recebendo o endereço e o socket do cliente conectado.
    run(self): 
        Executa o loop principal da thread, responsável por processar as solicitações do cliente.
    verificar_usuario_senha(self, cpf, senha): 
        verifica se o usuário e a senha fornecidos pelo cliente são válidos.
    cadastrar_novo_usuario(self, nome, cpf, email, estado, telefone, cep, cidade, data_nascimento, senha):
        cadastra um novo usuário no sistema.
    busca(self, cpf):
        busca um usuário no sistema pelo CPF.
    

    """    
    def __init__(self, clientAddress, clientesocket):
        """
        Responsavel por inicializar a classe, recebendo o endereco e o socket do cliente conectado.
        
        ....
        
        """
        threading.Thread.__init__(self)
        self.csocket = clientesocket
        self.addr = clientAddress
        print('Nova conexão:', clientAddress)
        
    def run(self):
        """
        Este método é responsável por executar o loop principal da thread, processando as solicitações do cliente.
        
        ...
        
        
        Returns:
        --------
        
        None que significa que não há retorno.
        
        """
        try:
            data = self.csocket.recv(1024).decode()
            operacao, *dados = data.split(';')
            dados = ';'.join(dados) 
            print('Operação:', operacao)
            print('Dados:', dados)

            if operacao == 'sair':
                print('Cliente solicitou sair. Fechando a conexão...')
                self.csocket.send("Desconectado pelo servidor".encode())
                self.csocket.close()
                return
            
            elif operacao == 'login':
                cpf, senha = dados.split(';')
                print('cpf:', cpf)
                print('senha:', senha)

                if self.verificar_usuario_senha(cpf, senha):
                    self.csocket.send("Login bem-sucedido!".encode())
                    print(f'{cpf} se conectou!')
                    
                    data = self.csocket.recv(1024).decode()
                    operacao, *dados = data.split(';')
                    dados = ';'.join(dados) 
                    print('Operação:', operacao)
                    print('Dados:', dados)
                    
                    if operacao == 'busca':
                       cpf = dados.split(';')[0]
                       print(cpf)
                       resultado = self.busca(cpf)
                       print("abaixo disso tem o resultado:")
                       print(resultado)
                       if resultado != None:
                            nome, cpf_encotrado, email, estado, telefone, cep, cidade, data_nascimento = resultado
                            resposta = f'{nome};{cpf_encotrado}; {email}; {estado};{telefone};{cep};{cidade};{data_nascimento}'
                            print(resposta)
                            self.csocket.send(resposta.encode())
                            self.csocket.close()
                       else:
                            print("Erro, não foi encontrado")
                    else:
                        print('Erro') 
                else:
                    self.csocket.send("Usuário ou senha incorretos.".encode())
                    self.csocket.close()
                    return
            elif operacao == 'cadastro':
                nome, cpf, email, estado, telefone, cep, cidade, data_nascimento, senha = dados.split(';')
                if self.cadastrar_novo_usuario(nome, cpf, email, estado, telefone, cep, cidade, data_nascimento, senha) == True:
                    self.csocket.send("Conta criada com sucesso!".encode())
                    print(f'{nome} tem uma conta no sistema!')
                else:
                    self.csocket.send("Erro na criação da conta".encode())
                    self.csocket.close()
                    return
            else:
                print(f'Operação não reconhecida: {operacao}')
        except Exception as e:
            print(f"Erro durante a execução da thread: {e}")
        finally:
            self.csocket.close()
        
    def verificar_usuario_senha(self, cpf, senha):
        """Este método verifica se o usuário e a senha fornecidos pelo cliente são válidos.
        ...
        
        Attributes:
        -----------

        cpf: str
            CPF do usuário.
        senhaa: str
            Senha do usuário.
        
        Returns:
        --------
        
        True: 
            Se o usuário e a senha forem válidos.
        False:
            Se o usuário e a senha forem inválidos.
                   
                   
        """
        query = "SELECT * FROM cadastrapessoa WHERE cpf = %s AND senha = %s"
        values = (cpf, senha)

        cursor.execute(query, values)

        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    def cadastrar_novo_usuario(self, nome, cpf, email, estado, telefone, cep, cidade, data_nascimento, senha):
        """
        Este método cadastra um novo usuário no sistema.
        
        ...
        
        Attributes:
        -----------
        
        nome: str
            Nome do usuário.
        cpf: str
            CPF do usuário.
        email: str
            Email do usuário.
        estado: str
            Estado do usuário.
        telefone: str
            Telefone do usuário.
        cep: str
            CEP do usuário.
        cidade: str
            Cidade do usuário.
        data_nascimento: str
            Data de nascimento do usuário.
        senha: str
            Senha do usuário.
        
        
        Returns:
        --------
        
        True: 
            Se o cadastro for bem-sucedido.
        False: 
            Se o cadastro não for bem-sucedido.
        
        
        """
        try:
            insert_sql = """
            INSERT INTO cadastrapessoa (nome, cpf, email, estado, telefone, cep, cidade, data_nascimento, senha)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_sql, (nome, cpf, email, estado, telefone, cep, cidade, data_nascimento, senha))
            conexao.commit()

            print("Dados inseridos com sucesso!")
            return True
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False
        
    def busca(self, cpf):
        
        """
        Este método busca um usuário no sistema pelo CPF.
        
        ...
        
        Attributes:
        cpf: str
            CPF do usuário.
        
        

        Returns:
        --------
        
        nome (str): 
            Nome do usuário.
        cpf_encontrado (str): 
            CPF do usuário.
        email (str):
            Email do usuário.
        estado (str):
            Estado do usuário.
        telefone (str): 
            Telefone do usuário.
        cep (str):  
            CEP do usuário.
        cidade (str): 
            Cidade do usuário.
        data_nascimento (str):
            Data de nascimento do usuário.
        
        """
        sql = "SELECT nome, cpf, email, estado, telefone, cep, cidade, data_nascimento FROM cadastrapessoa WHERE cpf = %s"
        cursor.execute(sql, (cpf,))
        
        resultado = cursor.fetchone()
        if resultado:
            nome, cpf_encontrado, email, estado, telefone, cep, cidade, data_nascimento = resultado
            return nome, cpf_encontrado, email, estado, telefone, cep, cidade, data_nascimento
        else:
            return None
            
  
                
if __name__ == '__main__':
    localhost = ''
    port = 1600
    addr = (localhost, port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    print('Servidor iniciado!')
    print('Aguardando nova conexão...')

    while True:
        server.listen(20)
        clientsock, clientAddress = server.accept()
        newthread = ServidorCadastro(clientAddress, clientsock)
        newthread.start()