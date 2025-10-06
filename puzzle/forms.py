from django import forms

class PuzzleForm(forms.Form):
    number = forms.IntegerField(label="Enter a number", min_value=0)
    text = forms.CharField(label="Enter a word or phrase", max_length=100)
