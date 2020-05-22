import click
from flask.cli import with_appcontext

from blog import db 
from blog.models import User, Post

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    print("db created")
    db.create_all()
