from django import forms
from blog.models import Post, Comment

#putting models into forms:

class PostForm(forms.ModelForm):
    #connecting with model and choosing fileds to access
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')
        #some attributes needed later working on JS and CSS
        widgets = {
            'title':forms.TextInput(attrs = {'class': 'textinputclass'}),
            'text':forms.Textarea(attrs = {'class': 'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author':forms.TextInput(attrs = {'class': 'textinputclass'}),
            #pretty same but without 'postcontent' class for purpose
            'text':forms.Textarea(attrs = {'class': 'editable medium-editor-textarea'})
        }
