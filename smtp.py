import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "info.qubisttech@gmail.com"
password = "irbxbycdtxndvhlu"
toaddr = "deepakjoshiuk.in@gmail.com"  #todo create a class



# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Mail from Qubist Tech -Course Completion Certificate"

# string to store the body of the mail
body = "Course Completion Certificate"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "certificate.pdf"   #attachments name with file extention.pdf
attachment = open("static/pdf.pdf", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())


# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr,password)

# Converts the Multipart msg into a string
text = msg.as_string()

server.send_message(msg)

server.quit()
print("Email Send sucessfilly from Qubist Tech")