from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileField,FileAllowed,FileRequired


class UploadForm(FlaskForm):
    description = TextAreaField('description',validators=[DataRequired()])

    photo = FileField('photo', validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'],'Select Image Files Only.')])