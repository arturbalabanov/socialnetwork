from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, HTML, Field, Submit
from crispy_forms.bootstrap import Alert
from django.core.urlresolvers import reverse
from django import forms

from timeline.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('timeline:create_post')
        self.helper.form_action = reverse('timeline:post-list')
        self.helper.form_id = 'new-post-form'
        # TODO: extract this mess in a template
        self.helper.layout = Layout(
            Div(
                Div(
                    HTML("Write on your timeline"),
                    css_class='panel-heading',
                ),
                Div(
                    Alert(
                        "<strong>Error:</strong> You cannot make an empty post",
                        css_class="alert-danger",
                        css_id="empty-post-error-message",
                    ),
                    Field('text', placeholder="What's on your mind?", css_class='form-control',
                          rows='3', cols='30'),
                    css_class='panel-body',
                ),
                Div(
                    Submit('submit', "Post"),
                    css_class='panel-footer',
                ),
                css_class='panel panel-default',
            )
        )

    def save(self, commit=True):
        post = super(CreatePostForm, self).save(commit=False)
        post.author = self.request.user

        if commit:
            post.save()

        return post
