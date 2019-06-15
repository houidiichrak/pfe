from django import forms

class userFormLogin(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'Username'}),label='')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'Password'}),label='')


class workerPos(forms.Form):
    lat = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id' : 'lat', 'type' : 'hidden'}))
    lon = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id' : 'lon', 'type' : 'hidden'}))