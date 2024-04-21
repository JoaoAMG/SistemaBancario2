menu = """
[1] Criar Usúario
[2] Criar Conta
[3] Depositar
[4] Sacar
[5] Extrato
[6] Sair




=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
cliente = {}
usuarios = {}
def verificar_cpf_existente(cpf):
    return cpf in usuarios

def usuario(nome,cpf,dtnascimento,endereco):
    if len(cpf)>= 12:
        nome = str(input("Digite seu nome: "))
        dtnascimento = str(input("Digite sua idade: dia/mes/ano "))
        cpf = str(input("informe seu cpf(sem tracos e pontos): "))
        endereco = str(input("informe seu endereço(somente logradouro,número - cidade - bairro - cidade/sigla estado.)"))
    
    if not verificar_cpf_existente(cpf):
        usuarios[cpf] = {
            'nome': nome,
            'cpf': cpf,
            'dtnascimento': dtnascimento,
            'endereco': endereco,
            'contas': []
        }
        print("Usuário cadastrado com sucesso!")
    else:
        print("CPF já cadastrado! Não é possível cadastrar novamente.")
    return(nome,cpf,dtnascimento,endereco)

    
def contas(cpf,usuarios):
    
    if cpf in usuarios:
        
        numero_conta = len(usuarios[cpf]['contas']) + 1

        nova_conta = {
            'numero': numero_conta,
            'agencia': "0001"
        }
       
        usuarios[cpf]['contas'].append(nova_conta)
        print("Conta criada com sucesso!")
        print(f"Seu número de conta é: {numero_conta}")
        print("Agência: 0001")
    else:
        print("Usuário não encontrado.")
        

def depositar(saldo,valor,extrato,/):
    if  valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n Deposito realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato
    
def saque(*,saldo,valor,extrato,limite,numero_saques,LIMITE_SAQUES):
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

        return saldo,extrato

def mostrarextrato(saldo,/,*,extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        return(saldo,extrato)

"""def mostrar_usuarios():
    if usuarios:
        print("=== Usuários Cadastrados ===")
        for cpf, dados_usuario in usuarios.items():
            print(f"CPF: {cpf}")
            print(f"Nome: {dados_usuario['nome']}")
            print(f"Data de Nascimento: {dados_usuario['dtnascimento']}")
            print(f"Endereço: {dados_usuario['endereco']}")
            print("--------------------------")
    else:
        print("Não há usuários cadastrados no sistema.")"""


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)
        
        if opcao == "1":
            nome = input("Digite seu nome: ")
            dtnascimento = input("Digite sua idade: dia/mes/ano ")
            cpf = input("Informe seu CPF (sem traços ou pontos): ")
            endereco = input("Informe seu endereço (logradouro, número - cidade - bairro - cidade/estado): ")
            
            usuario(nome, cpf, dtnascimento, endereco)
                
        elif opcao == "2":
            cpf = input("Informe seu CPF (sem traços ou pontos): ")
            if verificar_cpf_existente(cpf):
                contas(cpf, usuarios)
                
        elif opcao == "3":
            cpf = input("Informe seu CPF (sem traços ou pontos): ")
            if verificar_cpf_existente(cpf) and 'contas' in usuarios[cpf]:
                valor = float(input("Informe o valor do depósito: "))
                saldo, valor = depositar(saldo, valor, extrato)
            else:
                print("Você precisa se cadastrar (opção 1) e criar uma conta (opção 2) antes de fazer um depósito.")
                
        elif opcao == "4":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
                
        elif opcao == "5":
            mostrarextrato(saldo, extrato=extrato)

        elif opcao == "6":
            break  

        else:
            print("""Operação inválida. Por favor, escolha uma opção válida.""")

main()

