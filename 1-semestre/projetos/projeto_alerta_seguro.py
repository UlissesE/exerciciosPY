#Eduardo Ulisses Pereira da Silva RM:566339
#Eduardo Duran Del Ciel RM:562017
#Henrique Guedes Silvestre RM:562474

# Importa bibliotecas necessárias
import random
import time

# Listas para armazenar históricos e usuários
historico_leituras = []
historico_alertas = []
usuarios = []

# Definição de limites para sensores
umidade_maximo = 75
temp_baixa = 20
temp_alta = 26
nivel_normal = 50
nivel_atencao = 100
nivel_alerta = 150
nivel_evacuacao = 200

def exibir_cabecalho():
    # Exibe o cabeçalho do sistema
    print("=" * 60)
    print("PLATAFORMA ALERTA SEGURO - CONTRA ENCHENTES")
    print("=" * 60)
    print()

def limpar():
    # Limpa a tela (simulado com várias quebras de linha)
    print("\n" * 50)

def pausar():
    # Pausa até o usuário pressionar Enter
    input("\n Aperte Enter para continuar...")

def simularTemperatura():
    # Simula leitura de temperatura
    return round(random.uniform(15, 35), 1)

def simularUmidade():
    # Simula leitura de umidade
    return round(random.uniform(40, 90), 1)

def simularNivelAgua():
    # Simula leitura do nível da água
    return round(random.uniform(40, 250), 1)

def coletar_leituras(num_amostras=5, intervalo=1):
    # Coleta e calcula a média de 5 amostras dos sensores
    print("\nColetando últimas 5 amostras...\n")
    temperaturas = 0
    umidades = 0
    niveis = 0

    for i in range(num_amostras):
        print(f"Leitura {i+1}/{num_amostras}...")
        temperaturas += simularTemperatura()
        umidades += simularUmidade()
        niveis += simularNivelAgua()
        if i <= num_amostras:
            time.sleep(intervalo)
    
    media_temperaturas = temperaturas / num_amostras
    media_umidades = umidades / num_amostras
    media_niveis = niveis / num_amostras

    # Dicionário que armazena as médias das leituras dos sensores
    leituras = {
        'temperatura': round(media_temperaturas, 1),  # valor médio da temperatura
        'umidade': round(media_umidades, 1),          # valor médio da umidade
        'nivel_agua': round(media_niveis, 1)          # valor médio do nível da água
    }

    historico_leituras.append(leituras)
    return leituras

def status_temperatura(temperatura):
    # Determina o status da temperatura
    if temperatura <= temp_baixa:
        return 'BAIXA', 'TEMPERATURA BAIXA', 'verde'
    elif temperatura < temp_alta:
        return 'NORMAL', 'TEMPERATURA NORMAL', 'verde'
    else:
        return 'CRITICO', 'TEMPERATURA ALTA', 'amarelo'

def status_umidade(umidade):
    # Determina o status da umidade
    if umidade <= umidade_maximo:
        return 'NORMAL', 'UMIDADE OK', 'verde' 
    else:
        return 'UMIDO', 'UMIDADE ALTA', 'amarelo'

def status_nivel(nivel):
    # Determina o status do nível da água
    if nivel < nivel_atencao:
        return 'NORMAL', 'Nivel de água normal', 'verde'
    elif nivel < nivel_alerta:
        return 'ATENÇÃO', 'ATENÇÃO: Nível de água alto ', 'amarelo'
    elif nivel < nivel_evacuacao:
        return 'ALERTA', 'ALERTA: Nível de água em alerta', 'vermelho'
    else:
        return 'EVACUAÇÃO', 'EVACUAR AGORA: NIVEL EXTREMO', 'vermelho'

