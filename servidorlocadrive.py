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

'''class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, telefone, email, cep, estado, cidade, senha):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._telefone= telefone
        self._email = email
        self._cep = cep
        self._estado = estado
        self._cidade = cidade
        self._senha = senha

class Cadastro:

    def cadastra(self, pessoa):
        existe = self.busca(pessoa)
        if existe:
            insert_sql = """
            INSERT INTO cadastrapessoa (nome, cpf, email, estado, telefone, cep, cidade, data_nascimento, senha)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            with self.conexao.cursor() as cursor:
                cursor.execute(insert_sql, (pessoa._nome, pessoa._cpf, pessoa._email, pessoa._estado,
                                            pessoa._telefone, pessoa._cep, pessoa._cidade, pessoa._data_nascimento, pessoa._senha))
            conexao.commit()
            return True
        else:
            return False

    def busca(self, pessoa):
        #Verifica se o CPF já existe
        select_sql = "SELECT * FROM cadastrapessoa WHERE cpf = %s"
        cursor.execute(select_sql, (pessoa._cpf,))
        result = cursor.fetchone()
        
        #Se o CPF já existir, retorna False
        if result:
            return False
        else:
            return True

    def buscausuario(self, cpf, senha):
    
        query = "SELECT * FROM cadastrapessoa WHERE cpf = %s AND senha = %s"
        values = (cpf, senha)

        cursor.execute(query, values)

        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    def busca_dados(self, cpf):
        sql = "SELECT cpf, data_nascimento, nome FROM cadastrapessoa WHERE cpf = %s"
        cursor.execute(sql, (cpf,))

        resultado = cursor.fetchone()

        if resultado:
            cpf, data_nascimento, nome = resultado
            return True, cpf, data_nascimento, nome
        else:
            return None
        
    def busca_dadosPessoais(self, cpf):
        sql = "SELECT nome, cpf, email, estado, telefone, cep, cidade, data_nascimento FROM cadastrapessoa WHERE cpf = %s"
        cursor.execute(sql, (cpf,))
        
        resultado = cursor.fetchone()
        if resultado:
            nome, cpf, email, estado, telefone, cep, cidade, data_nascimento = resultado
            return nome, cpf, email, estado, telefone, cep, cidade, data_nascimento
        else:
            None


# módulo cadastra_cnh.py


class Cadastra_CNH:
#nome, datanasci, cpf, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci
    def cadastracnh(self, cnh):
        existe = self.busca(cnh)
        if existe == True:
            insert_sql = """
            INSERT INTO cadastracnh (nome, data_nascimento, cpf, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_sql, (cnh._nome, cnh._data_nascimento, cnh._cpf, cnh._rg, cnh._tipo_carteira, cnh._data_emissao_CNH, cnh._estado, cnh._cidade, cnh._data_venci))
            conexao.commit()
            return True
        else:
            return False
    
    def busca(self, cnh):
        #Verifica se o RG já existe
        select_sql = "SELECT * FROM cadastracnh WHERE rg = %s"
        cursor.execute(select_sql, (cnh._rg,))
        result = cursor.fetchone()
        
        #Se o CPF já existir, retorna False
        if result:
            return False
        else:
            return True
    
    def buscaDadosCNH(self, cpf):
        sql = "SELECT rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci FROM cadastracnh WHERE cpf = %s"
        cursor.execute(sql, (cpf,))
        
        resultado = cursor.fetchone()
        if resultado:
            rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci = resultado
            return True, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci
        else:
            None'''



# módulo servidor_cadastro.py


class ServidorCadastro(threading.Thread):
    def __init__(self, clientAddress, clientesocket):
        threading.Thread.__init__(self)
        self.csocket = clientesocket
        self.addr = clientAddress
        print('Nova conexão:', clientAddress)
        
    def run(self):
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
                    
                    elif operacao == "cadastracnh":
                        data = self.csocket.recv(1024).decode()
                        operacao, *dados = data.split(';')
                        dados = ';'.join(dados) 
                        print('Operação:', operacao)
                        print('Dados:', dados)
                        nome, data_nascimento, cpf, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci = dados.split(';')
                        
                        if self.cadastracnh(nome, data_nascimento, cpf, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci):
                            
                            print(f'{nome} tem uma conta no sistema!')
                       
                        else:
                            print("Erro na criação da cnh")
                            self.csocket.close()
                            return
                        
                    elif operacao == "buscacnh":
                        data = self.csocket.recv(1024).decode()
                        operacao, *dados = data.split(';')
                        dados = ';'.join(dados) 
                        print('Operação:', operacao)
                        print('Dados:', dados)

                        cpf = dados.split(';')[0]
                        print(cpf)
                        resultado = self.busca(cpf)
                        print("abaixo disso tem o resultado:")
                        print(resultado)
                        if resultado != None:
                            nome, data_nascimento, cpf, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci = resultado
                            resposta = f'{nome};{data_nascimento}; {cpf}; {rg};{tipo_carteira};{data_emissao_CNH};{estado};{cidade}; {data_venci}'
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
        query = "SELECT * FROM cadastrapessoa WHERE cpf = %s AND senha = %s"
        values = (cpf, senha)

        cursor.execute(query, values)

        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    def cadastrar_novo_usuario(self, nome, cpf, email, estado, telefone, cep, cidade, data_nascimento, senha):
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
        sql = "SELECT nome, cpf, email, estado, telefone, cep, cidade, data_nascimento FROM cadastrapessoa WHERE cpf = %s"
        cursor.execute(sql, (cpf,))
        
        resultado = cursor.fetchone()
        if resultado:
            nome, cpf_encontrado, email, estado, telefone, cep, cidade, data_nascimento = resultado
            return nome, cpf_encontrado, email, estado, telefone, cep, cidade, data_nascimento
        else:
            return None

    def cadastracnh(self, nome, data_nascimento, cpf, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci):
        existe = self.buscacnh(cpf)
        if existe == True:
            insert_sql = """
            INSERT INTO cadastracnh (nome, data_nascimento, cpf, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_sql, (nome, data_nascimento, cpf, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci))
            conexao.commit()
            return True
        else:
            return False
    
    def buscacnh(self, cpf):
        #Verifica se o RG já existe
        select_sql = "SELECT * FROM cadastracnh WHERE cpf = %s"
        cursor.execute(select_sql, (cpf,))
        result = cursor.fetchone()
        
        #Se o CPF já existir, retorna False
        if result:
            return False
        else:
            return True
    

    
    def buscacnhmostra(self, cpf):
        #Verifica se o RG já existe
        select_sql = "SELECT * FROM cadastracnh WHERE cpf = %s"
        cursor.execute(select_sql, (cpf,))
        result = cursor.fetchone()
        
        #Se o CPF já existir, retorna False
        if result:
            nome, data_nascimento, cpf_encotrado, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci = result

            return nome, data_nascimento, cpf_encotrado, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci
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