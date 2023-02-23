from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
from tinydb import TinyDB, Query
from enum import Enum

db = TinyDB("db.json")

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Treinador(BaseModel):
    nome_treinador: str
    sobrenome_treinador: str
    idade_treinador: int
    num_pokemons: int


unique_id = str(uuid4())


@app.get('/')
def raiz():
    return db.all()


@app.get("/vertodosostreinadores")
def get_todos_os_treinadores():
    return db.all()

@app.get("/vertreinadoresativos")
def get_todos_os_treinadores():
    return db.search((Query().status == True))

@app.post("/adicionartreinadores")
def inserir_treinador(treinador: Treinador):
    id = len(db)
    nome = treinador.nome_treinador
    sobrenome = treinador.sobrenome_treinador
    if(db.search(Query().nome == nome) and db.search(Query().sobrenome == sobrenome)):
        return 'Não pode adicionar dois treinadores com o mesmo nome e sobrenome'

    else:
        db.insert({"id": id, "nome": nome, "sobrenome": sobrenome,
                   "idade": treinador.idade_treinador,
                   "num_pokemons": treinador.num_pokemons, "status": True})
        return {"id": id, "nome": nome, "sobrenome": sobrenome,
                "idade": treinador.idade_treinador,
                "num_pokemons": treinador.num_pokemons, "status": True}
#
@app.put("/alterarTreinador")
def alterar_treinador(id: int, coluna: str, novo_valor):

    class Colunas(Enum):
        nome = "nome"
        sobrenome = "sobrenome"
        idade = "idade"
        numerodepoke = "num_pokemons"

    colunas = [elem.value for elem in Colunas]
    if coluna in colunas:
        if(db.search(Query().id == id) and db.search(Query().status == True)):
            db.update({coluna: novo_valor},
                Query().id == id
            )
            return db.search(Query().id == id)
        else:
            return 'Não é possível alterar treinador desativado! Tente outro.'
    else:
        return 'Coluna Inválida'

@app.put("/desativarTreinador")
def desativar_treinador(id: int):
    db.update(
        {"status": False},
        Query().id == id
    )
    return db.search(Query().id == id)


# print(db.search(Query().id.exists()))
# print(db.search(Query().status))
# print(db.all())
