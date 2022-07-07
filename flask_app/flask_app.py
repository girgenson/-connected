import os
import pprint
from datetime import datetime

from flask import Flask, render_template, request, session, redirect, url_for, flash, Response
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_moment import Moment


from find_degrees import find_degrees
from db import entries, type_of_entries

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, widgets, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FL_CONN_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite3')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

Bootstrap(app)
moment = Moment(app)


migrate = Migrate(app, db)

#
# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User', backref='role', lazy='dynamic')
#
#     def __repr__(self):
#         return f'<Role {self.name}>'
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#     role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
#
#     def __repr__(self):
#         return f'<User {self.username}>'


entry_category = db.Table('association', db.Model.metadata,
                          db.Column('Entry_id', db.Integer, db.ForeignKey('Entry.id')),
                          db.Column('Category_id', db.Integer, db.ForeignKey('Category.id'))
                          )


class Entry(db.Model):
    __tablename__ = 'Entry'
    id = db.Column(db.Integer, unique=True, index=True, primary_key=True)
    title = db.Column(db.String(255), unique=True, index=True)
    content = db.Column(db.String)
    category = db.relationship('Category', secondary=entry_category)

    # editor == ...

    def __repr__(self):
        return f'<Entry id: {self.id} title: {self.title}, content: {self.content}, ' \
               f'categories: {", ".join([i.title for i in Entry.query.all()])}>'


class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, unique=True, index=True, primary_key=True)
    title = db.Column(db.String(255), unique=True, index=True)

    def __repr__(self):
        return f'<Category id: {self.id} title: {self.title}>'


# class Alias(db.Model):
#     id = db.Column(db.Integer, unique=True, index=True, primary_key=True)
#     title = db.Column(db.String(255), unique=True, index=True)
#     entry_id = db.Column(db.Integer, db.ForeignKey('entries.id'))


# class TypesOfEntries(db.Model):
#     id = db.Column(db.Integer, unique=True, index=True, primary_key=True)
#     title = db.Column(db.String(255), unique=True, index=True)


class NameForm(FlaskForm):
    entry_1 = StringField('First entry', validators=[DataRequired()])
    entry_2 = StringField('Second entry', validators=[DataRequired()])
    submit = SubmitField('Find connection')


class AddEntryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    # choices = list(enumerate([i.capitalize() for i in type_of_entries.values()]))
    # select_multiple_field = SelectMultipleField('Type', choices=[('', '')] + choices,
    #                                             option_widget=widgets.CheckboxInput())
    content = StringField('Content')
    category = SelectMultipleField('Category', choices=[i.title for i in Category.query.all()], option_widget=widgets.CheckboxInput())
    submit = SubmitField('Add')


class AddCategoryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Add')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        start = form.entry_1.data
        end = form.entry_2.data
        path = find_degrees(start, end, entries)
        session['entry_1'] = start
        session['entry_2'] = end
        session['path'] = path
        if session['path'] is not None:
            session['arrowed_path'] = '<b> -> </b>'.join(path)
        else:
            session['arrowed_path'] = f'There is no connection between {start} and {end}'
        return render_template('how_connected_result.html')
    return render_template('home.html', form=form)


@app.route('/add_entry', methods=['GET', 'POST'])
def add_entry():
    form = AddEntryForm()
    if form.validate_on_submit():
        title, content, alias = request.form.get('title'), request.form.get('content'), request.form.get('alias')
        # if Entry.query.filter_by(title=title).all():
        #     flash('This title already exists')
        #     form.title.data = ''
        #     return render_template('add_entry.html', form=form)
        entry = Entry(title=title, content=content)
        db.session.add(entry)
        db.session.commit()
        session['entry_id'] = Entry.query.filter_by(title=title).all()[0].id
        return redirect(f'added_entry/{session.get("entry_id")}')
    return render_template('add_entry.html', form=form)


@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    form = AddCategoryForm()
    if form.validate_on_submit():
        title = request.form.get('title')
        if Category.query.filter_by(title=title).all():
            flash('This category already exists')
            form.title.data = ''
            return render_template('add_category.html', form=form)
        category = Category(title=title)
        db.session.add(category)
        db.session.commit()
        return redirect('all_categories')
    return render_template('add_category.html', form=form)


@app.route('/all_categories')
def all_categories():
    _all_categories = Category.query.all()
    return render_template('all_categories.html', _all_categories=_all_categories)


@app.route('/added_entry/<entry_id>')
def added_entry(entry_id):
    return render_template('added_entry.html', db=db, Entry=Entry, session=session, entry_id=entry_id)


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
