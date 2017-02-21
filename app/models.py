# -*- coding: utf-8 -*-
from app import db

class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    cityname = db.Column(db.String(40))
    ip = db.Column(db.String(40))
    time = db.Column(db.String(40))
    location = db.Column(db.String(40))
    api = db.Column(db.String(40))
    weather = db.Column(db.String(20))
    weathercode = db.Column(db.String(10))
    tempunit = db.Column(db.String(10))
    tempmin = db.Column(db.Float)
    tempmax = db.Column(db.Float)

    def __init__(self):
        pass

    def __repr__(self):
        return '%s(%r %r %r %r %r)' %(self.__class__.__name__, self.time, self.ip, self.location, self.cityname, self.weather)

