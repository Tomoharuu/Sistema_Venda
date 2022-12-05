import PySimpleGUI as sg

import pandas as pd


layout = [[sg.Text("Insira o GIX Desejado"), sg.Input(size=(6,0),key='-myinput-')],
          [sg.Text('GIX Digitado: '), sg.Text(size=(50, 1), key='-mytext-')],
          [sg.Text('Descrição: '), sg.Text(size=(90, 1), key='-CSI-')],
          ]

window = sg.Window('Teste', layout, [100, 400], finalize=True)
window['-myinput-'].bind("<Return>", "_Enter")





while True:
    event, values = window.read()


    if event == sg.WIN_CLOSED or event == 'Fechar':
        break

    if event ==  '-myinput-' + "_Enter":
        codigo = int(values['-myinput-'])
        df2 = pd.read_excel("teste_gix.xlsx")
        resultado = df2.loc[df2['GIX'] == codigo, 'DESCRIÇÃO']
        resultado2 = resultado.iloc[0]
        # response = kernel.respond(input_text)
        window['-mytext-'].update(codigo)
        window['-CSI-'].update(resultado2)

window.close()
