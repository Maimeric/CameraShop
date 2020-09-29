from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Form, ModelForm

from catalog.models import Comments, Order


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class CommentForm(forms.Form):
    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'email', 'address', 'postal_code', 'city']
