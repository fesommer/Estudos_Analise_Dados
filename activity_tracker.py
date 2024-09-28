#arquivo: activity_tracker.py

#Mensagem de boas-vindas
print("Bem-vindo ao Sommer training")

#Dicionário para armazenar as atividades
atividades = {
    'Tipo': [],
    'Duração (min)': [],
    'Intensidade': []
}

#Função para adicionar atividades
def adicionar_atividade(tipo, duracao, intensidade):
    atividades['Tipo'].append(tipo)
    atividades['Duração (min)'].append(duracao)
    atividades['Intensidade'].append(intensidade)
    printf(f"Atividade {tipo} adicionada com sucesso!")

    #Função para listar atividades
    def listar_atividades():
        print("\nAtividades Registradas:")
        for i in range(len(atividades['Tipo'])):
            print(f"{i+1}. {atividades['Tipo'][i]}] - {atividades['Duração (min)']} min - intensidade: {atividades[´'intensidade'][i]}")
                                                                  
        #Menu de opções
        print("\nOpções:")
        print("1. Adicionar atividade")
        print("2. Listar atividades")
        print("3. Remover atividade")
        print("4. Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
          tipo = input("Informe o tipo de exercicio (ex.: calistenia, musculação, Jiu-Jitsu): ")
          duracao = int(input("Informe a duração (em min): "))
          intensidade = input("Informe a intensidade (ex.: baixa, média, alta): ")
          adicionar_atividade(tipo, duracao, intensidade)
          elif escolha == '2':
          listar_atividades()
          elif escolha == '3':
          printf("Salvando...")
          break
          else:
          print("opção invalida, tente novamente.")

          import csv

          def salvar_atividade(nome_arquivo='atividades.csv'):
          with open(nome_arquivo, mode='w', newline='') as csvfile:
          writer = csv.writer(csvfile)
          writer.writerow(atividades.keys()) #Cabeçalhos
          writer.writerows(zip(*atividades.values())) #linhas
          print(f"atividades salvas no arquivo {nome_arquivo} com sucesso!")

          #chamada para salvar_atividades() antes de sair:

          if escolha == '3':
            salvar_atividade()
            print("Salvando...")
            break
            }

        