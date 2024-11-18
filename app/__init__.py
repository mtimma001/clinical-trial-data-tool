from flask import g
from .app_factory import create_app
from .db_connect import close_db, get_db

app = create_app()
app.secret_key = 'my-super-secret'

# Register Blueprints
from app.blueprints.participants import participants
app.register_blueprint(participants)

from . import routes

@app.before_request
def before_request():
    g.db = get_db()

# Setup database connection teardown
@app.teardown_appcontext
def teardown_db(exception=None):
    close_db(exception)
