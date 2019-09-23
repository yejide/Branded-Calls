from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, Say, Play


app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.say('Hello, How are you doing', voice='alice')
    resp.play('https://demo.twilio.com/docs/classic.mp3')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
