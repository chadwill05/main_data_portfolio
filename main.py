from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

#import os
#
app = Flask(__name__)
#app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
#ckeditor = CKEditor(app)
#Bootstrap5(app)
#
#
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///projects.db")
#db = SQLAlchemy()
#db.init_app(app)
#
#with app.app_context():
#    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/resume')
def resume():
   return render_template('resume.html')

@app.route('/projects')
def projects():
  return render_template('projects.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/tableau-projects')
def tableau_projects():
   return render_template('tableau-projects.html')

@app.route('/data-projects')
def data_projects():
   return render_template('data-projects.html')

@app.route('/python-projects')
def python_projects():
   return render_template('python-projects.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)