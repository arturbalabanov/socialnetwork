from crispy_forms.bootstrap import InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div, Field
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse

from users.models import UserProfile


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.widgets.TextInput)
    password1 = forms.CharField(widget=forms.widgets.PasswordInput)
    password2 = forms.CharField(widget=forms.widgets.PasswordInput)
    email = forms.CharField(widget=forms.widgets.EmailInput)
    gender = forms.TypedChoiceField(
        widget=forms.widgets.RadioSelect,
        choices=UserProfile.GENDER_CHOICES)

    class Meta:
        model = UserProfile
        # We don't want the user to be able to set "is_admin" and "is_staff"
        fields = ['username', 'password1', 'password2', 'email', 'gender']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "",
                'username',
                'password1',
                'password2',
                'email',
                InlineRadios('gender'),
            ),
            ButtonHolder(
                Submit('submit', "Register")
            )
        )

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The passwords don't match.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', "Log in"))


class SearchForm(forms.Form):
    q = forms.CharField(widget=forms.widgets.TextInput)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'navbar-left navbar-form'
        self.helper.form_show_labels = False
        self.helper.form_method = 'get'
        self.helper.form_action = reverse('users:search_results')
        self.helper.layout = Layout(
            Div(
                Field('q', placeholder="Search for other users", css_class='form-control'),
                Div(
                    Submit(name='', value="Go", css_class='btn btn-default'),
                    css_class='input-group-btn'
                ),
                css_class='input-group',
            ),
        )
