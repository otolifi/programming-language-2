import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = sqlalchemy.create_engine('sqlite:///server.db')
connection = engine.connect()

Base = declarative_base(engine)

session = Session()

connection.execute(
    """
    CREATE TABLE IF NOT EXISTS AUTOR (
        ID INTEGER PRIMARY KEY,
        NOME VARCHAR(255) NOT NULL
    )
    """
)


class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))

    def __init__(self, nome):
        self.nome = nome


autor1 = Autor('Miguel de Cervantes')
autor2 = Autor('Machado de Assis')

autores = [autor1, autor2]

session.add_all(autores)

session.commit()

print('-'*15 + 'AUTORES' + '-'*15)
result = session.query(Autor).all()
for i in result:
    print(f"{i.id} - {i.nome}")


connection.execute(
    """
    CREATE TABLE IF NOT EXISTS LIVRO (
        ID INTEGER PRIMARY KEY,
        TITULO VARCHAR(255) NOT NULL,
        PAGINAS INTEGER NOT NULL,
        AUTOR_ID INTEGER NOT NULL
    )
    """
)


class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255))
    paginas = Column('PAGINAS', Integer)
    autor_id = Column('AUTOR_ID', Integer)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


livro1 = Livro('Dom Quixote', 600, 1)
livro2 = Livro('Dom Casmurro', 400, 2)

livros = [livro1, livro2]

session.add_all(livros)

session.commit()

print('-'*15 + 'LIVROS' + '-'*15)
result = session.query(Livro).all()
for i in result:
    print(f"{i.id} - {i.titulo} - \
{session.query(Autor).get(i.autor_id).nome} - {i.paginas} pgs")
