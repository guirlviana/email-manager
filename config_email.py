import os
import smtplib
from email.message import EmailMessage
import imghdr
import time
class Emailer:
    def __init__(self, email_remetente, senha_email):        
        # config login
        self.email_remetente = email_remetente
        self.senha_email = senha_email
    
    def definir_conteudo(self, assunto, lista_contatos, conteudo_email):
        #criando email
        self.msg = EmailMessage()
        self.msg['Subject'] = assunto
        self.msg['From'] = self.email_remetente
        self.msg['To'] = ', '.join(lista_contatos) #colocar virgulas entres o email

        self.msg.set_content(conteudo_email)

    def anexar_imagens(self, lista_imagens):
        #configurar anexo imagens
        imagens = lista_imagens
        for imagem in imagens:
            with open(imagem, 'rb') as arquivo:
                dados = arquivo.read()
                extensao = imghdr.what(arquivo.name)
                nome_arquivo = arquivo.name
            self.msg.add_attachment(dados, maintype='image', 
                    subtype=extensao, filename=nome_arquivo)

    def anexar_arquivos(self, lista_arquivos):
        #Anexar arquivos
        arquivos = lista_arquivos
        for arquivo in arquivos:
            with open(arquivo, 'rb') as a:
                dados = a.read()
                nome_arquivo = a.name
            self.msg.add_attachment(dados, maintype='application', subtype='octet-stream', filename=nome_arquivo)

    def enviar_email(self, intervalo, contato):
        # envio
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as stmp:
                stmp.login(self.email_remetente, self.senha_email)
                stmp.send_message(self.msg)
                time.sleep(intervalo)

        except Exception:
            print(f'Não foi possivel enviar o email para {contato}')
        else:
            print(f'Email enviado com sucesso para {contato}!')