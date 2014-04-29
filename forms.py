# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.forms import Form, RadioSelect
from django.forms.fields import CharField, ChoiceField, FileField, BooleanField
from django.forms.widgets import Textarea, ClearableFileInput, TextInput
from model import Record, ActivityType, ActivitySport
from model import update_counter, Activity
from defines import ACTIVITY_TYPES, ACTIVITY_SPORTS, ACTIVITIES, DOMAIN,\
    URL_PHOTO
import re
from google.appengine.ext import ndb, db
import logging


def belongs_to_group(name, group):
    return re.match(group + r'_[0-9]+', name)

def get_id_in_group(name, group):
    match = re.match(group + r'_([0-9]+)', name)
    if match:
        return int(match.group(1))

def get_checkbox_field_group(form, group):
    for name in form.fields:
        if belongs_to_group(name, group):
            yield(form[name])
            
def init_checkbox_field_group(form, group_name, group_values):
    for value, i in zip(group_values, range(len(group_values))):
        field = BooleanField(required=False, label=value) 
        field.widget.label = value
        form.fields['{}_{}'.format(group_name, i)] = field 
        
def get_group_label(group_name, field_id):
    if group_name=='activity_type':
        return ACTIVITY_TYPES[field_id]
    if group_name=='activity_sport':
        return ACTIVITY_SPORTS[field_id]
    if group_name=='activity':
        return ACTIVITIES[field_id]

def update_group(name, val, group, model_cls):
    field_id = get_id_in_group(name, group)
    if field_id is not None and val: 
        update_counter(model_cls, field_id, get_group_label(group, field_id))
    return field_id is not None

    
class Page1Form(Form):
    #error_css_class = 'error'
    #activity = ChoiceField(choices=ACTIVITY_CHOICES, widget=RadioSelect(), required=False)
    my_activity = CharField(widget=Textarea(attrs={'rows': 3, 'columns': 50, 'placeholder': "Vpíšte sem Vašu aktivitu"}), required=False)
    joke = CharField(widget=Textarea, required=False)
    photo = FileField(widget=ClearableFileInput, required=False)
    name = CharField(widget=TextInput(attrs={'placeholder': 'Vaše meno...'}), required=False)
    
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
    
    def activities_part_1(self):
        acts = list(self.activities())
        return acts[:len(acts)/2+3]
    
    def activities_part_2(self):
        acts = list(self.activities())
        return acts[len(acts)/2+3:]
    
    def save(self, photo):
        rec = Record()
        rec.my_activity = self.cleaned_data['my_activity']
        rec.joke = self.cleaned_data['joke']
        if photo:
            rec.photo = db.Blob(photo);
            
        rec.name = self.cleaned_data['name']
        rec.put()
        logging.info('Key: %s', rec.key.urlsafe())
        rec.photo_link = DOMAIN + URL_PHOTO + '?key=' + rec.key.urlsafe()
        rec.put() 
        
        for name, val in self.cleaned_data.items():
            if update_group(name, val, 'activity', Activity): 
                continue
            if update_group(name, val, 'activity_sport', ActivitySport): 
                continue
            if update_group(name, val, 'activity_type', ActivityType): 
                continue
                
            

        
        