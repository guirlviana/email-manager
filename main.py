import PySimpleGUI as sg 
from config_email import Emailer  
import gui 
import threading

sg.theme('DarkBrown3') 
  

layout = gui.layout()
window = sg.Window('EMAIL MANAGER', layout) 

def send_mail(values, window):
    window['Enviar email'].update(disabled=True)
    lista_contatos = values['email_to'].split()
    mail = Emailer(email_remetente=values['email_remetente'], senha_email=values['senha_email'])
    for contato in lista_contatos:
        mail.definir_conteudo(assunto=values['assunto'],
        lista_contatos=[contato], conteudo_email=values['conteudo'])
        mail.enviar_email(intervalo=5, contato=contato)
    window.write_event_value('end up', 'emails enviados com sucesso!')

while True:   
    event, values = window.read() 

    if event in (None, 'Exit'): 
        break
    
    if event == 'Enviar email':
        thread_sendmail = threading.Thread(target=send_mail,
                                         args=(values, window,),daemon=True)
        thread_sendmail.start()
    
    elif event == 'end up':
        thread_sendmail.join()
        print(values['end up'])
        window['Enviar email'].update(disabled=False)

window.close() 