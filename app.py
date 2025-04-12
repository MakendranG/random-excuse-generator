import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_excuse', methods=['GET'])
def get_excuse():
    # Fetch a random excuse from the Excuser API
    response = requests.get("https://excuser.herokuapp.com/v1/excuse")
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch excuse"}), 500

    data = response.json()
    return jsonify({"excuse": data[0]['excuse']})

if __name__ == '__main__':
    app.run(debug=True)
