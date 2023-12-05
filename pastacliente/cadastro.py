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


class Cadastro:
 
    def cadastra(self, pessoa):
        existe = self.busca(pessoa)
        if existe == True:
            insert_sql = """
            INSERT INTO cadastrapessoa (nome, cpf, email, estado, telefone, cep, cidade, data_nascimento, senha)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_sql, (pessoa._nome, pessoa._cpf, pessoa._email, pessoa._estado, pessoa._telefone, pessoa._cep, pessoa._cidade, pessoa._data_nascimento, pessoa._senha))
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
            None


# O QUE JA TEM: NOME, DATANASCI, CPF. BUSCAR NO BANCO DE DADOS