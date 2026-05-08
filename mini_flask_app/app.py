from flask import Flask, render_template

app = Flask(__name__)

#Index route - music 
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

#Film route
@app.route("/films", methods=['GET'])
def films():
    return render_template("films.html")


# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)