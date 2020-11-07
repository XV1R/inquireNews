from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import DataRequired

class searchForm(Form):
    search = TextField("Search...")