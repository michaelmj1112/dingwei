# (A) INIT
# (A1) LOAD REQUIRED PACKAGES
from flask import Flask, render_template, request, make_response
from werkzeug.datastructures import ImmutableMultiDict
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# (A2) FLASK INIT
app = Flask(__name__)
app.debug = True

# (B) SETTINGS
HOST_NAME = "0.0.0.0"
HOST_PORT = 8080
MAIL_FROM = "sys@site.com"
MAIL_TO = "admin@site.com"
MAIL_SUBJECT = "Booking Request"

# (C) ROUTES
# (C1) BOOKING PAGE
@app.route("/")
def index():
  return render_template("1-booking.html")

# (C2) THANK YOU PAGE
@app.route("/thank")
def thank():
  return render_template("2-thank.html")

# (C3) BOOKING ENDPOINT
@app.route("/book", methods=["POST"])
def foo():
  # EMAIL HEADERS
  mail = MIMEMultipart("alternative")
  mail["Subject"] = MAIL_SUBJECT
  mail["From"] = MAIL_FROM
  mail["To"] = MAIL_TO

  # EMAIL BODY (BOOKING DATA)
  data = dict(request.form)
  msg = "<html><head></head><body>"
  for key, value in data.items():
    msg += key + " : " + value + "<br>"
  msg += "</body></html>"
  mail.attach(MIMEText(msg, "html"))

  # SEND MAIL
  mailer = smtplib.SMTP("localhost")
  mailer.sendmail(MAIL_FROM, MAIL_TO, mail.as_string())
  mailer.quit()

  # HTTP RESPONSE
  res = make_response("OK", 200)
  return res

# (D) START!
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)
