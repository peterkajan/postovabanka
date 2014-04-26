from django.core.exceptions import ValidationError
from django.forms import Form, RadioSelect
from django.forms.fields import CharField, ChoiceField, FileField, BooleanField
from django.forms.widgets import Textarea, ClearableFileInput
from model import Record
from defines import ACTIVITY_TYPES


class Page1Form(Form):
    #error_css_class = 'error'
    #activity = ChoiceField(choices=ACTIVITY_CHOICES, widget=RadioSelect(), required=False)
    joke = CharField(widget=Textarea, required=False)
    photo = FileField(widget=ClearableFileInput, required=False)
    
#     def clean_id_num(self):
#         if self.cleaned_data['id_num'] == 'error':
#             raise ValidationError('Nespravne cislo')

    def __init__(self, *args, **kwargs):
        super(Page1Form, self).__init__(*args, **kwargs)
            
        for activity_type, i in zip(ACTIVITY_TYPES, range( len(ACTIVITY_TYPES))): 
            self.fields['activity_type_{}'.format(i)] = BooleanField(required=False)
            
    def activity_types(self):
        for name in self.fields:
            if name.startswith('activity_type_'):
                yield(self[name])
                
    @property
    def activity_labels(self):
        return ACTIVITY_TYPES       
    
    def save(self):
        rec = Record()
        rec.activity = self.cleaned_data['activity']
        rec.joke = self.cleaned_data['joke']
        rec.put()