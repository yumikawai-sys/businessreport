from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import requests
from sentiment import sentiment_analysis

app = Flask(__name__)
# CORS(app) * still seeing CORS
CORS(app, origins='http://localhost:5173')

@app.route('/summarize', methods=['GET'])
def summarize_endpoint():
    summary, emotions = get_summary_from_colab()
    return jsonify({'summary': summary, 'emotions': emotions})

def get_summary_from_colab():
    # colab_endpoint = 'https://colab.research.google.com/drive/1jKyb5vSthLoEmhaUySueKrCQof9bwdpc/summarize'
    # response = requests.get(colab_endpoint)
    # data = response.json()
    # summary = data['summary']

    # For demo....
    summary = 'I am very happy about this product.'
    emotions = sentiment_analysis(summary)

    return summary, emotions


@app.route("/")
def index():
    return "Welcome to the Business Report!"

# Run the Flask app
if __name__ == '__main__':
    app.run()