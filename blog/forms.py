from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import My_blog,Comment



class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class PostForm(forms.ModelForm):

    class Meta:
        model =My_blog
        fields = ('title', 'post_body', 'image')
        widgets = {
            'title': forms.TextInput(attrs ={'class': 'form-control'}),
            'post_body': forms.Textarea(attrs ={'class': 'form-control'}),
            'image': forms.FileInput(attrs ={'class': 'form-control'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model =Comment
        fields = ('post_body',)


class NovenaCommentForm(forms.ModelForm):

    class Meta:
        model =Comment
        fields = ('post_body',)


class dailyPrayersForm(forms.Form):
    title = forms.CharField()
    prayer = forms.CharField(widget=forms.Textarea)
    
class NewsLetterForm(forms.Form):
    title = forms.CharField()
    letter = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}))