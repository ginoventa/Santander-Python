tem fins educativos;

# Store API - Projeto TDD com FastAPI

## O que é TDD?
TDD (Test Driven Development) é o Desenvolvimento Orientado a Testes. O ciclo do TDD consiste em:
- Escrever um teste antes do código
- Implementar o código para passar no teste
- Refatorar e melhorar o código

### Vantagens do TDD
- Garante software de qualidade
- Ajuda a encontrar falhas rapidamente
- Incentiva testes unitários e de integração
- Evita código desnecessário ou fora do escopo
- Garante que requisitos sejam atendidos desde o início

> "Com TDD, você codifica antes mesmo do código existir, garantindo mais qualidade e menos retrabalho."

---

## Sobre o Projeto
Esta API foi desenvolvida em FastAPI, utilizando TDD, MongoDB para persistência, Pydantic para validação e Pytest para testes.

### Objetivo
Proporcionar aprendizado prático de TDD, FastAPI e testes automatizados.

### O que é?
- Uma aplicação educativa
- Permite aprender TDD na prática com FastAPI + Pytest

### O que não é?
- Não se comunica com apps externas

---

## Solução Proposta
Desenvolvimento de uma API simples, com testes de Schemas, Usecases e Controllers (integração), para fixar o ciclo do TDD.

---

## Arquitetura e Diagramas
- Arquitetura baseada no modelo C4
- Banco de dados: MongoDB
- Diagramas de sequência para o módulo de Produtos:
	- Criação de produto
	- Listagem de produtos
	- Detalhamento de produto
	- Atualização de produto
	- Exclusão de produto

---

## Desafio Final
- **Create:** Mapear exceções de inserção e capturar na controller
- **Update:**
	- Retornar Not Found se o dado não for encontrado (tratar na controller)
	- Retornar mensagem amigável ao usuário
	- Atualizar o campo `updated_at` ao modificar dados
- **Filtros:**
	- Cadastre produtos com preços variados
	- Aplique filtro: (price > 5000 and price < 8000)

---

## Preparando o Ambiente
Utilize Pyenv + Poetry para gerenciar versões e dependências Python.

Veja a documentação oficial do Poetry para instruções:
https://python-poetry.org/docs/