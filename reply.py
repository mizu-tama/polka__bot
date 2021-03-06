from flask import Flask, jsonify, request
import json
import random
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    answer = "Yes, it is %s!\n" % data["keyword"]
    result = {
        "Content-Type": "application/json",
        "Answer":{"Text": answer}
    }
    # return answer
    return jsonify(result)

@app.route('/echo', methods=['POST'])
def echo():
    message = request.json.get("queryResult").get("parameters").get("game")
    response = {
        "payload": {
            "google": {
                "expectUserResponse": True,
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": message
                            }
                        }
                    ]
                }
            }
        }
    }

    return json.dumps(response)

@app.route('/startgame', methods=['POST'])
def startGame():
    game = request.json.get("queryResult").get("parameters").get("game")
    message = game + "ですね！" + getFirstPlayer() + "が先攻です"
    response = {
        "payload": {
            "google": {
                "expectUserResponse": True,
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": message
                            }
                        }
                    ]
                }
            }
        }
    }

    return jsonify(response)

def getFirstPlayer():
    players = ['わたし', 'あなた']
    return players[random.randint(0,1)]

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port,debug=True)
