from django import forms
from djng.forms.angular_model import NgModelFormMixin
from djng.styling.bootstrap3.forms import Bootstrap3FormMixin

from timeline.models import Post


class CreatePostForm(NgModelFormMixin, forms.ModelForm, Bootstrap3FormMixin):
    text = forms.CharField(widget=forms.Textarea({'cols': '30', 'rows': '3'}), label="")

    class Meta:
        model = Post
        fields = ['text']

    def __init__(self, *args, **kwargs):
        kwargs.update(scope_prefix='create_post_form')
        super(CreatePostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super(CreatePostForm, self).save(commit=False)
        post.author = self.request.user

        if commit:
            post.save()

        return post
