from django.contrib.auth.forms import AuthenticationForm


class SisgerecuAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(SisgerecuAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class': 'username', 'placeholder': 'username'})
        self.fields['password'].widget.attrs.update({'class': 'password', 'placeholder': 'password'})