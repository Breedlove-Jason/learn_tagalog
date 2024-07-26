import pandas as pd
from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed to keep data in session variables


@app.route('/')
def index():
    if 'current_index' not in session:
        session['current_index'] = 0
        session['known_words'] = []
    translations = load_translations()
    current_word = translations[session['current_index']]
    return render_template('index.html', word=current_word)


@app.route('/next/<known>')
def next_word(known):
    translations = load_translations()
    if known == 'true':
        session['known_words'].append(translations[session['current_index']]['Tagalog'])
    session['current_index'] += 1
    if session['current_index'] >= len(translations):
        return render_template('complete.html', known_words=session['known_words'])
    return redirect(url_for('index'))


def load_translations():
    df = pd.read_csv('data/translations.csv')
    return df.to_dict(orient='records')


if __name__ == '__main__':
    app.run(debug=True)
