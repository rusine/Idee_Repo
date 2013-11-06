from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags


class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'first name': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'last name': 'Last Name'}))
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'username': 'Username'}))
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'email': 'Email Address'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'password': 'Password'}))
    passwordconfirm = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'password': 'Password Confirmation'}))
 
    def is_valid(self):
        form = super(SignupForm, self).is_valid()
        for x, error in self.errors.iteritems():
            if x != '__all__':
                self.fields[x].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

    class Meta:
    	fields = ['username', 'first_name', 'last_name', 'email', 'password',
                  'passwordconfirm']
        model = User


class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'username': 'Username'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'password': 'Password'}))
 
    def is_valid(self):
        form = super(AuthenticateForm, self).is_valid()
        for x, error in self.errors.iteritems():
            if x != '__all__':
                self.fields[x].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

