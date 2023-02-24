from src.repositories.trainer.repository import TrainerRepository
from tinydb import Query


class TrainerService:

    repo = TrainerRepository

    @classmethod
    def search_active_trainers(cls):
        query = Query().status == True
        repo_instance = TrainerRepository()
        result = repo_instance.search(query)
        return result
