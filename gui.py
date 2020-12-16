import PySimpleGUI as sg 
from config_email import Emailer  
  

sg.theme('DarkBrown3') 
  
layout = [[sg.Text('Email de')],[sg.Input(size=(40,1), key="email_remetente")], 
          [sg.Text('Senha do Email')],[sg.Input(password_char='*', size=(40,1), key="senha_email")],
          [sg.Text('Email para', tooltip='Separe por espaços ex (cont1@gmail.com cont2@gmail.com cont3@gmail.com)')],[sg.Input(size=(40,1), key="email_to", tooltip='Separe por espaços ex (cont1@gmail.com cont2@gmail.com cont3@gmail.com)')], 
          [sg.Text('Assunto')],[sg.Input(size=(40,1), key="assunto")],
          [sg.Text('Conteúdo do Email')],
          [sg.Multiline(size=(40,8),autoscroll=True, key="conteudo")],
          [sg.Button('Enviar email')]]
  
window = sg.Window('Theme List', layout) 
  

while True:   
    event, values = window.read() 
    if event in (None, 'Exit'): 
        break
    
    if event == 'Enviar email':
        mail = Emailer(email_remetente=values['email_remetente'], senha_email=values['senha_email'])
        mail.definir_conteudo(assunto=values['assunto'],
        lista_contatos=values['email_to'].split(), conteudo_email=values['conteudo'])
        mail.enviar_email(intervalo=5)
      
window.close() 