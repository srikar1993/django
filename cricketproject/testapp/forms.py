from django import forms
from testapp.models import Cricket

class CricketForm(forms.ModelForm):
    class Meta:
        model = Cricket
        fields = '__all__'
