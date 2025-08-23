
from store.models.base import CreateBaseModel
from store.schemas.product import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    """Modelo de produto para persistência no banco."""
    pass