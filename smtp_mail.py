import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('info.qubisttech@gmail.com','zrqrbjgqzoedpfvk')
server.sendmail('info.qubisttech@gmail.com',
                'deepakjoshiuk.in@gmail.com',
                "Hi This is Python Testing Mail"
                )
print("Email Send sucessfilly")


