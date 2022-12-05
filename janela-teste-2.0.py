import PySimpleGUI as sg

import pandas as pd


layout2 = [[sg.Text("Bem-vindo!", font="Verdana")],
           [sg.Text("Total: R$"), sg.Text(key='-total')],

           [sg.Text("GIX", size=(5, 0)), sg.Text("DESCRIÇÃO", size=(47, 0)), sg.Text("PREÇO", size=(10, 0))],
           [sg.Input(size=(6, 0), key='-gix1-'), sg.Input(size=(53, 0), readonly=True, key='-descricao1-'),
            sg.Input(size=(10, 0), readonly=True, key='-preco1-')],
           [sg.Input(size=(6, 0), key='-gix2-'), sg.Input(size=(53, 0), readonly=True, key='-descricao2-'),
            sg.Input(size=(10, 0), readonly=True, key='-preco2-')],



]

window = sg.Window('LUIX', layout2, [100, 400], finalize=True)
window['-gix1-'].bind("<Return>", "_Enter")
window['-gix2-'].bind("<Return>", "_Enter")




while True:
    event, values = window.read()


    if event == sg.WIN_CLOSED or event == 'Fechar':
        break

    if event ==  '-gix1-' + "_Enter":
        codigo = int(values['-gix1-'])
        df2 = pd.read_excel("teste_gix.xlsx")
        calc1_descricao1 = df2.loc[df2['GIX'] == codigo, 'DESCRIÇÃO']
        calc2_descricao1 = calc1_descricao1.iloc[0]
        # Ajustando o Pandas para exibir somente a célula com o preço
        calc1_preco1 = df2.loc[df2['GIX'] == codigo, 'PREÇO TABELA']
        calc2_preco1 = calc1_preco1.iloc[0]
        # response = kernel.respond(input_text)
        #window['-mytext-'].update(codigo)
        window['-descricao1-'].update(calc2_descricao1)
        window['-preco1-'].update(calc2_preco1)

        total = calc2_preco1
        window["-total"].update(total)

    if event ==  '-gix2-' + "_Enter":
        codigo = int(values['-gix2-'])
        df2 = pd.read_excel("teste_gix.xlsx")
        calc_descricao1 = df2.loc[df2['GIX'] == codigo, 'DESCRIÇÃO']
        calc_descricao2 = calc_descricao1.iloc[0]
        # Ajustando o Pandas para exibir somente a célula com o preço
        calc_preco1 = df2.loc[df2['GIX'] == codigo, 'PREÇO TABELA']
        calc_preco2 = calc_preco1.iloc[0]
        # response = kernel.respond(input_text)
        #window['-mytext-'].update(codigo)
        window['-descricao2-'].update(calc_descricao2)
        window['-preco2-'].update(calc_preco2)

        total = calc_preco2 + calc2_preco1
        window["-total"]. update(total)
window.close()
