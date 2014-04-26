from django.core.exceptions import ValidationError
from django.forms import Form, RadioSelect
from django.forms.fields import CharField, ChoiceField, FileField, BooleanField
from django.forms.widgets import Textarea, ClearableFileInput
from model import Record

ACTIVITY_TYPES=[
    'activity1',
    'activity2',
]
                  

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
        self.activity_types = ACTIVITY_TYPES
            
        for activity_type, i in zip(ACTIVITY_TYPES, range( len(ACTIVITY_TYPES))):
            self.fields['activity_type_{}'.format(i)] = BooleanField(required=False, label=activity_type)
            self.activity_types.append( self.fields['activity_type_{}'.format(i)] )
    
    def save(self):
        rec = Record()
        rec.activity = self.cleaned_data['activity']
        rec.joke = self.cleaned_data['joke']
        rec.put()