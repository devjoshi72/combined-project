from flask import Flask,render_template,make_response
import pdfkit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr = "info.qubisttech@gmail.com"
password = "zrqrbjgqzoedpfvk"
import os
app=Flask(__name__)


@app.route("/")
def index():
    name=""
    type=2
    email="deepakjoshiuk.in@gmail.com"
    return render_template("slow.html",name=name)
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdf=pdfkit.from_string(html, False, configuration=config)
    if type==1:
        response=make_response(pdf)
        response.headers["Content-Type"]="application/pdf"
        response.headers['Content-Disposition']='inline;' \
                                            'filename=certificate.pdf' #inline-for view pdf mode  /attachment-for download pdf
        return response
    elif type==2:
      sendEmail(email,pdf)

    else:
        render_template(404)


def sendEmail(toaddr,file):

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "hii this is mail"

    # string to store the body of the mail
    body = "Body_of_the_mail"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = "attachments name with file extention eg. .jpg"
    attachment = open(file, "rb")

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
    server.login(fromaddr, password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    server.send_message(msg)

    server.quit()
    print("Email Send sucessfilly")



if __name__ =='__main__':
    app.run(debug=True)