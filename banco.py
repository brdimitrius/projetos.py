
class Conta:
    def __init__(self, banco, cliente, accountid, limite=0):
        self.limite = limite
        self.banco = banco
        self.cliente = cliente
        self.accountid = accountid
    def getbanco(self):
        print("Nome do banco de "+self.cliente+ ": "+ self.banco)
    def getid(self):
        print("ID do cartão de " + self.cliente + ": "+self.accountid)
    def getname(self):
        print("Nome registrado no cartão " + self.banco + " de id (" + self.accountid + ")" + " é " + self.cliente)
    def getlimite(self):
        if self.limite == "0":
            print("O cartão "+ self.banco + " de " + self.cliente + (" de id %a"%(self.accountid)) + " não possui Limites")
        else:
            print("O cartão "+ self.banco + " de " + self.cliente + (" de id %a"%(self.accountid)) + " possui limite de R$" + self.limite )
#class ContaEspecial(Conta):
 #   def __init__(self, banco, cliente, accountid, limite=0):
  #      Conta.__init__(self, cliente, accountid)
   #     self.limite = limite


try:
    bankname = input(
        "Escolha o banco:\n\n[1] Bradesco\n[2] Itau\n[3] Banco do Brasil\n[4] Santander\n[5] Caixa\n[6] American Express\n[7] Banco do Nordeste\n[8] Banco BMG\n\nDigite o numero aqui (1-5): ")
    if bankname == "1":
        bank = "Bradesco"
    elif bankname == "2":
        bank = "Itau"
    elif bankname == "3":
        bank = "Banco do Brasil"
    elif bankname == "4":
        bank = "Santander"
    elif bankname == "5":
        bank = "Caixa"
    elif bankname == "6":
        bank = "American Express"
    elif bankname == "7":
        bank = "Banco do nordeste"
    elif bankname == "8":
        bank = "Banco BMG"
    clientname = input("\nInsira o nome e sobrenome registrado no cartão " + bank + ": ")
    accountlimit = input("\nInsira o limite do cartão: ")
    accoid = input("\nColoque o id da sua conta do banco: ")
    Conta.accountid = accoid
    Conta.banco = bank
    Conta.cliente = clientname
    Conta.limite = accountlimit
    Conta1 = Conta(Conta.banco, Conta.cliente, Conta.accountid, Conta.limite)
    Conta1.getname()
    print("")
    Conta1.getid()
    print("")
    Conta1.getbanco()
    print("")
    Conta1.getlimite()
except:
    print("Insira valores somente de 1 a 8")
