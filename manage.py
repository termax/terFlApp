#! /usr/bin/env python

from thermos import app, db
from thermos.models import User
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
	db.create_all()
	db.session.add(User(username="termax", email="termax@nton.info", password="test"))
	db.session.add(User(username="mrwho", email="who@who.com", password="test"))
	db.session.commit()
	print 'Initialized the DB'

@manager.command
def dropdb():
	if prompt_bool(
		"Are you sure"):
		db.drop_all()
		print 'Dropped the DB'

if __name__ == '__main__':
	manager.run()