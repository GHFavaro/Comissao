i = 0

while i <= 10:
    venda = int(input("Digite o valor de vendas: "))
    nome = input("Digite o nome: ")
    lojas = int(input("Digite a loja: "))

    comissao = venda * 0.08
    comissao = venda + comissao

    
    
    print("O funcionário {} da loja {} fez {} vendas, ganhando {} reais".format(nome, lojas, venda, comissao))
    
    i -= -1