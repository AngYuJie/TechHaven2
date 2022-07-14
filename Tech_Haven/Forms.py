from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, PasswordField, SubmitField, ValidationError, TextField, DecimalField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, InputRequired, Required
from flask_wtf import RecaptchaField

class LoginForm(Form):
    email = StringField('Email', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    recaptcha = RecaptchaField()

class RegisterForm(Form):
    first_name = StringField('First Name',[validators.Length(min=3, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=2, max=150), validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(), validators.Email("Invalid Email")])
    password = PasswordField('Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')
    securityQn = RadioField('Choose your security question', choices=[("What is your first car?","What is your first car?"), ("What is one of your siblings names?","What is one of your siblings names?"), ('What is a brand of footwear that you own?','What is a brand of footwear that you own?')], validators=[validators.DataRequired()])
    securityQnAns = StringField('What is the answer to the selected security question?', [validators.DataRequired()])
    street = StringField('Street', [validators.DataRequired()])
    postal_code = StringField('Postal Code', [validators.DataRequired()], render_kw={"placeholder": "000000"})
    unit_number = StringField('Unit Number', [validators.DataRequired()], render_kw={"placeholder": "#00-00"})
    mobile_number = StringField('Mobile Number', [validators.DataRequired()])
    recaptcha = RecaptchaField()


class ContactUsForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired("Please enter your first name")], render_kw={"placeholder": "First Name"})
    last_name = StringField('Last Name', [validators.DataRequired("Please enter your last name")], render_kw={"placeholder": "Last Name"})
    email = EmailField('Email', [validators.Email(), validators.DataRequired()], render_kw={"placeholder": "Email"})
    subject = StringField('Subject', [validators.DataRequired("Please enter a subject")], render_kw={"placeholder": "Subject"})
    inquiry = TextAreaField('Inquiry', [validators.DataRequired("Please enter your inquiry"), validators.Length(min=1, max=150)], render_kw={"placeholder": "Inquiry"})
    recaptcha = RecaptchaField()


class CreateReplyForm(Form):
    reply = TextAreaField('Reply', [validators.DataRequired("Please enter your reply"), validators.Length(min=1, max=150)], render_kw={"placeholder": "Reply"})
    recaptcha = RecaptchaField()


class ReviewForm(Form):
    rating = RadioField('Rating', choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')],  default='1', validators=[DataRequired()])
    title = StringField('Title', [validators.DataRequired("Please enter a title")])
    review = TextAreaField("Review", [validators.DataRequired("Please enter a review")])

class updateReviewForm(Form):
    updated_rating = RadioField('Rating', choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')])
    updated_title = StringField('Title', [validators.DataRequired("Please enter a title")])
    updated_review = TextAreaField("Review", [validators.DataRequired("Please enter a review")])


class createProductForm(Form):
    product_name = StringField('Product Name', [validators.DataRequired("Please enter Product Name")])
    product_price = DecimalField('Product Price', places=2)

class ForgetPasswordForm(Form):
    email = EmailField('Email Address',[validators.DataRequired(), validators.Email()])
    recaptcha = RecaptchaField()

class PasswordResetForm(Form):
    current_password = PasswordField('Current Password',[validators.DataRequired(), validators.Length(min=4, max=80)])
    submit = SubmitField(label='Login', validators=[DataRequired()])

class OTPForm(Form):
    email = EmailField('Email Address',[validators.DataRequired(), validators.Email()])
    OTP = StringField('OTP PIN', [validators.Length(min=6, max=10), validators.DataRequired()])
    recaptcha = RecaptchaField()

class OTPGform(Form):
    email = EmailField('Email Address',[validators.DataRequired(), validators.Email()])
    recaptcha = RecaptchaField()

class securityQnsForm(Form):
    answer = StringField('Answer', [validators.DataRequired("Please enter security question answer")])
    submit = SubmitField(label='Login')