def analisar_leituras():
    # Analisa as leituras e retorna o status de cada sensor e geral
    leituras = coletar_leituras()
    status_temp = status_temperatura(leituras['temperatura'])
    status_umid = status_umidade(leituras['umidade'])
    status_niv = status_nivel(leituras['nivel_agua'])

    status_geral = 'NORMAL'
    cor_led_geral = 'verde'
    ativar_buzzer = False

    # Avalia o status geral com base nos sensores
    for status, _, cor_led in [status_umid, status_niv]:
        if status == 'EVACUAÇÃO':
            status_geral = 'EVACUAÇÃO - ÁGUA ACIMA DE 2 METROS'
            cor_led_geral = 'vermelho'
            ativar_buzzer = True
        elif status == 'ALERTA':
            status_geral = 'ALERTA - NÍVEL DE ÁGUA ALTO'
            cor_led_geral = 'vermelho'
            ativar_buzzer = True
        elif status == 'ATENÇÃO':
            status_geral = 'ATENÇÃO - NIVEL DE ÁGUA ACIMA DO NORMAL'
            cor_led_geral = 'amarelo'
        elif status == 'UMIDO' and status_temp[0] == 'CRITICO':
            status_geral = 'ATENÇÃO - GRANDES CHANCES DE CHUVA PESADA'
            cor_led_geral = 'amarelo'
    
    # Dicionário que reúne o resultado da análise das leituras dos sensores
    resultado = {
        'temperatura': {
            'valor': leituras['temperatura'],      # valor médio da temperatura
            'status': status_temp[0],              # status da temperatura (ex: NORMAL)
            'mensagem': status_temp[1],            # mensagem descritiva
            'cor_led': status_temp[2]              # cor do LED correspondente
        },
        'umidade': {
            'valor': leituras['umidade'],          # valor médio da umidade
            'status': status_umid[0],              # status da umidade
            'mensagem': status_umid[1],            # mensagem descritiva
            'cor_led': status_umid[2]              # cor do LED correspondente
        },
        'nivel_agua': {
            'valor': leituras['nivel_agua'],       # valor médio do nível da água
            'status': status_niv[0],               # status do nível da água
            'mensagem': status_niv[1],             # mensagem descritiva
            'cor_led': status_niv[2]               # cor do LED correspondente
        },
        'geral': {
            'status': status_geral,                # status geral do sistema
            'cor_led': cor_led_geral,              # cor do LED geral
            'buzzer': ativar_buzzer                # indica se o buzzer deve ser ativado
        }
    }

    if status_geral != 'NORMAL':
        registrar_alerta(resultado)

    return resultado

def registrar_alerta(resultado_analise):
    # Registra um alerta no histórico
    # Dicionário que representa um alerta gerado pelo sistema
    alerta = {
        'status': resultado_analise['geral']['status'],           # status geral do alerta
        'temperatura': resultado_analise['temperatura']['valor'], # valor da temperatura no momento do alerta
        'umidade': resultado_analise['umidade']['valor'],         # valor da umidade no momento do alerta
        'nivel_agua': resultado_analise['nivel_agua']['valor']    # valor do nível da água no momento do alerta
    }
    historico_alertas.append(alerta)

def exibir_resultado(resultado_analise):
    # Exibe o resultado da análise das leituras
    limpar()
    exibir_cabecalho()
    temp = resultado_analise['temperatura']
    print(f"Temperatura: {temp['valor']}ºC - {temp['mensagem']}")

    umid = resultado_analise['umidade']
    print(f"Umidade: {umid['valor']}% - {umid['mensagem']}")

    nivel_agua = resultado_analise['nivel_agua']
    print(f"Nível da água: {nivel_agua['valor']}cm - {nivel_agua['mensagem']}")

    geral = resultado_analise['geral']
    print(f"\nStatus Geral: {geral['status']}")

    if geral['buzzer']:
        print("\n🔊 BEEP! BEEP! BEEP! 🔊")

def exibir_historico():
    # Exibe o histórico de alertas registrados
    limpar()
    exibir_cabecalho()    

    if not historico_alertas:
        print('Não há histórico de alertas...')
    print("\nHISTÓRICO DE ALERTAS")

    for i, alerta in enumerate(historico_alertas,1):
        print(f"\n")
        print(f"Alerta {i}")
        print(f"    Status {alerta['status']}")
        print(f"    Nivel da água: {alerta['nivel_agua']}")
        print(f"    Umidade: {alerta['umidade']}")
        print(f"    Temperatura: {alerta['temperatura']}")

