from django import forms

class AddItemsForm(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()

