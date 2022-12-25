from Utils import *
from flask import Flask

app = Flask(__name__)


@app.route('/')
def score_server():
    score_file = open(SCORES_FILE_NAME, 'r').read()
    # with score_file:
    #     final_score = score_file.readline()
    message = f"""
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">{score_file}</div></h1>
        </body>
    </html>"""
    print(f'This is your Final Score: {score_file}')

    return message


app.run(debug=True)
