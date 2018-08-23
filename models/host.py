from db import db

class Host(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(9), unique=True)
    reserved = db.Column(db.String)

    def __init__(self, hostname, reserved):
        self.hostname = hostname
        self.reserved = reserved

    def json(self):
        return {'Hostname': self.hostname, 'Reserved': self.reserved}

    @classmethod
    def find_by_hostname(cls, hostname):
        return Host.query.filter_by(hostname=hostname).first()

    @classmethod
    def find_all(cls):
        return Host.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()