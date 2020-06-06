""" A Rock Paper Scissors webapp with Python as the backend """
from flask import Flask, render_template, request, redirect, url_for
from logic import computerChoice, play, options

app = Flask(__name__)


@app.route('/')  # route for the main page
def index():
    return render_template('index2.html', options=options)


@app.route('/play', methods=['POST'])
def playFrontend():
    player = request.form['game-option']
    computer = computerChoice()
    outcome = play(computer, player)
    return render_template('index2.html', options=options, outcome=outcome, player=player, computer=computer)


if __name__ == '__main__':
    app.run(debug=True)

# print(play(computerChoice(), player))
