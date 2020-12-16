import PySimpleGUI as sg 
from config_email import Emailer  
import gui  

sg.theme('DarkBrown3') 
  

layout = gui.layout()
window = sg.Window('EMAIL MANAGER', layout) 
  

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