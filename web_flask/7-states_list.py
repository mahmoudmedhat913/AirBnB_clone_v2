#!/usr/bin/python3
"""web flask application"""
from flask import Flask, render_template
import models
from models.state import State
app = Flask('web_flask')
app.url_map.strict_slashes = False


@app.route('/states_list')
def list_of_states():
    """return html with unordered list of states"""
    states = sorted(models.storage.all('State').values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """close database"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
