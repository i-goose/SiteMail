from flask import render_template, session
from .. import db
from ..models import Caption
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    all_captions = Caption.query.all()
    return render_template('index.html', all_captions=all_captions)
