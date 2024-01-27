from app1.models import * 
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        help_texts={'username':''}
        widgets={'password':forms.PasswordInput}
 
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile 
        fields=['adress','profile_pic']
     