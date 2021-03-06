""" A Rock Paper Scissors webapp with Python as the backend """
from flask import Flask, render_template, request, redirect, url_for
from logic import computerChoice, play, options

app = Flask(__name__)


@app.route('/')  # route for the main page
def index():
    return render_template('index.html', options=options)


@app.route('/play', methods=['POST'])
def playFrontend():
    # get player selection
    player = request.form['game-option']
    # generate computer selection
    computer = computerChoice()

    # calculate outcome
    outcome = play(computer, player)

    return render_template('index.html', options=options, outcome=outcome, player=player, computer=computer)


if __name__ == '__main__':
    app.run(debug=False)
