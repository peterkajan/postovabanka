from django.core.exceptions import ValidationError
from django.forms import Form
from django.forms.fields import CharField

class Page1Form(Form):
    error_css_class = 'error'