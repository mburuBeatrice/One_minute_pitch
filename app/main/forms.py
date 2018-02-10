from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):

    title = StringField('Comment title',validators=[Required()])
    comment = TextAreaField('Pitch comment', validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    category =  SelectField('category',choices=[('pickup lines','Pickup Lines'),
                                                        ('product','Product Pitch'),
                                                        ('interview','Interview Pitch'),
                                                        ('promotion','Promotion Pitch')], validators=[Required()])
    author= StringField('author', validators=[Required()])
    body = TextAreaField('body', validators=[Required()])
    submit = SubmitField('Submit')
    

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')    