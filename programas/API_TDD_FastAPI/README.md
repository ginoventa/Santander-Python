# Projeto Store - API TDD FastAPI

## Como rodar o projeto

1. **Instale as dependências:**
   
   ```sh
   poetry install
   ```

2. **Ative o ambiente virtual do Poetry:**
   
   ```sh
   poetry shell
   ```

3. **Execute a aplicação:**
   
   ```sh
   uvicorn store.main:app --reload
   ```
   Acesse: http://localhost:8000

4. **Rodar os testes:**
   
   ```sh
   poetry run pytest
   ```

## Outras opções

- **Pre-commit:**
  
  Instale hooks:
  ```sh
  poetry run pre-commit install
  ```
  Rode manualmente:
  ```sh
  poetry run pre-commit run --all-files
  ```

- **Docker Compose:**
  
  Se quiser rodar com Docker Compose:
  ```sh
  docker-compose up --build
  ```

## Estrutura do projeto

- `store/` - Código principal da API
- `tests/` - Testes automatizados
- `documentação/` - Diagramas e imagens

---

