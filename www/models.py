# !usr/bin/env python
# _*_ coding:utf-8 _*_

print('\n====== modles.py start ======\n')

import time, uuid

from transwarp.orm import Model, StringField, BooleanField, FloatField, TextField
from transwarp.db import next_id


class User(Model):
	__table__ = 'users'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	email = StringField(updatable=False, ddl='varchar(50)')
	passwork=StringField(ddl='varchar(50)')
	admin = BooleanField()
	name = StringField(ddl='varchar(50)')
	image = StringField(ddl='varchar(500)')
	created_at = FloatField(updatable=False, default=time.time)

class Blog(Model):
	__table__ = 'blogs'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	user_id = StringField(updatable=False, ddl='varchar(50)')
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	name = StringField(ddl='varchar(50)')
	summary = StringField(ddl='varchar(200)')
	cotent = TextField()
	created_at = FloatField(updatable=False, default=time.time)

class Comment(Model):
	__table__ = 'comments'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	blog_id = StringField(updatable=True, ddl='varchar(50)')
	user_id = StringField(updatable=True, ddl='varchar(50)')
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	content = TextField()
	created_at = FloatField(updatable=False, default=time.time)

print('\n====== modles.py end ======\n')