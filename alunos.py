from conexao import conectar

class Aluno:
    def __init__(self, nome, media, id_aluno = None, cadastrado_em = None):
        self.id_aluno = id_aluno
        self.nome = nome
        self.media = media
        self.cadastrado_em = cadastrado_em

    def mostrar(self):
        print (f"""
    Código: {self.id_aluno}
    Nome: {self.nome}
    Média: {self.media}
    Cadastrado_em: {self.cadastrado_em}
    """)

    def mostrar_id(self):
        print(f"""
    Código: {self.id_aluno}
    Nome: {self.nome}
    Média: {self.media}
    """)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO alunos (nome, media) VALUES (%s, %s)"
        cursor.execute(sql, (self.nome, self.media))

        conexao.commit()
        conexao.close()

def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM alunos"
    cursor.execute(sql)

    alunos = []
    for id_aluno, nome, media, cadastrado_em in cursor.fetchall():
        aluno = Aluno(nome, media, id_aluno, cadastrado_em)
        alunos.append(aluno)

    conexao.close()
    return alunos

def mostrar_aluno(id_aluno):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT id_aluno, nome, media FROM alunos WHERE id_aluno = %s"
    cursor.execute(sql, (id_aluno,))

    # Buscar apenas um registro
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        cod, nome, media = resultado
        return Aluno(nome, media, cod)
    
    return None