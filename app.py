from flask import Flask, render_template, jsonify
import time
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['GET'])
def process():
    time.sleep(2)  # Simulating processing time
    return jsonify({'message': 'Process Complete!'})


@app.route('/secondProcess', methods=['GET'])
def second_process():
    time.sleep(2)
    
    return jsonify({'value': str(datetime.datetime.now())})


if __name__ == '__main__':
    app.run(debug=True)
