from flask import Flask, render_template, request, session
import requests
import json
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generates a random secret key

@app.route('/')
def index():
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('index.html', result=session['chat_history'])

@app.route('/parse', methods=['POST'])
	# 2.Result Variable: In your route handling this request (the /parse route), 
    # you’re generating or updating the result variable
def extract():
    text = str(request.form.get('value1'))
    payload = json.dumps({"sender": "Rasa", "message": text})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post("http://localhost:5005/webhooks/rest/webhook", headers=headers, data=payload)
    response = response.json()
    
    # Append user message and bot response to chat history
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    session['chat_history'].append(f"User: {text}")
    for message in response:
        session['chat_history'].append(f"Bot: {message.get('text', '')}")

    return render_template('index.html', result=session['chat_history'])

if __name__ == '__main__':
    app.run(debug=True)