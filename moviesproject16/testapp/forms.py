from django import forms
from testapp.models import MoviesInformation
class MovieForm(forms.ModelForm):
    class Meta:
        model=MoviesInformation
        fields="__all__"
