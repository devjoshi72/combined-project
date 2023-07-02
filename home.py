from flask import Flask,render_template,make_response
import pdfkit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

app = Flask(__name__)

#for smtp

#for certificate
@app.route("/welcomee")
def welcomee():
    return render_template("pj.html", param=0)


@app.route("/list   ", methods=["GET", "POST"])
def list():
    if request.method == "POST":

        name = {"Name": request.form["Name"],
                "Grade": request.form["Grade"],
                "Date": request.form["Date"],
                "Course": request.form["Course"],
                "Duration": request.form["Duration"]}
        return render_template("pj.html", param=name)
    else:
        return render_template("list.html")


#certification project

@app.route('/certification_project', methods=["get", "post"])
def certification_project():
    try:

        if request.method == "POST":



            type =int( request.form["rdbCreate"])
            email = request.form["email"]
            name = {"Name": request.form["name"],
                    "Grade": request.form["grade"],
                    "Date": request.form["date"],
                    "Course": request.form["workshop"],
                    "Duration":"2months"}

            return render_template("pj.html", param=name)
            option={'enable-local-file-access':None}
            config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
            pdf = pdfkit.from_string(html, False, configuration=config,options=option)
            if type == 1:
                response = make_response(pdf)
                response.headers["Content-Type"] = "application/pdf"
                response.headers['Content-Disposition'] = 'inline;' \
                                                          'filename=certificate.pdf'  # inline-for view pdf mode  /attachment-for download pdf

                return response
            elif type == 2:
                sendEmail(email, pdf)
                return render_template("certification_project.html", param=0)

            else:
                render_template(404)
        else:
            return render_template("certification_project.html", param=0)
    except IndexError:
        os.abort(404)

#for pdf
fromaddr = "info.qubisttech@gmail.com"
password = "zrqrbjgqzoedpfvk"

@app.route("/")
def index():
    name=""
    type=2
    email="deepakjoshiuk.in@gmail.com"
    html=render_template("pj.html",name=name)
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
   app.run(debug=True, port=4000)