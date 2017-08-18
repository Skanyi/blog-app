from django import forms

class EmailForm(forms.Form):
    name=forms.CharField(label='Name')
    email=forms.EmailField(label='Email')
    message=forms.CharField(label=Message, widget=forms.TextArea(attrs={'rows': 5}))
    