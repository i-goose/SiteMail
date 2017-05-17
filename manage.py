#!/usr/bin/env python
import os
from news import create_app, db
from news.models import Source, Caption
from flask_script import Manager, Shell

#That is start file for program initialization
news = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(news)

#This makes next names available in shell mode
def make_shell_context():
    return dict(news=news, db=db, Source=Source, Caption=Caption)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
