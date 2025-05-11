# https://docs.djangoproject.com/en/5.2/topics/forms/
from django import forms

class ReviewForm(forms.Form):
    user    = forms.CharField(max_length=100, label="Your Name")
    rating  = forms.IntegerField(min_value=1, max_value=5, label="Rating (1–5)")
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), required=False, label="Comment")
