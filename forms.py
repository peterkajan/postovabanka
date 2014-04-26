from django.core.exceptions import ValidationError
from django.forms import Form, RadioSelect
from django.forms.fields import CharField, ChoiceField, FileField, BooleanField
from django.forms.widgets import Textarea, ClearableFileInput
from model import Record
from defines import ACTIVITY_TYPES, ACTIVITY_SPORTS, ACTIVITIES
import re


def get_checkbox_field_group(form, group):
    for name in form.fields:
        print name
        if re.match(group + r'_[0-9]+', name):
            yield(form[name])
            
def init_checkbox_field_group(form, group_name, group_values):
    for value, i in zip(group_values, range(len(group_values))):
        field = BooleanField(required=False, label=value) 
        field.widget.label = value
        form.fields['{}_{}'.format(group_name, i)] = field 
    
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
            
        init_checkbox_field_group(self, 'activity_type', ACTIVITY_TYPES)
        init_checkbox_field_group(self, 'activity_sport', ACTIVITY_SPORTS)
        init_checkbox_field_group(self, 'activity', ACTIVITIES)
        
            
    def activity_types(self):
        return get_checkbox_field_group(self, 'activity_type')
                
    @property
    def activity_type_labels(self):
        return ACTIVITY_TYPES
                
    @property
    def activity_sport_labels(self):
        return ACTIVITY_SPORTS
    
    def activity_sports(self):
        return get_checkbox_field_group(self, 'activity_sport')
                
    @property
    def activity_labels(self):
        return ACTIVITIES
    
    def activities(self):
        return get_checkbox_field_group(self, 'activity')
           
    
    def save(self):
        rec = Record()
        rec.activity = self.cleaned_data['activity']
        rec.joke = self.cleaned_data['joke']
        rec.put()