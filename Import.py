class Import:
    pass


from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João", "123-144")
conta = Conta (c1.get_nome(), 148)
#print(conta.titular, "NUMERO:", conta.numero, "SEU SALDO É:", conta.saldo)
conta.deposita(200)
conta.saque(40)
conta.extrato()
