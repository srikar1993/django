from django import forms
from django.core import validators


class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollNo = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput)
    rpwd = forms.CharField(label='Password(Again)', widget=forms.PasswordInput)
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    def passwordcheck(self):
        inputpwd = self.cleaned_data['pwd']
        inputrpwd = self.cleaned_data['rpwd']
        if inputpwd != inputrpwd:
            raise forms.ValidationError('Passwords not matched!!!')

    def clean(self):
        cleaned_data = super().clean()
        self.passwordcheck()
        bot_handler_value = cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            raise forms.ValidationError('Thanks Bot!!!')

        
