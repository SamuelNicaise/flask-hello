from flask import Flask, jsonify
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def index():
    # return render_template("index.html", **{"greeting": "Hello from Flask!"})
    return jsonify("Hello from Flask!")


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4285)
