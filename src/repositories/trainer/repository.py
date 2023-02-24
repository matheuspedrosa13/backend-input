from src.infrastructures.tiny_db.infrastructure import TinyDBInfra


class TrainerRepository:

    def __init__(self):
        self.infra = TinyDBInfra

    def search(self, query):
        client = self.infra.get_client()
        result = client.search(query)
        return result

