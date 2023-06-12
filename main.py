import random
from flask import Flask, render_template, request

app = Flask(__name__)

words = []
dictionary = []
hidden_word = ''


@app.route('/', methods=['GET', 'POST'])
def check_word():
    global words
    global dictionary
    global hidden_word
    message = ''

    if not dictionary:
        with open('pl_PL.dic', 'r', encoding='windows-1250') as file:
            dictionary = [word.strip().lower().split('/')[0] for word in file.readlines() if
                          len(word.strip().split('/')[0]) >= 5]
            hidden_word = random.choice(dictionary)
            words.append(hidden_word)
            print(hidden_word)

    if request.method == 'POST':
        user_word = request.form.get('word').lower()
        if user_word == hidden_word:
            message = 'Gratulacje, zgadłeś słowo!'
        elif user_word in dictionary:
            words.append(user_word)
            words.sort()
            message = 'Słowo zostało dodane.'
        else:
            message = 'Słowo nie znajduje się w słowniku.'

    words_display = words.copy()
    if hidden_word in words_display:
        words_display[words_display.index(hidden_word)] = ' '

    return render_template('index.html', words=words_display, message=message)


if __name__ == "__main__":
    app.run(debug=True)
