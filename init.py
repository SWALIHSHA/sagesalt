from flask import Flask, g, current_app
import sqlite3
import os
import click

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            os.path.join(current_app.instance_path, 'restaurent.sqlite'),
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db=None
    
    if 'db' in g:
        db = g.db

    if db is not None:
        g.pop('db', None)
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as schema:
        db.executescript(schema.read().decode('utf8'))

@click.command('init-db')
def init_db_cmd():
    init_db()
    click.echo('Reset menu table!')


@click.command('reset-order')
def reset_order_table():
    db = get_db()
    with current_app.open_resource('order-table-schema.sql') as schema:
        db.executescript(schema.read().decode('utf8'))
    click.echo(' reset order')


@click.command('reset-login')
def reset_login_table():
    db = get_db()
    with current_app.open_resource('login-schema.sql') as schema:
        db.executescript(schema.read().decode('utf8'))
    click.echo('reset login')

@click.command('reset-contact')
def reset_contact_table():
    db = get_db()
    with current_app.open_resource('contact_schema.sql') as schema:
        db.executescript(schema.read().decode('utf8'))
    click.echo('reset review')
    

def create_app():
    app = Flask(__name__)

    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_cmd)
    app.cli.add_command(reset_order_table)
    app.cli.add_command(reset_login_table)
    app.cli.add_command(reset_contact_table)
    return app