#-*- coding:utf-8 -*-

class Sacolão():
    def Vendas():    
        Nome = [0]*9999
        Tipo = [0]*9999
        Preço = [0]*9999
        qtd = [0]*9999
        SubTotal = [0]*9999
        VendaTotal = 0
        
        n = 0
        i = 1
        while(i!=0 and n<9999):
            print("Digite o nome do produto vendido: ")
            Nome[n] = input()
            print("Digite o tipo do produto vendido: ")
            Tipo[n] = input()
            print("Digite o preço do produto: ")
            Preço[n] = float (input())
            print("Digite a quantidade de produtos vendidos: ")
            qtd[n] = float (input())
                       
            SubTotal[n] = qtd[n] * Preço[n]
            VendaTotal = VendaTotal + SubTotal[n]

            print("Digite 1 para continuar ou 0 para sair: ")
            i = int (input())
            print("")
            
            n = n + 1


        print("")
        print("")
     

        k = 0
        while (k<n):
            print("Nome do Produto: ",Nome[k])
            print("Tipo do Produto: ",Tipo[k])
            print("Preço do Produto: R$%.2f" % Preço[k])
            print("Quantidade: %.0f" % qtd[k])
            print("SubTotal: R$%.2f" % SubTotal[k])
             
            print("")
            k = k + 1

        print("")
        print("Venda Total: R$%.2f" % VendaTotal)


s = Sacolão
s.Vendas()










