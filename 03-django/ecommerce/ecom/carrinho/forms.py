from django import forms

from carrinho.models import Person


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('address_street', 'address_number', 'address_cep',
                  'address_city', 'address_state')

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
