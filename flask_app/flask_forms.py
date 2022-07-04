import os
from datetime import datetime

from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from find_degrees import find_degrees
from db import entries

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FL_CONN_SECRET_KEY')

Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    entry_1 = StringField('First entry', validators=[InputRequired()])
    entry_2 = StringField('Second entry', validators=[InputRequired()])
    submit = SubmitField('Find connection')


@app.route('/form_2', methods=['GET', 'POST'])
def form_2():
    form = NameForm()
    if form.validate_on_submit():
        session['entry_1'] = form.entry_1.data
        session['entry_2'] = form.entry_2.data
        session['path'] = find_degrees(session['entry_1'], session['entry_2'], entries)
        return redirect(url_for('form_2'))
    return render_template('form_2.html', form=form, entry_1=session.get('entry_1'), entry_2=session.get('entry_2'),
                           path=session.get('path'))


@app.route('/home', methods=['GET', 'POST'])
@app.route('/')
def home():
    flash('Test alert')
    return render_template('home.html', current_time=datetime.utcnow())


@app.route("/~connected", methods=['POST'])
def search_connection():
    start = request.form.get('first_element')
    end = request.form.get('second_element')
    path = None
    if start and end:
        path = find_degrees(start, end, entries)
        if path is not None:
            print(path)
            arrowed_path = '<b> -> </b>'.join(path)
        else:
            arrowed_path = f'There is no connection between {start} and {end}'
    else:
        arrowed_path = ''

    return render_template(
        'result.html', path=path, arrowed_path=arrowed_path, start=start, end=end)


@app.errorhandler(405)
def page_not_found(_error):
    return render_template('405.html'), 405


@app.errorhandler(404)
def page_not_found(_error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def initial_server_error(_error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True, port=-2)
