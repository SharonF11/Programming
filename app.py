import flask
import smtplib

# creating the flask app object
APP = flask.Flask(__name__)


# creating the route for index page
@APP.route("/")
def index():
    return flask.render_template("index.html") # rendering index page

# creating the route for products page 
@APP.route("/products")
def products():
    return flask.render_template("products.html") # rendering products page

# creating the route for contact page
@APP.route("/contact")
def contact():
    return flask.render_template("contact.html") # rendering contact page

# connecting to SMTP service for mailing feature
fromaddr = "sgsugeeth@gmail.com"
username = "sgsugeeth@gmail.com"
password = "mrfsrtnatzhvzzzt"
server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)

# creating the route for send notification
@APP.route("/contact/send_notification", methods=["post"])
def send_notification():
    data = flask.request.get_json() # parsing data from request body
    print(data)
    msg = f"Thanks {data['name']} for contacting us, We'll get back to you as soon as possible" # creating the message
    toaddrs = data['email']
    server.sendmail(fromaddr, toaddrs, 'Subject: {}\n\n{}'.format("FIT HOUSE", msg)) # sending mail to the user email
    return "success"


if __name__ == "__main__":
    APP.debug = True
    APP.run() # starting the flask app listner
