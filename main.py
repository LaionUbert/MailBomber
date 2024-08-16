# import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Configuracao do smtp de saida do email
port = 587
smtp_server = "INSERT SMTP ADDRESS"
login = "INSERT EMAIL ADDRESS"
password = "INSERT PASSWORD" 

# Leitura do arquivo html
with open('EMAIL_HTML_FILE', 'rb') as file:
    file_content = file.read().decode('utf-8', 'ignore')

with open('EMAIL_ATTACHMENT', 'rb') as file:
    attachment = file.read()
    
    
emailRemetente = "EMAIL SENDER"
emailDestinatario = "EMAIL DESTINATION"
emailCopiaOculta = ["LIST EMAIL HIDDEN ADDRESSES"]
# Composicao do cabecalho do e-mail
message = MIMEMultipart("alternative")
message["Subject"] = "INSERT SUBJECT"
message["From"] = emailRemetente
message["To"] = emailDestinatario
message["Bcc"] = ', '.join(emailCopiaOculta)


part1 = MIMEText(file_content, 'html')
message.attach(part1)

# Envio do e-mail
with smtplib.SMTP("SMTP ADDRESS", 587) as server:
    server.login(login, password)
    server.sendmail(emailRemetente, emailCopiaOculta, message.as_string())

print('enviado')