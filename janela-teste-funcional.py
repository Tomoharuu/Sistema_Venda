import PySimpleGUI as sg

import pandas as pd


layout2 = [[sg.Text("Bem-vindo!", font="Verdana")],

           [sg.Text("GIX", size=(5, 0)), sg.Text("DESCRIÇÃO", size=(47, 0)), sg.Text("PREÇO", size=(10, 0))],
           [sg.Input(size=(6, 0), key='-myinput-'), sg.Input(size=(53, 0), readonly=True, key='-CSI-'),
            sg.Input(size=(10, 0), readonly=True, key='-preco-')],



]

layout = [[sg.Text("Insira o GIX Desejado"), sg.Input(size=(6,0),key='-myinput-')],
          [sg.Text('GIX Digitado: '), sg.Text(size=(50, 1), key='-mytext-')],
          [sg.Text('Descrição: '), sg.Text(size=(90, 1), key='-CSI-')],
          ]

window = sg.Window('LUIX', layout2, [100, 400], finalize=True)
window['-myinput-'].bind("<Return>", "_Enter")





while True:
    event, values = window.read()


    if event == sg.WIN_CLOSED or event == 'Fechar':
        break

    if event ==  '-myinput-' + "_Enter":
        codigo = int(values['-myinput-'])
        df2 = pd.read_excel("teste_gix.xlsx")
        descricao1 = df2.loc[df2['GIX'] == codigo, 'DESCRIÇÃO']
        descricao2 = descricao1.iloc[0]
        # Ajustando o Pandas para exibir somente a célula com o preço
        preco1 = df2.loc[df2['GIX'] == codigo, 'PREÇO TABELA']
        preco2 = preco1.iloc[0]
        # response = kernel.respond(input_text)
        #window['-mytext-'].update(codigo)
        window['-CSI-'].update(descricao2)
        window['-preco-'].update(preco2)

window.close()