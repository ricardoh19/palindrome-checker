from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Text(FlaskForm):
    text_field = StringField('text', validators=[DataRequired()])
