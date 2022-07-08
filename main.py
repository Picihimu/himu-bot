from flask import Flask, render_template, request
from threading import Timer
import webbrowser
import requests
import json
import uuid
import os

app = Flask(__name__)
myBid = "162594"  # This value can be changed to use your own bot
myKey = "HfLCrXnUDD9vjUpz"  # This value can be changed to use your own bot


# define app routes
@app.route("/")
def index():
    return render_template("index.html")


def open_browser():
    webbrowser.open_new('http://127.0.0.1:2000/')


def serial_num():
    var = str(uuid.uuid1(uuid.getnode(), 0))[24:]
    try:
        username = os.getlogin()
    except Exception as e:
        print(e)
        print("Unable to get username")
        username = "Unknown User"
    var = var + "+" + username
    print(var)
    return var


@app.route("/get")
# function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    answer = give_answer(userText)
    return str(answer)


def give_answer(givenText):
    uid = serial_num()
    url = "http://api.brainshop.ai/get?bid=" + myBid + "&key=" + myKey + "&uid=" + uid + "&msg=" + givenText
    response = requests.get(url)
    parsed = json.loads(response.text)['cnt']
    print(parsed)
    return parsed


if __name__ == "__main__":
    print(serial_num())
    Timer(1, open_browser).start();
    app.run(port=2000)
