
import pytest
import asyncio
from uuid import UUID
from typing import AsyncGenerator, Generator, List
from store.db.mongo import db_client
from store.schemas.product import ProductIn, ProductUpdate
from store.usecases.product import product_usecase
from tests.factories import product_data, products_data
from httpx import AsyncClient


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """Cria um novo event loop para a sessão de testes."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    """Retorna o cliente do banco MongoDB para os testes."""
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client) -> AsyncGenerator[None, None]:
    """Limpa as coleções do banco após cada teste (exceto system)."""
    yield
    db = mongo_client.get_database()
    collection_names = await db.list_collection_names()
    for collection_name in collection_names:
        if collection_name.startswith("system"):
            continue
        await db[collection_name].delete_many({})


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Retorna um cliente HTTP assíncrono para testes da API."""
    from store.main import app
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def products_url() -> str:
    """Endpoint base dos produtos."""
    return "/products/"


@pytest.fixture
def product_id() -> UUID:
    """UUID fixo para uso em testes de produto."""
    return UUID("fce6cc37-10b9-4a8e-a8b2-977df327001a")


@pytest.fixture
def product_in(product_id) -> ProductIn:
    """Instância de ProductIn para testes."""
    return ProductIn(**product_data(), id=product_id)


@pytest.fixture
def product_up(product_id) -> ProductUpdate:
    """Instância de ProductUpdate para testes."""
    return ProductUpdate(**product_data(), id=product_id)


@pytest.fixture
async def product_inserted(product_in) -> ProductIn:
    """Insere um produto no banco para uso em testes."""
    return await product_usecase.create(body=product_in)


@pytest.fixture
def products_in() -> List[ProductIn]:
    """Lista de instâncias ProductIn para testes em lote."""
    return [ProductIn(**product) for product in products_data()]


@pytest.fixture
async def products_inserted(products_in) -> List[ProductIn]:
    """Insere múltiplos produtos no banco para uso em testes."""
    return [await product_usecase.create(body=product_in) for product_in in products_in]