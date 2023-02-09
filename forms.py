from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange 

class CreateForm(FlaskForm):
    restaurant_name = StringField('Restaurant Name', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=0, max=5)])
    review_text = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Post')