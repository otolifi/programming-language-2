''' ALUNOS:
Otoniel de lima Filho   RA 1901686
###############################################################################
#   AC - 03 ----------------- LINGUAGEM DE PROGRAMAÇÃO II ------------------- #
###############################################################################
'''


# Definição da Classe Gerador
class Gerador:
    def __init__(self, nome, potencia, tanque, qtde_comb, capacidade):
        self.__nome = nome
        self.__status = 'Desligado'
        self.__potencia = potencia
        self.__tanque = tanque
        self.__qtde_comb = qtde_comb
        self.__capacidade = capacidade

    def get_nome(self):
        return self.__nome

    def get_ligado(self):
        return self.__ligado

    def get_status(self):
        return self.__status

    # Comando liga/desliga
    def set_status(self):
        if self.__status == 'Ligado':
            self.__status = 'Desligado'
        else:
            self.__status = 'Ligado'
            self.__qtde_comb -= 50

    def get_potencia(self):
        return self.__potencia

    def get_tanque(self):
        return self.__tanque

    def get_qtde_comb(self):
        return self.__qtde_comb

    def abastecer(self, qtde):
        self.__qtde_comb += qtde

    def get_capacidade(self):
        return self.__capacidade


# Programa principal
def main():

    # Cria 4 geradores e liga G1 automaticamente
    g1 = Gerador('G1', 85, 500, 90, 7000)
    g2 = Gerador('G2', 80, 400, 250, 6000)
    g3 = Gerador('G3', 95, 400, 30, 8000)
    g4 = Gerador('G4', 89, 850, 850, 5000)
    g1.set_status()

    # Armazena geradores em um dicionário
    geradores = {
        g1.get_nome(): g1,
        g2.get_nome(): g2,
        g3.get_nome(): g3,
        g4.get_nome(): g4
    }

    # Exibe informações sobre um gerador
    def exibir_detalhes():
        nome_gerador = input('Informe o Nome do Gerador: ')
        if (nome_gerador in geradores):
            ger = geradores[nome_gerador]
            print('DETALHES DO GERADOR')
            print('Nome: ', ger.get_nome())
            print('Potência: ', ger.get_potencia())
            print('Capacidade de geração de energia: ', ger.get_capacidade())
            print('Tamanho do Tanque: ', ger.get_tanque())
            print('Status: ', ger.get_status())
            menu_principal()
        else:
            menu_principal()

    # Liga/Desliga um gerador
    def acionamento():
        def opc_ligar(gerador):
            status = gerador.get_status()
            print('{} está {}. Deseja {}?'.format(
                gerador.get_nome(),
                status,
                'Desligar' if status == 'Ligado' else 'Ligar')
                  )
            print('1 - Sim')
            print('2 - Não')
            opc = input()
            return opc
        nome_gerador = input('Informe o Nome do Gerador: ')
        if nome_gerador in geradores:
            ger = geradores[nome_gerador]
            tem_comb = True if ger.get_qtde_comb() >= 50 else False
            g1_ligado = True if geradores['G1'].get_status() == 'Ligado' \
                else False
            sucesso = '{} foi Ligado/Desligado com sucesso' \
                .format(ger.get_nome())
            erro_comb = '{} não pode ser ligado '\
                'por falta de combustível'.format(nome_gerador)
            erro_g1 = '{} não pode ser ligado por que '\
                'G1 está desligado'.format(nome_gerador)
            if opc_ligar(ger) == '1':
                if ger.get_status() == 'Ligado':
                    if ger.get_nome() == 'G1':
                        for gerador in geradores:
                            if geradores[gerador].get_status() == 'Ligado':
                                geradores[gerador].set_status()
                                print('{} foi Ligado/Desligado '
                                      'com sucesso'.format(gerador))
                        menu_principal()
                    else:
                        ger.set_status()
                        print(sucesso)
                        menu_principal()
                else:
                    if ger.get_nome() == 'G1':
                        if tem_comb:
                            ger.set_status()
                            print(sucesso)
                            menu_principal()
                        else:
                            print(erro_comb)
                            menu_principal()
                    elif (ger.get_nome() == 'G2' or ger.get_nome() == 'G3'
                          or ger.get_nome() == 'G4'):
                        if g1_ligado:
                            if tem_comb:
                                ger.set_status()
                                print(sucesso)
                                menu_principal()
                            else:
                                print(erro_comb)
                                menu_principal()
                        else:
                            print(erro_g1)
                            menu_principal()
            else:
                menu_principal()
        else:
            print('Erro: Não existe esse gerador!')
            menu_principal()

    # Abastece o tanque de um gerador
    def abastecimento():
        nome_gerador = input('Nome do Gerador: ')
        if nome_gerador not in geradores:
            menu_principal()
        else:
            ger = geradores[nome_gerador]
            qtde_litros = int(input('Quantidade de Litros de Combustível: '))
            qtde_limite = ger.get_tanque() - ger.get_qtde_comb()
            if qtde_litros <= qtde_limite:
                ger.abastecer(qtde_litros)
                print("Abastecimento realizado com sucesso!")
            else:
                print("Não foi possível realizar abastecimento!")
        menu_principal()

    # Exibe o status ligado/desligado dos geradores
    def exibir_status():
        print('STATUS DOS GERADORES:')
        for gerador in geradores:
            print('{} - {}'.format(gerador, geradores[gerador].get_status()))
        menu_principal()

    # Exibe o status dos tanques dos geradores
    def exibir_tanques():
        print('STATUS DOS TANQUES:')
        for gerador in geradores:
            ger = geradores[gerador]
            tanque = ger.get_tanque()
            qtde = ger.get_qtde_comb()
            print('{} - {}/{} litros{}'.format(
                gerador,
                qtde,
                tanque,
                '' if (qtde > 0.2 * tanque) else ' (ABASTECER)'))
        menu_principal()

    # menu de opções
    def menu_principal():
        print('1 - Acionamento manual de gerador')
        print('2 - Status dos geradores')
        print('3 - Status dos tanques de combustível')
        print('4 - Abastecer tanque de combustível')
        print('5 - Detalhes do gerador')
        print('6 - Sair')
        try:
            opc = input()
            opcoes[opc]()
        except KeyError:
            print('Erro: Opção incorreta!')
            menu_principal()

    opcoes = {
        '1': acionamento,
        '2': exibir_status,
        '3': exibir_tanques,
        '4': abastecimento,
        '5': exibir_detalhes,
        '6': exit
    }

    menu_principal()


main()
