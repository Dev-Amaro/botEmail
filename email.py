import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr = "seuemail@gmail.com"
toaddr = "emaildedestino@gail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = "Titulo do email"

html = """
<html>
    <body>
        <p>
            <b>Boa Noite kombatentes</b><br>
            texto do seu email
        </p>
        <a href="link(ocional)">Assita a estreia aqui!!</a>
        <p>
            <b>OBS:</b><br>
            texto do seu email
        </p>
    </body>
<html>
"""
part1 = MIMEText(html, "html")
msg.attach(part1)
s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromaddr, "senha do seu email")

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()
