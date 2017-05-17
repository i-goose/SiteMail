from . import db


class Source(db.Model):
    __tablename__ = 'sources'
    id = db.Column(db.Integer, primary_key=True)
    s_name = db.Column(db.String(64), unique=True)
    s_logo = db.Column(db.String(128), unique=True)
    s_link = db.Column(db.String(64), unique=True)
    
    captions = db.relationship('Caption', backref='source', lazy='dynamic')

    def __repr__(self):
        return '<Source %r>' % self.s_name


class Caption(db.Model):
    __tablename__ = 'captions'
    id = db.Column(db.Integer, primary_key=True)
    c_link = db.Column(db.String(256), unique=True, index=True)
    c_topic = db.Column(db.Text)
    c_text = db.Column(db.Text)
    c_time = db.Column(db.DateTime)
    
    source_id = db.Column(db.Integer, db.ForeignKey('sources.id'))

    def __repr__(self):
        return '<Caption %r>' % self.c_topic
