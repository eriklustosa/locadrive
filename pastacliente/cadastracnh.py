#comentario para teste
import mysql.connector as mysql

conexao = mysql.connect(host='localhost', database='cadastracnh', user='root', passwd='123456')
cursor = conexao.cursor()

sql = """
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
    
  

)
"""
# nome, data_nascimento, data_emissao_CNH, estado, cpf, rg, data_venci, cidade, tipo_carteira
cursor.execute(sql)

#nome, datanascimento, cpf, rg, tipo_carteira, data_emissao_CNH, estado, cidade, data_venci

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

# O QUE JA TEM: NOME, DATANASCI, CPF. BUSCAR NO BANCO DE DADOS