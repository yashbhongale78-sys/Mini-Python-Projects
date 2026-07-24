from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks = {
        "man" : 43,
        "cat" : 46,
        "dog" : 55 
    }
    return jsonify(marks)

app.run(debug=True)