from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
