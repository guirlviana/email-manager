
import PySimpleGUI as sg 

  

def layout():
    left_column = [
            [sg.Text('Email de')],[sg.Input(size=(60,1), key="email_remetente")], 
            [sg.Text('Senha do Email')],[sg.Input(password_char='*', size=(60,1), key="senha_email")],
            [sg.Text('Email para', tooltip='Separe por espaços ex (cont1@gmail.com cont2@gmail.com cont3@gmail.com)')],[sg.Input(size=(60,1), key="email_to", tooltip='Separe por espaços ex (cont1@gmail.com cont2@gmail.com cont3@gmail.com)')], 
            [sg.Text('Assunto')],[sg.Input(size=(60,1), key="assunto")],
            [sg.Text('Conteúdo do Email')],
            [sg.Multiline(size=(60,5),autoscroll=True, key="conteudo")],
            [sg.Text('Arquivos adicionados ao corpo do email: ')],
            [sg.Multiline(size=(60,5), key='anexos',disabled=True)],
            [sg.FilesBrowse('Anexar Arquivos',key='arquivos',size=(25,0)),sg.Button('Visualizar arquivos adicionados',size=(25,0))],
        
            
        ]

    right_column = [
        [sg.Text('Acompanhe o processo aqui: ')],        
        [sg.Output(size=(58,26),k='status')],
        [sg.Button('Enviar email',size=(25,0)), sg.Button('Limpar corpo do email',size=(25,0))],
        ]
    return [[sg.Column(left_column),sg.Column(right_column)]]