from flask import Flask, jsonify


app = Flask(__name__)

data = [
        {
            "id": 1,
            "frameworks": "Django",
            "year": 2005
        },
        {
            "id": 2,
            "frameworks": "Flask",
            "year": 2010
        },
        {
            "id": 3,
            "frameworks": "Web2Py",
            "year": 2007
        }
    ]


@app.route('/')
def home():
    return "Hello World"


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)  # Return web frameworks information


if __name__ == "__main__":
    app.run(debug=True)