from flask import Flask, render_template

#create app
app = Flask(__name__)

#home site
@app.route("/")
def home():
    return render_template("home.html")

#run it
if __name__ == "__main__":
    app.run(debug=True)