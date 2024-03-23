#!/usr/bin/python3
"""web flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask('web_flask')
app.url_map.strict_slashes = False


@app.route('/states_list')
def list_of_states():
    """return html with unordered list of states"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """close database"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
