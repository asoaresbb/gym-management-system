from gym.storage.database import Banco


class Users(object):

    def __init__(self, idusuario=0, nome="", telefone="",
                 email="", usuario="", senha=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        if not self.nome.strip():
            return "O nome é obrigatório."

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute(
                "INSERT INTO usuarios (nome, telefone, email, usuario, senha) "
                "VALUES (?, ?, ?, ?, ?)",
                (self.nome, self.telefone, self.email, self.usuario, self.senha)
            )
            self.idusuario = c.lastrowid

            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            # Alterar a consulta para usar "?" no lugar de "%s" (SQLite)
            c.execute(
                "UPDATE usuarios SET nome = ?, telefone = ?, email = ?, "
                "usuario = ?, senha = ? WHERE idusuario = ?",
                (self.nome, self.telefone, self.email, self.usuario, self.senha, self.idusuario)
            )

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário: {str(e)}"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("DELETE FROM usuarios WHERE idusuario = ?", (self.idusuario,))

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("SELECT * FROM usuarios WHERE idusuario = ?", (idusuario,))
            linha = c.fetchone()
            c.close()

            if linha is None:
                return "Usuário não encontrado."

            self.idusuario = linha[0]
            self.nome = linha[1]
            self.telefone = linha[2]
            self.email = linha[3]
            self.usuario = linha[4]
            self.senha = linha[5]

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
