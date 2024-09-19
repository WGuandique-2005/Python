"""
* Programacion Computacional III - Semana 9
! Gestion de correos
"""

#? Importar la biblioteca smtplib para enviar correos
#todo\ contraseña: ibfl pewk fqua vzks

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = "smtp.gmail.com"
port = 587
email = "wguandiquerivera07@gmail.com"
password = "ibfl pewk fqua vzks"

try:
    conn = smtplib.SMTP(server,port)
    # print(conn.ehlo())
    conn.starttls()
    # print(conn.login(email,password))
    conn.login(email,password)
    message = MIMEMultipart()
    message ["From"] = email
    message["To"] = "alfredomedrano678@gmail.com"
    message["Subject"] = "Ganas de joder"
    body = "XD"
    message.attach(MIMEText(body))
    conn.sendmail(email,email,message.as_string())
except smtplib.SMTPResponseException as e:
    print(f"Hay un error: {e}")
finally:
    conn.quit()

"""
for i in range(1,100): 
    conn.sendmail(email,"alfredomedrano678@gmail.com", "Importante: Mensaje prueba \n\n"+
                "Hola")
"""