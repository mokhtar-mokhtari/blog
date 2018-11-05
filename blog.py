import datetime
import os
import markdown
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect, url_for, abort, Blueprint
from markupsafe import Markup

#app = Flask(__name__)


BASE_DIR_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/data/')



# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, url_for
# )
# from werkzeug.exceptions import abort
#
# from flaskr.auth import login_required
# from flaskr.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/home')
def home():
    return redirect(url_for('index'))


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/posts/')
def posts():
    posts = []

    list_file = os.listdir('data')

    for file in list_file:
        filename = os.path.join(BASE_DIR_DATA + file)
        dt = os.path.getctime(filename)
        date = datetime.datetime.fromtimestamp(dt)
        link = file.split('.')[0]
        title = link.replace('-', ' ')

        f = open(filename, 'r', encoding='UTF-8')
        fileString = f.read()
        text_detail = markdown.markdown(fileString)

        extract = BeautifulSoup(text_detail, "html.parser").find('p').text
        posts.append({ 'title': title, 'date': date, 'link': link, 'extract': extract })


    posts.sort(key=lambda item:item['date'], reverse=True)


    return render_template('posts.html', posts=posts)


@bp.route('/posts/<title>')
def post_detail(title=None):
    filename = 'data/' + title + '.md'
    try:
        f = open(filename, 'r', encoding='UTF-8')
    except FileNotFoundError:
        abort(404)
        #return render_template('404.html'), 404

    dt = os.path.getctime(filename)
    date = datetime.datetime.fromtimestamp(dt)
    fileString = f.read()
    text_detail = markdown.markdown(fileString)
    post_detail = Markup(text_detail)

    return render_template('post_detail.html', text=post_detail, date=date)


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/contact')
def contact():
    return render_template('contact.html')


@bp.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# if __name__ == '__main__':
#     app.run()
