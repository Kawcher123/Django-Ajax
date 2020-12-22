from django import forms
from .models import USer

class studentRegister(forms.ModelForm):
    class Meta:
        model=USer
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'passwordid'}),
        }