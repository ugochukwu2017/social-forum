from django.forms import ModelForm

from .models import Booz,Tag,Comment,Like


class BoozForm(ModelForm):
    class Meta:
        model = Booz
        exclude = ('created_on','owner')


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class LikeForm(ModelForm):

    class Meta:
        model = Like
        exclude = ('booz','approved_like')
