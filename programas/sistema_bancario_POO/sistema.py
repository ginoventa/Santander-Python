from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Conta: 
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    @classmethod 
    def nova_conta(cls, cliente, numero): 
        return cls(numero, cliente)
    @property
    def saldo(self): 
        return self.saldo
    @property 
    def sacar(self,valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo 

        if excedeu_saldo:
            print("Operação falhou! Dinheiro insuficiente.")
        elif valor > 0:
            self.saldo -= saldo
            print("Saque realizado com sucesso!")
            return True
        else: 
            print("Saque sem sucesso! Valor deve ser superior a 0.")
            return False
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Deposito realiazado com sucesso!")
            return True
        else: 
            print("O valor precisa ser um numero positivo!")
            return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero,cliente)
        self.limite=limite
        self.limite_saques=limite_saques
    def sacar(self,valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        excedeu_limite=valor>self.limite
        if excedeu_limite: 
            print("O valor máximo de saques foi atingido!") 
        excedeu_saque=numero_saques>self.limite_saques
        if excedeu_saque:
            print("O valor máximo de saques foi atingido!")

class Cliente: 
    def __init__(self, endereco, contas): 
        self.endereco = endereco 
        self.contas = []
    
    def realizar_transacao(self,conta,transacao): 
        transacao.registrar(conta)
    
    def adicionar_conta(self,conta): 
        self.contas.append(conta)
    
class PessoaFisica(Cliente): 
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)    