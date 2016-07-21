from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PersonCreateForm(LoginForm):
    states = ('SP', 'RJ', 'AC', 'RS')

    password_check = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    address_street = forms.CharField()
    address_number = forms.CharField()
    address_cep = forms.CharField()
    address_city = forms.CharField()
    address_state = forms.ChoiceField(choices=states)