def cadastrar_usuario():
    # Cadastra um novo usuário no sistema
    limpar()
    exibir_cabecalho()

    nome = ''
    while not nome:
        nome = input('Qual seu nome? ')
        if not nome:
            print("Erro: Nome não pode ser vazio.")

    email = ''
    while (not email) or ('@' not in email) or ('.' not in email):
        email = input('Qual seu email? ')
        if (not email) or ('@' not in email) or ('.' not in email):
            print("Erro: Email inválido")

    telefone = ''
    while (not telefone) or (len(telefone) < 10) or (not telefone.isdigit()):
        telefone = input('Qual seu telefone? (Apenas digitos) ')
        if (not telefone) or (len(telefone) < 10) or (not telefone.isdigit()):
            print("Erro: telefone inválido.")

    regiao = ''
    while not regiao:
        regiao = input('Qual região você mora?')
        if not regiao:
            print("Erro: Nome não pode ser vazio.")

    print('Você prefere ser notificado por...')

    canal_preferido = ""
    while canal_preferido not in ['sms', 'email']:
        canal_preferido = input('"sms" ou "email"?')
        if canal_preferido not in ['sms', 'email']:
            print('Resposta inválida. Responda com "sms" ou "email"')

    print('Deseja ser notificado em níveis de: ')
    pref_atencao = ""
    while pref_atencao not in ['s', 'n']:
        pref_atencao = input('Atenção (s/n): ')
        if pref_atencao not in ['s', 'n']:
            print('Inválido. Responda com "s" ou "n"')

    pref_alerta = ""
    while pref_alerta not in ['s', 'n']:
        pref_alerta = input('Alerta (s/n): ')
        if pref_alerta not in ['s', 'n']:
            print('Inválido. Responda com "s" ou "n"')

    pref_evacuacao = ""
    while pref_evacuacao not in ['s', 'n']:
        pref_evacuacao = input('Evacuação (s/n): ')
        if pref_evacuacao not in ['s', 'n']:
            print('Inválido. Responda com "s" ou "n"')

    # Dicionário que armazena os dados do usuário cadastrado
    usuario = {
        'nome': nome,                         # nome do usuário
        'email': email,                       # email do usuário
        'telefone': telefone,                 # telefone do usuário
        'regiao': regiao,                     # região onde mora
        'canal_preferido': canal_preferido,   # canal de notificação preferido
        'pref_atencao': pref_atencao == 's',  # preferência por receber alerta de atenção
        'pref_alerta': pref_alerta == 's',    # preferência por receber alerta de alerta
        'pref_evacuacao': pref_evacuacao == 's' # preferência por receber alerta de evacuação
    }
    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!")
    pausar()

def lista_usuario():
    # Exibe a lista de usuários cadastrados
    limpar()
    exibir_cabecalho()

    if not usuarios:
        print('Não há usuários registrados')
    for usuario in usuarios:
        print("-" * 40)
        print(f"    Nome: {usuario['nome']}")
        print(f"    Email: {usuario['email']}")
        print(f"    Telefone: {usuario['telefone']}")
        print(f"    Região: {usuario['regiao']}")
        print(f"    Canal preferido: {usuario['canal_preferido']}")
        print(f"    - Atenção: {'Sim' if usuario['pref_atencao'] else 'Não'}")
        print(f"    - Alerta: {'Sim' if usuario['pref_alerta'] else 'Não'}")
        print(f"    - Evacuação: {'Sim' if usuario['pref_evacuacao'] else 'Não'}")
        print("-" * 40)
    pausar()

