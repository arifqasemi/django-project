from django import forms
from .models import User
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ( "email","password","image")
        error_messages ={
            "email":{"required": "Please enter a username"},
            "password":{"required": "Please enter a password"},
            "image":{"required": "Please enter a image"}

        }
