from pydantic import BaseModel


class Treinador(BaseModel):
    nome_treinador: str
    sobrenome_treinador: str
    idade_treinador: int
    num_pokemons: int