def quiz():
    # Executa o quiz educativo sobre enchentes
    exibir_cabecalho()
    limpar()
    
    questao_atual = 0
    pontos = 0
    questions = [
        {
            "question": "Qual é a primeira medida a ser tomada ao receber um alerta de enchente?",
            "options": [
                "A. Verificar as redes sociais para confirmar a informação",
                "B. Reunir documentos importantes, medicamentos e itens essenciais",
                "C. Esperar até que a água comece a subir para tomar uma decisão",
                "D. Ligar para todos os vizinhos para avisar"
            ],
            "correct": 'B'
        },
        {
            "question": "Qual destes itens NÃO deve fazer parte de um kit de emergência para enchentes?",
            "options": [
                "A. Lanternas e pilhas extras",
                "B. Alimentos não perecíveis",
                "C. Equipamentos eletrônicos de valor",
                "D. Água potável"
            ],
            "correct": 'C'
        },
        {
            "question": "Durante uma enchente, é seguro:",
            "options": [
                "A. Atravessar áreas alagadas a pé",
                "B. Dirigir através de áreas com água corrente",
                "C. Permanecer em locais altos e seguros",
                "D. Tocar em equipamentos elétricos molhados"
            ],
            "correct": 'C'
        },
        {
            "question": "Qual é o principal fator que contribui para enchentes em áreas urbanas?",
            "options": [
                "A. Impermeabilização do solo",
                "B. Plantio de árvores",
                "C. Coleta seletiva de lixo",
                "D. Uso de energia renovável"
            ],
            "correct": 'A'
        },
        {
            "question": "Após uma enchente, antes de retornar para casa, é importante:",
            "options": [
                "A. Ligar imediatamente todos os equipamentos elétricos para verificar se funcionam",
                "B. Verificar se há danos estruturais e se é seguro entrar",
                "C. Beber a água da torneira para verificar se está contaminada",
                "D. Limpar imediatamente com água sanitária pura"
            ],
            "correct": 'B'
        },
        {
            "question": "Qual destas doenças NÃO está comumente associada a enchentes?",
            "options": [
                "A. Leptospirose",
                "B. Dengue",
                "C. Sarampo",
                "D. Hepatite A"
            ],
            "correct": 'B'
        },
        {
            "question": "Qual é a melhor maneira de se manter informado durante uma situação de enchente?",
            "options": [
                "A. Confiar apenas em informações de redes sociais",
                "B. Ignorar alertas oficiais se não estiver chovendo no momento",
                "C. Acompanhar boletins oficiais da Defesa Civil e meteorologia",
                "D. Sair para verificar pessoalmente o nível dos rios"
            ],
            "correct": 'C'
        },
        {
            "question": "Em caso de evacuação devido a enchentes, o que você deve fazer com animais de estimação?",
            "options": [
                "A. Deixá-los em casa com bastante comida e água",
                "B. Soltá-los para que encontrem abrigo por conta própria",
                "C. Levá-los junto no processo de evacuação",
                "D. Entregá-los aos vizinhos que não precisam evacuar"
            ],
            "correct": 'C'
        },
        {
            "question": "Qual destas ações ajuda a prevenir enchentes em áreas urbanas?",
            "options": [
                "A. Jogar lixo em bueiros e córregos",
                "B. Remover árvores e vegetação",
                "C. Impermeabilizar todo o quintal",
                "D. Implementar sistemas de captação de água da chuva"
            ],
            "correct": 'D'
        },
        {
            "question": "Qual é o papel da tecnologia no monitoramento e prevenção de enchentes?",
            "options": [
                "A. Apenas registrar dados históricos sem utilidade prática",
                "B. Substituir completamente a necessidade de evacuação",
                "C. Prever com 100% de precisão quando ocorrerão enchentes",
                "D. Fornecer alertas antecipados e monitorar níveis de água em tempo real"
            ],
            "correct": 'D'
        }
    ]
    for i, questao in enumerate(questions,1):
        questao_atual += 1
        exibir_cabecalho()
        print(f"Questão {i}:\n")
        print(f"{questao['question']}\n")
        print(f"    {questao['options'][0]}\n")
        print(f"    {questao['options'][1]}\n")
        print(f"    {questao['options'][2]}\n")
        print(f"    {questao['options'][3]}\n")
        resposta = input('\nDigite a alternativa. ').upper()
        
        if len(resposta) > 1 or resposta not in ['A', 'B', 'C', 'D']:
            while len(resposta) > 1 or resposta not in ['A', 'B', 'C', 'D']:
                print('Alternátiva inválida')
                resposta = input('\nDigite a alternativa. ').upper()
        
        if resposta == questao['correct']:
            pontos += 1

        limpar()
    
    exibir_cabecalho()
    print('Quiz finalizado!')
    print(f"Total de pontos: {pontos}/10")
        
    pausar()

def menu_principal():
    # Exibe o menu principal e retorna a opção escolhida
    limpar()
    exibir_cabecalho()
    print("MENU PRINCIPAL")
    print("=" * 40)
    print("1. Monitoramento de enchentes")
    print("2. Historico de alertas")
    print("3. Cadastrar Usuário")
    print("4. Lista de usuários")
    print("5. Quiz sobre enchentes")
    print('0. Sair')
    print("=" * 40)
    opcao = input("Escolha uma opção: ")
    return opcao

def main():
    # Função principal do sistema
    limpar()
    exibir_cabecalho()
    while True:
        opcao = menu_principal()
        if opcao == '1':
            resultado = analisar_leituras()
            exibir_resultado(resultado)
            pausar()
        elif opcao == '2':
            exibir_historico()
            pausar()
        elif opcao == '3':
            cadastrar_usuario()
        elif opcao == '4':
            lista_usuario()
        elif opcao == '5':
            quiz()
        elif opcao == '0':
            print('\nObrigado por utilizar o sistema Alerta Seguro!\n')
            break

if __name__ == "__main__":
    # Executa o sistema se o arquivo for rodado diretamente
    main()
