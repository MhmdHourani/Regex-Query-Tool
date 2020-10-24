from flask import Flask, render_template, request, jsonify
from regexQuery import regex_query

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/result', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        query = request.form['regex']
        text = request.form['test_str']
        result = regex_query(query, text)
        inputy = ([], [])
        if result == inputy:
            return 'There is no matching between your text and query'
        else:
            return jsonify(regex_query(query, text))
    else:
        return "This is the submit page mothe GET"


if __name__ == "__main__":
    app.run(debug=True)
