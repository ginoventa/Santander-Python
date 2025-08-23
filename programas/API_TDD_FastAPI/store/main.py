

from fastapi import FastAPI
from store.core.config import settings
from store.routers import api_router


class App(FastAPI):
    """Classe principal da aplicação FastAPI customizada."""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH,
        )


# Instância global da aplicação
app = App()
app.include_router(api_router)