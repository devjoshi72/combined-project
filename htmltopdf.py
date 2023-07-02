from flask import Flask,render_template,make_response
import pdfkit
import os
app=Flask(__name__)

@app.route("/")
def index():
    name=""
    html = render_template("pdf.html",name=name)
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdf=pdfkit.from_string(html, False, configuration=config)
    response=make_response(pdf)
    response.headers["Content-Type"]="application/pdf"
    response.headers['Content-Disposition']='inline;' \
                                            'filename=certificate.pdf'   #inline-for view pdf mode  /attachment-for download pdf
    return response

if __name__ =='__main__':
    app.run(debug=True)