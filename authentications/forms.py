# from cProfile import label
# from email import message
# from tkinter import Widget
from tinymce.widgets import TinyMCE
from django import forms


class NewsletterForm(forms.Form):
    subject=forms.CharField()
    receiver =forms.CharField()
    message =forms.CharField(widget=TinyMCE(), label='Email Content')
