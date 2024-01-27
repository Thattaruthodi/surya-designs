from django import forms
from app.models import Review

# class Reviewform(forms.ModelForm):
#     content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"write review"}))

#     class Meta:
#         model = Review
#         fields = ['content','rating']