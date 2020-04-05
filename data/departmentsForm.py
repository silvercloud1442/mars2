from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DepartmentsForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    chief = StringField('Chief', validators=[DataRequired()])
    members = StringField("Members", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField("Continue")
