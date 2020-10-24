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
        if result == ([], []):
            print(result3)
        # if not any(result):
        #     # print("This is the result inside the len() and it is empty")
        #     return "Sorry there no result, try again"
        # else:
        return jsonify(regex_query(query, text))
    else:
        return "This is the submit page mothe GET"


if __name__ == "__main__":
    app.run(debug=True)
