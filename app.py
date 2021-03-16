from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import ldclient
from ldclient.config import Config

ldclient.set_config(Config(sdk_key = "sdk-d42af0f3-878a-47a1-ae5f-a639a0a5c5be"))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

show_feature = ldclient.get().variation("populate-list", {"key": "user@test.com"}, False)
if show_feature:
# application code to pre-populate the list
    todos = ["Create An App", "Deploy LD", "Record Demo"]
else:
# application code to provide an empty list
    todos = []


class TodoForm(FlaskForm):
    todo = StringField("Todo")
    submit = SubmitField("Add Todo")

@app.route('/', methods=["GET", "POST"])
def index():
    if 'todo' in request.form:
        todos.append(request.form['todo'])     
    return render_template('index.html', todos=todos, template_form=TodoForm())