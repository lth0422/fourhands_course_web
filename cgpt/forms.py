# cocktail/forms.py
from django import forms

class Userform(forms.Form):
    user_input = forms.CharField(label='당신의 기분을 입력하세요', max_length=200)
