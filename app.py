from flask import Flask

app = Flask(__name__)


@app.route("/",methods =['GET','POST'])
def index():
    return "Hi folks , Myself Roodra I AM COMING TO MAKE YOU BLOW AWAY"

if __name__=="__main__":
    app.run(debug=True)
