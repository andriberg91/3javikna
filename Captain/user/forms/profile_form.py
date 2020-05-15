from django.forms import ModelForm, widgets
from user.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'id', 'user']
        widgets = {
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'}),
            'user_name' : widgets.TextInput(attrs={'class' : 'form-control'})
        }