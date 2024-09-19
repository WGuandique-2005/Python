"""
* Programacion Computacional III - Semana 9
! Gestion de correos
"""

#? Importar la biblioteca smtplib para enviar correos
#todo\ contraseña: ibfl pewk fqua vzks

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.encoders import encode_base64

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
    message["To"] = "jimmyrivas568@gmail.com"
    message["Subject"] = "Ganas de joder"
    body = "XD"
    html ="""
    <html>
        <body>
            <h1>Hola</h1>
        </body>
    </html>
    """
    message.attach(MIMEText(html, 'html'))
    conn.sendmail(email,"jimmyrivas568@gmail.com",message.as_string())
    
except smtplib.SMTPResponseException as e:
    print(f"Hay un error: {e}")
finally:
    conn.quit()

"""
for i in range(1,100): 
    conn.sendmail(email,"alfredomedrano678@gmail.com", "Importante: Mensaje prueba \n\n"+
                "Hola")
"""