from flask import Flask, render_template, request, jsonify
# Location of the messages
messages_txt = "messages.txt"

app = Flask(__name__)

def get_message_count():
    return sum(1 for line in open(messages_txt))


@app.route("/")#, methods=["POST", "GET"])
def home():
    return render_template("ui.html", message_count = get_message_count()-1)


@app.route("/get_new_messages/<n>")
def get_new_messages(n):
    n = int(n)
    # Get all the messages that are on lines n + 1 to the end
    with open(messages_txt) as f:
        lines = [line.rstrip() for line in f]

    n_messages = len(lines)
    return jsonify({"count": n_messages, "messages": lines[n:n_messages]})


@app.route("/save_message", methods=["POST"])
def save_message():
    # Save a message to messages.txt
    with open(messages_txt, "a") as fo:
        fo.write(request.form["message"] + "\n")
    return str(0)

if __name__ == "__main__":
    app.run(debug=True)