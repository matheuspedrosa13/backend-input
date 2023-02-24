from tinydb import TinyDB


class TinyDBInfra:

    __db = None

    @classmethod
    def get_client(cls) -> TinyDB:
        if cls.__db is None:
            cls.__db = TinyDB("db.json")
        return cls.__db

