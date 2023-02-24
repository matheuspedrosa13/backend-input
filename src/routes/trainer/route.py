from src.services.trainer.service import TrainerService
from src.services.router.service import Router

router = Router.get_router()

@router.get("/vertreinadoresativos")
def get_todos_os_treinadores():
    return TrainerService.search_active_trainers()
