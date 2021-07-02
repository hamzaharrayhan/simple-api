from flask import Flask, jsonify, request, make_response
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'superkey'


@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        req_json = request.json
        username = req_json['username']
        password = req_json['password']

        if username == 'aku' and password == 'rahasia':
            return jsonify({"message": "success", "data": {"username": username, "hobby": "makan"}})
        else:
            return jsonify({"message": "fail"})


if __name__ == '__main__':
    app.run(debug=True)
