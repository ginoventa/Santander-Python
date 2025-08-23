from typing import Dict, List

def product_data() -> Dict[str, object]:
    """Retorna um dicionário com dados de um produto de teste."""
    return {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


def products_data() -> List[dict]:
    """Retorna uma lista de dicionários com dados de múltiplos produtos de teste."""
    return [
        {"name": "Iphone 11 Pro Max", "quantity": 20, "price": "4.500", "status": True},
        {"name": "Iphone 12 Pro Max", "quantity": 15, "price": "5.500", "status": True},
        {"name": "Iphone 13 Pro Max", "quantity": 5, "price": "6.500", "status": True},
        {"name": "Iphone 15 Pro Max", "quantity": 3, "price": "10.500", "status": False},
    ]