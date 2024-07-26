# cgpt/forms.py
from django import forms

class Userform(forms.Form):
    user_input = forms.CharField(max_length=200)
