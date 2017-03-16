from django import forms

class movieform(forms.Form):
    moviename=forms.CharField(label='Movie', max_length=100)

    searchterm=forms.CharField(label='Search', max_length=100)
        