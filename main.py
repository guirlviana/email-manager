import PySimpleGUI as sg 
from config_email import Emailer  
import gui 
import threading
import os
sg.theme('Dark') 
layout = gui.layout()

window = sg.Window('EMAIL MANAGER', layout,element_justification='center',icon='email.ico') 

def send_mail(values, window):
    window['Enviar email'].update(disabled=True)
    lista_contatos = values['email_to'].split()
    mail = Emailer(email_remetente=values['email_remetente'], senha_email=values['senha_email'])

    for contato in lista_contatos:
        mail.definir_conteudo(assunto=values['assunto'],
        lista_contatos=[contato], conteudo_email=values['conteudo'])

        lista_de_anexos = mostrar_arquivos(values=values)
        lista_de_arquivos = formatar_somente_arquivos(lista=lista_de_anexos)
        lista_de_imagens = formatar_somente_imagens(lista=lista_de_anexos)
        
        if len(lista_de_arquivos) != 0:
            mail.anexar_arquivos(lista_arquivos=lista_de_arquivos)
        
        if len(lista_contatos) != 0:
            mail.anexar_imagens(lista_imagens=lista_de_imagens)

        mail.enviar_email(intervalo=5, contato=contato)
    window.write_event_value('end up', 'emails enviados com sucesso!')


def mostrar_arquivos(values):
    caminhos = values['arquivos'].replace(';', f'{os.linesep}')      
    arquivos_formatados = caminhos.split()
    lista_com_arquivos = []
    for caminho in arquivos_formatados:
        lista_com_arquivos.append(caminho)
    
    return lista_com_arquivos
    
def formatar_somente_arquivos(lista):
    lista_formatada = []
    if len(lista) == 0:
        return lista_formatada
    else:
        for arquivo in lista:
            if "png" in arquivo:
                pass
            elif "jpg" in arquivo:
                pass
            else:
                lista_formatada.append(arquivo)
        return lista_formatada
        # diferenciar se é arquivo ou foto e mandar pra cada função (criar duas listas e mandar)

def formatar_somente_imagens(lista):
    lista_formatada = []
    if len(lista) == 0:
        return lista_formatada
    else:
        for arquivo in lista:
            if "png" in arquivo:
                lista_formatada.append(arquivo)
            elif "jpg" in arquivo:
                lista_formatada.append(arquivo)
        return lista_formatada

def atualizar_botao(window):
    print('''
x======================x
|    FINALIZADO PROCESSO    |
x======================x
            ''')
    window['Enviar email'].update(disabled=False)

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
        message = values['end up']
        atualizar_botao(window)

        
    if event == 'Limpar corpo do email':
        for k, v in values.items():
            print(k)
            if k != 'arquivos':
                window[k].update('')
        window['status'].update('')
                    

    if event == 'Visualizar arquivos adicionados':
        caminhos = mostrar_arquivos(values=values)
        if len(caminhos) == 0:
            window['anexos'].update('')
        else:
            window['anexos'].update(caminhos)
        
        
window.close() 