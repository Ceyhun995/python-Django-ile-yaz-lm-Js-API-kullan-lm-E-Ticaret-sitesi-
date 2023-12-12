from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    
    class Meta:
        
        model =Comment
        fields =["comment_message"]

class UpdateCommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields =["comment_message"]