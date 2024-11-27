from django import forms
from django.contrib.auth.forms import UserCreationForm

from new_app.models import Login, seller, coustmer, blog


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password = forms.CharField(label="passord", widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ('username', 'password')


class  sellerRegister(forms.ModelForm):
    class Meta:
        model= seller
        fields ="__all__"
        exclude =("user",)

class  coustmerRegister(forms.ModelForm):
    class Meta:
        model= coustmer
        fields ="__all__"
        exclude =("user",)

class blogform(forms.ModelForm):
    class Meta:
        model=blog
        fields = "__all__"




