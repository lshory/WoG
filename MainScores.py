from Utils import *
from flask import Flask

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        score_file = open(SCORES_FILE_NAME, 'r').read()
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
    except BaseException:
        message = f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
            <body>
                <h1><div id="score" style="color:red">{BAD_RETURN_CODE}</div></h1>
            </body>
        </html>"""


app.run(debug=True)
