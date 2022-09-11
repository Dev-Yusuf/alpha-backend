
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserInfo



class Registration(UserCreationForm):

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name',  'username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password': None,
            'password2': None,
        }
        
# this block of code loops through the fields and style them based of the class picked by css
    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})