from django import forms
from testApp.models import Student

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'