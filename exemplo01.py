from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


# Conectar ao SQLite em memoria
engine = create_engine('sqlite:///meubanco.db', echo=True)

# conn = create_engine('duckdb:///duckdb.db').connect()

# URI = "postgresql+pyodbc://dbuser:kx%40jj5%2Fg@pghost10/appdb"
# dialect+driver://username:password@host:port/database

print('Conecao com SQLite estabelecida')


Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)


# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()

# novo_usuario = Usuario(nome='Joao', idade=28)
# session.add(novo_usuario)
# session.commit()

# print('Usuario inserido com sucesso')


# try:
#     novo_usuario = Usuario(nome='Ana', idade=25)
#     session.add(novo_usuario)
#     session.commit()
# except:
#     session.rollback()
#     raise
# finally:
#     session.close()

with Session() as session:
    novo_usuario = Usuario(nome='Ana', idade=69)
    session.add(novo_usuario)
    session.commit()

resultado = session.query(Usuario).filter_by(nome='Ana').first()


print(f'Usuario encontrado: {resultado.nome}, Idade: {resultado.idade}')