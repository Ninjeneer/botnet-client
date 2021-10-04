from email.mime.text import MIMEText
import smtplib

fromaddr = "ensicaen.securite.2021@gmail.com"
toaddr = "lemazier.elise@gmail.com"

html = open("page_mail.html")
msg = MIMEText(html.read(), 'html')
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Mise à jour sécurité Firefox"

debug = False
if debug:
    print(msg.as_string())
else:
    server = smtplib.SMTP('http://localhost',8080)
    server.starttls()
    server.login("ensicaen.securite.2021@gmail.com", "Ensicaen.2021@")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()