import PySimpleGUI as sg 

  

def layout():
    layout = [[sg.Text('Email de')],[sg.Input(size=(40,1), key="email_remetente")], 
            [sg.Text('Senha do Email')],[sg.Input(password_char='*', size=(40,1), key="senha_email")],
            [sg.Text('Email para', tooltip='Separe por espaços ex (cont1@gmail.com cont2@gmail.com cont3@gmail.com)')],[sg.Input(size=(40,1), key="email_to", tooltip='Separe por espaços ex (cont1@gmail.com cont2@gmail.com cont3@gmail.com)')], 
            [sg.Text('Assunto')],[sg.Input(size=(40,1), key="assunto")],
            [sg.Text('Conteúdo do Email')],
            [sg.Multiline(size=(40,8),autoscroll=True, key="conteudo")],
            [sg.Button('Enviar email')]]
    return layout