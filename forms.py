from django.core.exceptions import ValidationError
from django.forms import Form, RadioSelect
from django.forms.fields import CharField, ChoiceField, FileField
from django.forms.widgets import Textarea, ClearableFileInput

ACTIVITY_CHOICES=[
    ('activity1','activity1'),
    ('activity2','activity2'),
]
                  

class Page1Form(Form):
    error_css_class = 'error'
    activity = ChoiceField(choices=ACTIVITY_CHOICES, widget=RadioSelect())
    joke = CharField(widget=Textarea)
    photo = FileField(widget=ClearableFileInput)
    
#     def clean_id_num(self):
#         if self.cleaned_data['id_num'] == 'error':
#             raise ValidationError('Nespravne cislo')