

from flask import Flask, request, jsonify, send_from_directory
import praw

app = Flask(__name__)

# Reddit API credentials
reddit = praw.Reddit(

    client_id='R6RzOd5oHlgTnAxrdt4FrA',
    client_secret='FST0qJX51u2KY9NCvWCG4mxQw4s8Jw',
    username='Guilty_Floor9214',
    password='NoorAlden1',
    user_agent='web:com.example.myredditapp:v1.0 (by /u/Guilty_Floor9214)'
)

@app.route('/post_to_reddit', methods=['POST'])
def post_to_reddit():
    data = request.get_json()
    title = data.get('title')
    thread_text = data.get('threadText')

    try:
        subreddit = reddit.subreddit('AllHayganeen')


        flair_id = data.get('flair')
        subreddit.submit(title, selftext=thread_text, flair_id=flair_id)
        return jsonify({'success': True, 'message': 'Thread posted successfully!'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})


@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

