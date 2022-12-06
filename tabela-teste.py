import PySimpleGUI as sg
import pandas as pd

# Folowup to this video https://youtu.be/xZyqYJGjhFs
# https://www.pysimplegui.org/en/latest/call%20reference/#table-element
# To make this useful you need to save the data on exit. See https://youtu.be/BaIKzvZf-qk

td = []
Headings = ['GIX  ', 'Descrição                    ', 'Qtde', 'Preço Tabela']

layout = [[sg.Text(Headings[0]), sg.Input(size=6, key=Headings[0]), sg.Text(size=55, key=Headings[1]),
           sg.Text(size=20, key=Headings[3])],
          [sg.Text("Quantidade"), sg.Input(size=(3, 0), key=Headings[2])],
          [sg.Button('Adicionar produto'), sg.Button('Editar Produto'),  # New buttons
           sg.Button('Salvar Alteração', disabled=True), sg.Button('Deletar Produto'), sg.Exit("Fechar")],
          [sg.Table(td, Headings, key='myTable', size=(500,500))]]

window = sg.Window('LUIX', layout, size=(700, 700))

while True:
    event, values = window.read()
    if event == 'Adicionar produto':

        codigo = int(values[Headings[0]])
        df2 = pd.read_excel("teste_gix.xlsx")
        calc1_descricao1 = df2.loc[df2['GIX'] == codigo, 'DESCRIÇÃO']
        calc2_descricao1 = calc1_descricao1.iloc[0]
        # Ajustando o Pandas para exibir somente a célula com o preço
        calc1_preco1 = df2.loc[df2['GIX'] == codigo, 'PREÇO TABELA']
        calc2_preco1 = calc1_preco1.iloc[0]
        values[Headings[1]] = calc2_descricao1
        values[Headings[3]] = calc2_preco1 * int(values[Headings[2]])

        td.append([values[Headings[0]], values[Headings[1]], values[Headings[2]], values[Headings[3]]])
        window['myTable'].update(values=td)
        for i in range(3):  # Loop thru to clear boxes
            window[Headings[i]].update(value='')
    #########################  New code added between bars
    if event == 'Editar Produto':
        if values['myTable'] == []:
            sg.popup('Nenhum produto selecionado')
        else:
            editRow = values['myTable'][0]
            sg.popup('Edite o Produto Selecionado')
            for i in range(3):
                window[Headings[i]].update(value=td[editRow][i])
            window['Salvar Alteração'].update(disabled=False)
    if event == 'Salvar Alteração':
        values[Headings[1]] = calc2_descricao1
        values[Headings[3]] = calc2_preco1 * int(values[Headings[2]])
        td[editRow] = [values[Headings[0]], values[Headings[1]], values[Headings[2]], values[Headings[3]]]
        window['myTable'].update(values=td)
        for i in range(3):  # Loop thru to clear boxes
            window[Headings[i]].update(value='')
        window['Salvar Alteração'].update(disabled=True)
    if event == 'Deletar Produto':
        if values['myTable'] == []:
            sg.popup('Nenhum produto selecionado')
        else:
            if sg.popup_ok_cancel('Alteração sem retorno: Continuar?') == 'OK':
                del td[values['myTable'][0]]  # Removes the selected row
                window['myTable'].update(values=td)
    #########################
    if event in (sg.WIN_CLOSED, 'Fechar'):
        break
window.close()
