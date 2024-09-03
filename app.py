from flask import Flask, request, jsonify, render_template
from database import get_db
from social_media import fetch_twitter_data, fetch_facebook_data
from sentiment_analysis import analyze_sentiment
from trend_detection import detect_trends

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/collect_data', methods=['POST'])
def collect_data():
    platform = request.json.get('platform')
    if platform == 'twitter':
        data = fetch_twitter_data()
    elif platform == 'facebook':
        data = fetch_facebook_data()
    else: 
        return jsonify({'error': 'Unsupported platform'}), 400

    # Analyze sentiment
    sentiments = [analyze_sentiment(post['text']) for post in data]

    # Detect trends
    trends = detect_trends(data)

    # Store data in MongoDB
    db = get_db()
    collection = db['social_data']
    collection.insert_many(data)

    return jsonify({
        'status': 'Data collected',
        'sentiments': sentiments,
        'trends': trends
    })

if __name__ == '__main__':
    app.run(debug=True)








