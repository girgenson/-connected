import os
import pprint
from datetime import datetime

from flask import Flask, render_template, request, session, redirect, url_for, flash, Response, abort
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_moment import Moment

from find_degrees import find_degrees
from db import entries

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, widgets, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['TESTING'] = True
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


entry_category = db.Table('entry_category',
                      db.Column('entry_id', db.Integer, db.ForeignKey('entry.id')),
                      db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
                      )


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, index=True)

    def __repr__(self):
        return f'<Category id: {self.id} title: {self.title}>'


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, index=True)
    content = db.Column(db.Text)
    categories = db.relationship('Category', secondary=entry_category, backref='entries')

    # author = ...
    # editor = ...

    def __repr__(self):
        return f'<Entry id: {self.id} title: {self.title}, content: {self.content}, ' \
               f'categories: {[i for i in self.categories]}>'


# class Alias(db.Model):
#     id = db.Column(db.Integer, unique=True, index=True, primary_key=True)
#     title = db.Column(db.String(255), unique=True, index=True)
#     entry_id = db.Column(db.Integer, db.ForeignKey('entries.id'))


# class TypesOfEntries(db.Model):
#     id = db.Column(db.Integer, unique=True, index=True, primary_key=True)
#     title = db.Column(db.String(255), unique=True, index=True)


class EntriesToFindConnection(FlaskForm):
    entry_1 = StringField('First entry', validators=[DataRequired()])
    entry_2 = StringField('Second entry', validators=[DataRequired()])
    submit = SubmitField('Find connection')


class EntryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content')
    # categories = SelectMultipleField('Category', choices=Category.query.all())
    categories = SelectMultipleField('Category', choices=[i.title for i in Category.query.all()])
    submit = SubmitField('Add')


class CategoryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Add')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = EntriesToFindConnection()
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
    form = EntryForm()
    if form.validate_on_submit():
        title = request.form.get('title')
        content = request.form.get('content')

        #categories = request.form.get('categories')
        categories_from_form = request.form.getlist('categories')
        print('categories_from_form', categories_from_form)
        # categories = [Category(title=title) for title in categories_from_form]
        print('title', title)
        print('content', content)
        categories = []
        for i in categories_from_form:
            print('type(i)', type(i))
            print(i)
            print('Category.query.filter_by(title=i).first()', Category.query.filter_by(title=i).first())
            categories.append(Category.query.filter_by(title=i).first())
        print("CATEGORIESSSS", categories)
        print('time', datetime.utcnow())
        # TODO: check if there is same title
        # if Entry.query.filter_by(title=title).all():
        #     flash('This title already exists')
        #     form.title.data = ''
        #     return render_template('add_entry.html', form=form)
        entry = Entry(title=title, content=content, categories=categories)
        # if categories:
        #     entry.categories = categories
        db.session.add(entry)
        db.session.commit()
        session['entry_id'] = Entry.query.filter_by(title=title).all()[0].id

        return redirect(f'entries/{session.get("entry_id")}')
    return render_template('add_entry.html', form=form)


@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        title = request.form.get('title')
        category = Category(title=title)
        db.session.add(category)
        db.session.commit()
        return redirect('categories')
    return render_template('add_category.html', form=form)


@app.route('/entries')
def all_entries():
    return render_template('entries.html', _all_entries=Entry.query.all())


@app.route('/categories')
def all_categories():
    return render_template('categories.html', _all_categories=Category.query.all(), cats_list_type=[type(i) for i in Category.query.all()])


@app.route('/entries/<int:entry_id>')
def entry_page(entry_id):
    try:
        entry = Entry.query.filter_by(id=entry_id).all()[0]
        _categories = [i.title for i in entry.categories]
    except IndexError:
        return abort(404)
    return render_template('entry_page.html', db=db, entry=entry, session=session, _categories=_categories)


@app.route('/entries/<int:entry_id>/edit', methods=['GET', 'POST'])
def edit_entry(entry_id):
    form = EntryForm()
    entry = Entry.query.filter_by(id=entry_id).first_or_404()

    try:
        if request.method == "POST":
            form.title = request.form['title']
            form.content = request.form['content']
            form.links = request.form['links']
            form.categories = request.form['categories']
            try:
                db.session.commit()
                flash('Edited successfully')
                return render_template('update_entry.html', form=form, etnry=entry)
            except:
                flash('Error. Try again')
                return render_template('update_entry.html', form=form, etnry=entry)
    except IndexError:
        return abort(404)

    return render_template('entry_page.html', db=db, entry=entry, session=session)



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
    app.run(debug=True, port=2)

# TODO: add dates in entries
