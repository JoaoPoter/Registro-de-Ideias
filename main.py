
from recursos.funcoes import limpar_tela, aguarde, inicializarBancoDeDados, escreverDados, ouvir
inicializarBancoDeDados()
listaIdeias = []
# INI - carregando dados do arquivo
banco = open("base.atitus", "r")
listaIdeias = [linha.strip() for linha in banco.readlines()]
banco.close()
# END - carregando dados do arquivo
while True:
    limpar_tela()
    print("(0) Sair")
    print("(1) Cadastrar Ideia")
    print("(2) Listar Ideias")
    print("(3) Excluir Ideia")
    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        break
    elif opcao == "1":
        print("Cadastrar Ideia")
        ideia = ouvir()
        if len(ideia) > 0:
            listaIdeias.append(ideia)
            escreverDados(listaIdeias)
            print("Ideia cadastrada com sucesso!")
            aguarde(3)
        else:
            print("Ideia inválida!")
            aguarde(1)
        
    elif opcao == "2":
        print("Listar Ideias")
        for item in listaIdeias:
            print(f"- {item}")
        input("press enter to continue...")
    elif opcao == "3":
        print("Excluir Ideia")
        contador = 0
        for item in listaIdeias:
            print(f"({contador}) - {item}")
            contador += 1
        
        while True:
            try:
                idDeletar = int(input("Informe o ID:"))
                if idDeletar < 0: 
                    print("ID inválido!")
                    aguarde(1)
                    continue
                else:
                    break
            except:
                print("Não é um número!")
                aguarde(2)
                
        try:
            del listaIdeias[idDeletar]
            escreverDados(listaIdeias)
            print("Ideia excluída com sucesso!")
            aguarde(3)
        except:
            print("ID inválido!")
            aguarde(1)
            
    else:
        print("Opção inválida!")
        aguarde(1)
    
    
print("Volte Sempre....")