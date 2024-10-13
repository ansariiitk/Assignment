from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is Ansar from IIITK and the Reg.no is 2024PHD21006"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)