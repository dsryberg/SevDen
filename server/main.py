from flask import Flask, render_template, request, redirect
from datetime import datetime
import os

app = Flask("__main__")

#################################################
## Index page
@app.route("/")
def index():
    return render_template("index.html", date=datetime.now())

#################################################
## CV/Resume
@app.route("/cv")
def cv_pdf(): return redirect("/static/files/david_severin_ryberg_cv.pdf")
@app.route("/resume")
def cv_pdf2(): return redirect("https://www.dropbox.com/s/xs794rzznemqtl2/David_Ryberg_resume.docx?dl=0")

#################################################
## Just for funsies
from hooks import sandbox
app.route("/jspg")(sandbox.javascript_playground(app, request))


#################################################
## Start the server
## 
## * set the WEBSERVER_PRODUCTION environment vairable to 1 in order
##   to trigger the server to start in production mode (as in, being
##   being served by uWSGI and nginx), otherwise it will just use the 
##   built-in server (which is not intended for use beyond debugging)
if __name__ == "__main__":
    if not os.environ.get("WEBSERVER_PRODUCTION", 0)==1:
        app.run()
