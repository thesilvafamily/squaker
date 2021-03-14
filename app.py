from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        return request.form["message"]
    else:
        return render_template("ui.html")

if __name__ == "__main__":
    app.run(debug=True)