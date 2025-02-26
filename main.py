from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    # Host is set to 0.0.0.0 to allow external access.
    app.run(host="0.0.0.0", port=5000)
