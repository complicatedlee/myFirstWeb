from orm import Model, StringField, FloatField, BooleanField, TextField
import time, uuid

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

#定义一个user对象，把数据库表users和它关联起来
class User(Model):
    #类的属性，不是实例的属性，实例属性必须通过__init__
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    user_name = StringField(ddl='varchar(50)')
    content = TextField()
    created_at = FloatField(default=time.time)

