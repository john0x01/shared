from PySimpleGUI import PySimpleGUI as pg

sex = ''

class TelaPython:
    def __init__(self):
        #Layout
        pg.theme('Reddit')
        layout = [
            [pg.Text('Jogador:'),pg.Input(key='jogador', size=(15, 0))],
            [pg.Button('Jogar')],
            [pg.Radio('Homem','sexo', key='homem'), pg.Radio('Mulher', 'sexo', key='mulher')]
        ]

        #Janela
        janela = pg.Window('Capitalismo', layout)

        #Ler os eventos
        self.button, self.values = janela.read()

    def inciar(self):
        global sex

        nome = self.values['jogador']
        homem = self.values['homem']
        mulher = self.values['mulher']
        print(f'nome: {nome}')
        if homem == True:
            sex = 'male'
        elif mulher == True:
            sex = 'female'
        print(sex)

tela = TelaPython() 
tela.inciar()