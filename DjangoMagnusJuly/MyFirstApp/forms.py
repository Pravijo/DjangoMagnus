from django import forms


class UserForm(forms.Form):
    user = forms.CharField(label="Enter the Username")
    email = forms.EmailField(label="Enter the Email")
    password = forms.CharField(label="Enter the Password",widget=forms.PasswordInput)
