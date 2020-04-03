from django import forms
from django.core.files.images import get_image_dimensions
from .models import Profile


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(max_length=32, label='First Name')
    last_name = forms.CharField(max_length=32, label='Last Name')
    username = forms.CharField(max_length=32, label='User Name')
    password = forms.CharField(max_length=32, min_length=8, label='Password', widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('my_instruments', 'short_description', 'years_of_musical_experience', 'avatar')

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        try:
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')
        except AttributeError:
            pass
        return avatar

