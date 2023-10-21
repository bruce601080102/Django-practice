from django import forms
from myapp.samples.profiles_test.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email']