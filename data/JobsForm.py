from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = IntegerField("Team leader", validators=[DataRequired()])
    job = StringField('Job', validators=[DataRequired()])
    work_size = IntegerField("Work size", validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is finished', validators=[DataRequired()])
    submit = SubmitField("Continue")
