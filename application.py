from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def root():
    return render_template("index.html")

#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.run()
#------------------------------
